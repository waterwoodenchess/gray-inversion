import cv2

#由于是对彩色的图像进行灰度反转，所以需要先将彩色图像转换为灰度图像
#读取彩色图
img=cv2.imread("C:/Users/lenovo/Desktop/image/image_image/test_image/image1.jpg")

#对彩色的图片进行灰度化操作，首先生成新图
gray_image1=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#COLOR_BGR2GRAY可以将彩色的图片转为灰度图

#保存已经灰度化好了的图片
cv2.imwrite("C:/Users/lenovo/Desktop/image/image_image/output_image/gray_image1.jpg", gray_image1)

#对灰度图片进行翻转，生成另外一张新图片，公式是255-c
gray_image2=255-gray_image1

#保存已经翻转好了的图片
cv2.imwrite("C:/Users/lenovo/Desktop/image/image_image/output_image/gray_image2.jpg", gray_image2)

#由于原图片太大所以对图片进行缩小再显示
img=cv2.resize(img, (0, 0), fx=0.2, fy=0.2)#cv2.revise是对图片大小进行缩放的，(0, 0)表示不指定输出图像的大小，而是通过缩放因子fx和fy来计算输出图像的大小。fx=0.5表示将宽度缩小为原来的一半，fy=0.5表示将高度缩小为原来的一半。
gray_image1=cv2.resize(gray_image1, (0, 0), fx=0.2, fy=0.2)
gray_image2=cv2.resize(gray_image2, (0, 0), fx=0.2, fy=0.2)

#显示图片，所有的
cv2.imshow("img", img)
cv2.imshow("gray_image1", gray_image1)
cv2.imshow("gray_image2", gray_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()