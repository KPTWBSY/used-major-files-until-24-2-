
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = ((-1.0,-1.0,-1.0),(1.0,-1.0,-1.0),
            (1.0,1.0,-1.0), (-1.0,1.0,-1.0), (-1.0,-1.0,1.0),
            (1.0,-1.0,1.0), (1.0,1.0,1.0), (-1.0,1.0,1.0))

normals = 

myview =3

xRot = 0.0
yRot = 0.0

def polygonSmooth( a, b, c , d):
	glBegin(GL_POLYGON)
	glNormal3fv(normals[a])
	glVertex3fv(vertices[a])
	glNormal3fv(normals[b])
	glVertex3fv(vertices[b])
	glNormal3fv(normals[c])
	glVertex3fv(vertices[c])
	glNormal3fv(normals[d])
	glVertex3fv(vertices[d])
	glEnd()



def cubeSmooth():
	polygonSmooth( , , , )
	polygonSmooth( , , , )
	polygonSmooth( , , , )
	polygonSmooth( , , , )
	polygonSmooth( , , , )
	polygonSmooth( , , , )



def MyDisplay():
    global myview
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   
    glLoadIdentity()

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glLightfv(GL_LIGHT0, GL_POSITION, (8.0, 0.0, 8.0, 1.0))

    if myview == 0:
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif myview == 1:
        gluLookAt(0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
    elif myview == 2:
        gluLookAt(5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif myview == 3:
        gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


    glColor3f(1.0, 1.0, 1.0)

    cubeSmooth()
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
    glutCreateWindow('colorcube viewpoint Python')

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