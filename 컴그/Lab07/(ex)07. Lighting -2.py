from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

myview =0

light_ambient = (0.2, 0.1, 0.1, 1.0)  #Ia
light_diffuse = (1, 0.75, 1, 1.0)  #Id
light_specular = (1.0, 0.75, 0.5, 1.0)  #Is
light_position1 = (-10.0, 5.0, -8.0, 1.0)
light_position2 = (15.0, 8.0, 8.0, 1.0)

no_mat = (0.0, 0.0, 0.0, 1.0)
mat_ambient = (0.5, 0.1, 0.7, 1.0) #Ka
mat_diffuse = (1.0, 0.5, 1.0, 1.0) #kd
mat_specular = (1.0, 0.75, 1.0, 1.0) #Ks


no_shininess = 0.0  # Shininess Coefficient
low_shininess = 10.0 # Shininess Coefficient
high_shininess = 100 # Shininess Coefficient


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