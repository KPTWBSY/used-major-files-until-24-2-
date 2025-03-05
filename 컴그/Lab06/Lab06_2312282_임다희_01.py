
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

vertices = ((-1.0,-1.0,-1.0),(1.0,-1.0,-1.0),
            (1.0,1.0,-1.0), (-1.0,1.0,-1.0), (-1.0,-1.0,1.0),
            (1.0,-1.0,1.0), (1.0,1.0,1.0), (-1.0,1.0,1.0))

myview =3

xRot = 0.0
yRot = 0.0

def flatNormal(v1, v2, v3):
   
    v1= np.array(v1)
    v2= np.array(v2)
    v3= np.array(v3)

    cross = np.cross(v3-v2,v1-v2)  # 학생들이 작성
    length = np.linalg.norm(cross)
    normal = cross/length     # 학생들이 작성
    print(normal)
    return normal

def polygonNormal( a, b, c , d):

    normalvector=flatNormal(vertices[a],vertices[b],vertices[c])  # 학생들이 작성

    glBegin(GL_POLYGON)
    glNormal3fv(normalvector)
    glVertex3fv(vertices[a])
    glNormal3fv(normalvector)
    glVertex3fv(vertices[b])
    glNormal3fv(normalvector)
    glVertex3fv(vertices[c])
    glNormal3fv(normalvector)
    glVertex3fv(vertices[d])
    glEnd()

def cubeFlat():
    polygonNormal(0,3,2,1) #00-1
    polygonNormal(0,1,5,4) #0-10
    polygonNormal(5,4,7,6) #00-1
    polygonNormal(5,1,2,6) #100
    polygonNormal(7,6,2,3) #010
    polygonNormal(4,7,3,0) #-100

def MyDisplay():
    global myview
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (1, 1, 1, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glLightfv(GL_LIGHT0, GL_POSITION, (8.0, 0.0, 8.0, 1.0))

    gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
   
    cubeFlat()
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
    glutCreateWindow('cube with normal vector')

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