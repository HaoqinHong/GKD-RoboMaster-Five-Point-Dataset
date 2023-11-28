import os
os.chdir(r'E:/ProgrammingProjects/PythonProjects/DeepLearning/SWU-GKD-RMUC')
f = open("train.txt", mode="a", encoding="utf-8")
for i in range(1, 5497):
    f.write("E:\ProgrammingProjects\PythonProjects\DeepLearning\SWU-GKD-RMUC\_train\images\{:04d}.jpg\n".format(i))
f.close()
print("FINISH")