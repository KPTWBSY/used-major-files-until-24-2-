from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


myview =0

# 상수를 미리 정의. (값 바꿀 수 있다?)
light_ambient = (0.1, 0.1, 0.1, 1.0)  #Ia
light_diffuse = (0, 0, 1.0, 1.0)  #Id
light_specular = (0, 0, 1.0, 1.0)  #Is
light_position1 = (-15.0, 8.0, 8.0, 1.0)
light_position2 = (15.0, 8.0, 8.0, 1.0)

no_mat = (0.0, 0.0, 0.0, 1.0)
mat_ambient = (0.7, 0.7, 0.7, 1.0) #Ka
mat_diffuse = (0.1, 0.5, 0.8, 1.0) #kd
mat_specular = (1.0, 1.0, 1.0, 1.0) #Ks


no_shininess = 0.0  # Shininess Coefficient
low_shininess = 5.0 # Shininess Coefficient
high_shininess = 100.0 # Shininess Coefficient


def MyDisplay():
    global myview
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()


    # light  채워 넣기

    #glLight(GL_LIGHT0, GL_DIFFUSE,light_diffuse)
    #glLight(GL_LIGHT0, GL_AMBIENT,light_diffuse)
    glLight(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLight(GL_LIGHT0, GL_POSITION, light_position2)


    gluLookAt(0.0, 0.0, 13.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) #카메라 위치.



    #object1
    glPushMatrix()
    glTranslatef(-3, 0.0, 0.0)

    # material  채워 넣기

    glMaterial(GL_FRONT,GL_SPECULAR,mat_specular)
   

    glutSolidSphere(1.0, 40, 40)
    glPopMatrix()

    #object2
    glPushMatrix()
    # material  채워 넣기
    glMaterial(GL_FRONT, GL_AMBIENT,mat_ambient)
    glutSolidSphere(1.0, 40, 40)
    glPopMatrix()


    #object3
    glPushMatrix()
    glTranslatef(3, 0.0, 0.0)

	# material  채워 넣기
    glMaterial(GL_FRONT, GL_DIFFUSE, mat_diffuse)
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