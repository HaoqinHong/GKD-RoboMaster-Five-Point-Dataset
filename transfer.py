import os
os.chdir(r'E:/ProgrammingProjects/PythonProjects/DeepLearning/RM2023/SWU-GKD-RMUC')
f = open("train.txt", mode="a", encoding="utf-8")
for i in range(1, 5498):
    f.write("E:\ProgrammingProjects\PythonProjects\DeepLearning\RM2023\SWU-GKD-RMUC\_train\images\{:04d}.jpg\n".format(i))
f.close()
f1 = open("test.txt", mode="a", encoding="utf-8")
for i in range(1, 608):
    f1.write("E:\ProgrammingProjects\PythonProjects\DeepLearning\RM2023\SWU-GKD-RMUC\_test\images\{:d}.jpg\n".format(i))
f1.close()
print("FINISH")