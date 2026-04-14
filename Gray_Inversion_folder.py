import os#整个是python自带的操作系统，可以用来操作文件夹和目录
import cv2

# 输入文件夹
input_folder = "C:/Users/lenovo/Desktop/image_image/test_image"

# 输出文件夹
output_folder = "C:/Users/lenovo/Desktop/image_image/output_image"

# 如果输出文件夹不存在，就创建
#if not os.path.exists(output_folder):
    #os.makedirs(output_folder)

# 遍历输入文件夹里的所有文件
for filename in os.listdir(input_folder):#for....in是python的循环语句，意思是把列表里面的每一个东西挨个拿出来放进for后边的变量里面，然后执行后面的语句；os.listdir(input_folder)：列出这个文件夹里的所有文件名
    # 只处理常见图片格式
   # if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
        input_path = os.path.join(input_folder, filename)#这句一般跟在那个for之后的那行语句，用于将文件地址和文件夹地址拼起来形成一个完整的地址便于后续程序的操作

        # 读取图片
        img = cv2.imread(input_path)

        # 判断是否读取成功
        #if img is None:
            #print(f"无法读取图片: {filename}")
            #continue

        # 灰度化
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 灰度反转
        inverted_img = 255 - gray_img

        # 保存结果
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, inverted_img)

        #print(f"处理完成: {filename}")

print("全部图片处理完成！")
