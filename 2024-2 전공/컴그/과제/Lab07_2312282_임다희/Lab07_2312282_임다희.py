import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ObjLoader import ObjLoader

myview =0

light_ambient = (0.2, 0.1, 0.1, 1.0)  #Ia
light_diffuse = (1.0, 0.75, 1.0, 1.0)  #Id
light_specular = (1.0, 0.75, 0.5, 1.0)  #Is
light_position1 = (-10.0, 5.0, -8.0, 1.0)
light_position2 = (-5.0, 10.0, 8.0, 1.0)

no_mat = (0.0, 0.0, 0.0, 1.0)
mat_ambient = (0.5, 0.1, 0.7, 1.0) #Ka
mat_diffuse = (1.0, 0.5, 1.0, 1.0) #kd
mat_specular = (1.0, 0.75, 1.0, 1.0) #Ks

no_shininess = 0.0  # Shininess Coefficient
low_shininess = 10.0 # Shininess Coefficient
high_shininess = 70 # Shininess Coefficient


def flatNormal(v1, v2, v3):

	cross = np.cross(v3-v2,v1-v2)  # 학생들이 작성
	length = np.linalg.norm(cross)
	normal = (cross[0]/length, cross[1]/length,cross[2]/length)    # 학생들이 작성
	return normal

def Rabbit():
    global myview
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position2)

    gluLookAt(0.0, 0.0, 13.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glScalef(3, 3,3 )

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, high_shininess)

    global obj
    obj=ObjLoader()
    obj.load_model("res/bunny.obj")
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

            normal = flatNormal(v1, v2, v3)  # 학생들이 작성

            if i > 0:
                glEnd()
                glBegin(GL_POLYGON)

        glNormal3fv((normal[0], normal[1], normal[2]))

        glVertex3fv((obj.model[i * 3]
                     , obj.model[i * 3 + 1]
                     , obj.model[i * 3 + 2]))

    glEnd()

    glutSwapBuffers()


def loadRabbit():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow('Bunny Lighting')

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)

    glShadeModel(GL_SMOOTH)
    glutReshapeFunc(myReshape)
    glutDisplayFunc(Rabbit)

    glutMainLoop()


def MyDisplay():
    global myview
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    # light 넣기
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position1)

    gluLookAt(0.0, 0.0, 13.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    #object1
    glPushMatrix()
    glTranslatef(-3, 0.0, 0.0)

    # material
    glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
    glMaterialf(GL_FRONT, GL_SHININESS, no_shininess)

    glutSolidSphere(1.0, 40, 40)
    glPopMatrix()

    #object2
    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, low_shininess)
    glutSolidSphere(1.0, 40, 40)
    glPopMatrix()


    #object3
    glPushMatrix()
    glTranslatef(3, 0.0, 0.0)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, high_shininess)
    glutSolidSphere(1.0, 40, 40)
    glPopMatrix()

    glutSwapBuffers()


def myReshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glFrustum (left, right, bottom, top, near distance, far distance)
    #if w <= h:
    #glFrustum(-2.0, 2.0, -2.0 * float(h)/ float(w), 2.0* float(h) / float(w), 2.0, 20.0)
    #else:
    glFrustum(-2.0, 2.0, -2.0 * float(w)/ float(h), 2.0* float(w) / float(h), 5.0, 30.0)
    glMatrixMode(GL_MODELVIEW)

def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow('Lighting')

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)

    glShadeModel(GL_SMOOTH)
    glutReshapeFunc(myReshape)
    glutDisplayFunc(MyDisplay)

    glutMainLoop()

if __name__ == "__main__":
    main()
    #loadRabbit()