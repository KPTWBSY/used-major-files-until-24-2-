from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from ObjLoader import *


myview =3

light_ambient = (0.2, 0.1, 0.1, 1.0)
light_diffuse = (1, 0.75, 1, 1.0)
light_specular = (1.0, 0.75, 0.5, 1.0)
light_position1 = (10.0, 5.0, -8.0, 1.0)

xRot = 0.0
yRot = 0.0

obj = 0


def loadRabbit():
    global obj
    index_count = len(obj.vertex_index)
    for i in range(index_count):
        # START TRIANGLE
        if i % 3 == 0:
            glBegin(GL_POLYGON)
        glNormal3fv((obj.model[i * 3 + index_count * 3 + index_count * 2 ]
                     , obj.model[i * 3 + index_count * 3 + index_count * 2 + 1]
                     , obj.model[i * 3 + index_count * 3 + index_count * 2 + 2]
                     ))
        glVertex3fv((obj.model[i * 3]
                    ,obj.model[i * 3 + 1]
                    ,obj.model[i * 3 + 2]))
        # END TRIANGLE
        if i % 3 == 2:
            glEnd()

def MyDisplay():
    global myview
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position1)

    gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)
    glScalef(3, 3, 3)
    glColor3f(1.0, 1.0, 1.0)
    #cubeFlat()
    #cubeSmooth()
    global obj
    obj = ObjLoader()
    obj.load_model("res/bunny_smooth.obj")
    loadRabbit()
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
    #glShadeModel(GL_SMOOTH)
    glutReshapeFunc(myReshape)
    glutDisplayFunc(MyDisplay)

    glutAttachMenu(GLUT_RIGHT_BUTTON)


    glutMainLoop()


if __name__ == "__main__":
    main()
    #loadRabbit()