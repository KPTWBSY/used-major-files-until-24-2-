import numpy as np
import matplotlib.pyplot as plt
student=['1','2','3','4']
scores=np.array([[90,70,85],[95,88,80],[65,75,85],[90,92,100]])
print(scores)

stu_0=np.mean(scores,axis=1)
print(stu_0)

stu_1=np.mean(scores,axis=0)
print(stu_1)

X=[20,40,60,80]
np_student=np.array(student)
plt.bar(np_student,stu_0)
plt.show()

    

