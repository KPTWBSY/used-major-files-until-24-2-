#토끼 모델에 smooth shading을 적용한다.
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from ObjLoader import *

myview =3

xRot = 0
yRot = 0

obj = 0

def loadRabbit():
    global obj
    index_count = len(obj.vertex_index)
    for i in range(index_count): # 폴리곤을 생성한다.
        # START TRIANGLE
        if i % 3 == 0: # 3의 배수 번째 인덱스의 점에서 하나의 폴리곤 생성 시작.
            glBegin(GL_POLYGON)
        glNormal3fv((obj.model[i * 3 + index_count * 3 + index_count * 2 ]
                     , obj.model[i * 3 + index_count * 3 + index_count * 2 + 1]
                     , obj.model[i * 3 + index_count * 3 + index_count * 2 + 2]
                     )) # Smooth Shading을 위해 각 점마다 고유한 법선벡터 하나를 계산해 적용한다.
        glVertex3fv((obj.model[i * 3]
                    ,obj.model[i * 3 + 1]
                    ,obj.model[i * 3 + 2])) # 점의 x,y,z좌표를 glVertex3fv에 넣어 폴리곤을 구성하는 점에 해당 점을 포함시킨다.
        # END TRIANGLE
        if i % 3 == 2: # 3의 배수+2번째 인덱스의 점에서 폴리곤 생성 종료.
            glEnd()

def MyDisplay():
    global myview
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    #광원을 넣는다.
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    #주변광. r,g,b 알파값이 각각 0.2,0.2,0.2,1.0
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    #확산광. r,g,b,알파값이 각각 0.5, 0.5,0.5,1.0
    glLightfv(GL_LIGHT0, GL_POSITION, (8.0, 0.0, 8.0, 1.0))
    #광원의 위치. x,y,z값이 각각 8.0,0.0,8.0.

    gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    #카메라의 위치(3,3,3), 카메라가 바라보는 중심 위치(0,0,0), 카메라의 up vector(0,1,0).

    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)
    glScalef(3, 3, 3)
    glColor3f(1.0, 1.0, 1.0)

    global obj
    obj = ObjLoader()
    obj.load_model("res/bunny_smooth.obj")
    #토끼 모델을 로드한다.
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
