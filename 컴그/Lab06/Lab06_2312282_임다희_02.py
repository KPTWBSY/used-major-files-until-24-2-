
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from ObjLoader import *
import numpy as np


myview = 3

xRot = 0.0
yRot = 0.0

obj = 0


def flatNormal(v1, v2, v3):

	cross = np.cross(v3-v2,v1-v2)  # 학생들이 작성
	length = np.linalg.norm(cross)
	normal = (cross[0]/length, cross[1]/length,cross[2]/length)    # 학생들이 작성
	return normal


def loadRabbit():
	global obj
	#obj=ObjLoader()
	#obj.load_model("res/bunny.obj")
	index_count = len(obj.vertex_index)
	normal = None
	glBegin(GL_POLYGON)
	for i, vi in enumerate(obj.vertex_index):
		if i % 3 == 0:
			v1 = np.array((obj.model[i * 3]
						   , obj.model[i * 3 + 1]
						   , obj.model[i * 3 + 2]))
			v2 = np.array((obj.model[(i + 1) * 3]
						   , obj.model[(i + 1) * 3 + 1]
						   , obj.model[(i + 1) * 3 + 2]))
			v3 = np.array((obj.model[(i + 2) * 3]
						   , obj.model[(i + 2) * 3 + 1]
						   , obj.model[(i + 2) * 3 + 2]))

			normal=flatNormal(v1,v2,v3)  # 학생들이 작성

			if i > 0:
				glEnd()
				glBegin(GL_POLYGON)

		glNormal3fv((normal[0], normal[1], normal[2]))

		glVertex3fv((obj.model[i * 3]
					 , obj.model[i * 3 + 1]
					 , obj.model[i * 3 + 2]))
	glEnd()


def MyDisplay():
	global myview
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glLoadIdentity()

	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
	glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
	glLightfv(GL_LIGHT0, GL_POSITION, (8.0, 0.0, 8.0, 1.0))


	#gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
	gluLookAt(0.0, 0.0, 13.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


	glScalef(3, 3, 3)
	glColor3f(1.0, 1.0, 1.0)


	global obj
	obj = ObjLoader()
	obj.load_model("res/bunny.obj")
	loadRabbit()
	glutSwapBuffers()


def myReshape(w, h):
	glViewport(0, 0, w, h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	# glFrustum (left, right, bottom, top, near distance, far distance)
	if w <= h:
		glFrustum(-2.0, 2.0, -2.0 * float(h) / float(w), 2.0 * float(h) / float(w), 2.0, 20.0)
	else:
		glFrustum(-2.0, 2.0, -2.0 * float(w) / float(h), 2.0 * float(w) / float(h), 2.0, 20.0)
	glMatrixMode(GL_MODELVIEW)


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(500, 500)
	glutCreateWindow('Bunny normal')

	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_NORMALIZE)
	glutReshapeFunc(myReshape)
	glutDisplayFunc(MyDisplay)

	glutAttachMenu(GLUT_RIGHT_BUTTON)

	glutMainLoop()


if __name__ == "__main__":
	main()
