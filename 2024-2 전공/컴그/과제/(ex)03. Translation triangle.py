from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = ((0.25, -0.25, 0)
            , (-0.25, -0.25, 0)
            , (0, 0.25, 0))

def MyDisplay():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity() # vertices 위치를 초기값으로 초기화.
    glColor3f(1.0, 1.0, 1.0) #red

    #model 넣기
    glBegin(GL_TRIANGLES)
    glVertex3f(*vertices[0])
    glVertex3f(*vertices[1])
    glVertex3f(*vertices[2])
    glEnd()

    #translate(yellow)
    glTranslatef(0.5, 0.0, 0.0)
    glColor3f(1.0, 0, 0) #yellow

    #model 넣기
    glBegin(GL_TRIANGLES)
    glVertex3f(*vertices[0])
    glVertex3f(*vertices[1])
    glVertex3f(*vertices[2])
    glEnd()

    # LoadIdentity 안넣으면 vertices 값이 초기값이 아니라
    # 방금 translatef로 인해 바뀐 값으로 인식됨.
    glLoadIdentity()
    glTranslatef(0, 0.5, 0.0)
    glRotatef(90,0.0,0.0,1.0)
    glColor3f(0.0, 1.0, 0)  # green

    # model 넣기
    glBegin(GL_TRIANGLES)
    glVertex3f(*vertices[0])
    glVertex3f(*vertices[1])
    glVertex3f(*vertices[2])
    glEnd()

    glFlush()


def main():
    glutInit(sys.argv)
    glutCreateWindow('Model Transform')
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(MyDisplay)
    glutMainLoop()


if __name__ == "__main__":
    main()
