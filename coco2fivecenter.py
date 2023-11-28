import os

def convert_four_points_to_five_points(label):
    # 解析四点格式的标签
    label_parts = label.strip().split()
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, label_parts[1:])

    # 计算五个关键点的坐标
    left_eye_x = (x1 + x4) / 2
    left_eye_y = (y1 + y4) / 2
    right_eye_x = (x2 + x3) / 2
    right_eye_y = (y2 + y3) / 2
    nose_x = (x1 + x2 + x3 + x4) / 4
    nose_y = (y1 + y2 + y3 + y4) / 4
    left_mouth_x = (x1 + x4) / 2
    left_mouth_y = (y1 + y4) / 2 + abs(y1 - y4) / 3
    right_mouth_x = (x2 + x3) / 2
    right_mouth_y = (y2 + y3) / 2 + abs(y2 - y3) / 3

    # 将五个关键点的坐标转换为 YOLOv5-face 格式
    image_width = 640  # 图像宽度
    image_height = 480  # 图像高度
    x_center = nose_x / image_width
    y_center = nose_y / image_height
    width = abs(right_eye_x - left_eye_x) / image_width
    height = abs(left_mouth_y - left_eye_y) / image_height
    left_eye_x = (left_eye_x / image_width) - x_center
    left_eye_y = (left_eye_y / image_height) - y_center
    right_eye_x = (right_eye_x / image_width) - x_center
    right_eye_y = (right_eye_y / image_height) - y_center
    nose_x = 0
    nose_y = 0
    left_mouth_x = (left_mouth_x / image_width) - x_center
    left_mouth_y = (left_mouth_y / image_height) - y_center
    right_mouth_x = (right_mouth_x / image_width) - x_center
    right_mouth_y = (right_mouth_y / image_height) - y_center

    # 返回转换后的坐标
    return f"0 {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f} {left_eye_x:.6f} {left_eye_y:.6f} {right_eye_x:.6f} {right_eye_y:.6f} {nose_x:.6f} {nose_y:.6f} {left_mouth_x:.6f} {left_mouth_y:.6f} {right_mouth_x:.6f} {right_mouth_y:.6f}\n"

input_folder = "E:/ProgrammingProjects/PythonProjects/DeepLearning/SWU-GKD-RMUC/_train/labels_coco"
output_folder = "E:/ProgrammingProjects/PythonProjects/DeepLearning/SWU-GKD-RMUC/_train/labels"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(input_folder):
    if file_name.endswith(".txt"):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, file_name)
        with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
            for line in input_file:
                # 将四点格式转换为五点格式
                converted_line = convert_four_points_to_five_points(line)
                # 写入转换后的行到输出文件中
                output_file.write(converted_line)
        

