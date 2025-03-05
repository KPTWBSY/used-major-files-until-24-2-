
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = ((-1.0,-1.0,-1.0),(1.0,-1.0,-1.0),
            (1.0,1.0,-1.0), (-1.0,1.0,-1.0), (-1.0,-1.0,1.0),
            (1.0,-1.0,1.0), (1.0,1.0,1.0), (-1.0,1.0,1.0))

colors = ((0.0,0.0,0.0),(1.0,0.0,0.0),
          (1.0,1.0,0.0), (0.0,1.0,0.0), (0.0,0.0,1.0),
          (1.0,0.0,1.0), (1.0,1.0,1.0), (0.0,1.0,1.0))

myview =0


def polygon( a, b, c , d):
	glBegin(GL_POLYGON)
	glColor3fv(colors[a])
	glVertex3fv(vertices[a])
	glColor3fv(colors[b])
	glVertex3fv(vertices[b])
	glColor3fv(colors[c])
	glVertex3fv(vertices[c])
	glColor3fv(colors[d])
	glVertex3fv(vertices[d])
	glEnd()


def colorcube(): # 학생들이 수정
    polygon(0, 1, 2, 3)
    polygon(0, 1, 5, 4)
    polygon(4, 5, 6, 7)
    polygon(5, 1, 2, 6)
    polygon(6, 2, 3, 7)
    polygon(4, 7, 3, 0)


def MyDisplay():
    global myview
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    if myview == 0:  # front view
        gluLookAt(0.0,0.0,5.0,0.0,0.0,0.0,0.0,1.0,0.0)
    elif myview == 1: # top view
        gluLookAt(0.0,5.0,0.0,0.0,0.0,0.0,0.0,0.0,0.1)
    elif myview == 2: # side view
        gluLookAt(5.0,0.0,0.0,0.0,0.0 ,0.0 ,0.0 ,1.0 , 0.0)
    elif myview == 3: # perspective view
        gluLookAt(0.0,0.0,0.0,0.0,0.0,-1.0,0.0,1.0,0.0)

    colorcube()
    glutSwapBuffers()


def myReshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glFrustum (left, right, bottom, top, near distance, far distance)
    if w <= h:
        glFrustum(-2.0, 2.0, -2.0 * float(h)/ float(w), 2.0* float(h) / float(w), 2.0, 20.0)
    else:
        glFrustum(-2.0, 2.0, -2.0 * float(w)/ float(h), 2.0* float(w) / float(h), 2.0, 20.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow('color cube viewpoint Python')
    glutReshapeFunc(myReshape)
    glutDisplayFunc(MyDisplay)

    glutAttachMenu(GLUT_RIGHT_BUTTON)

    glEnable(GL_DEPTH_TEST)
    glutMainLoop()


if __name__ == "__main__":
    main()