'''PIL中的Image模块'''
from array import array
from turtledemo.chaos import plot

from PIL import Image
import os
from io import StringIO


img_obj1 = Image.open('.\images\ex1.jpg')  # 返回Image对象
# print(type(img_obj))

'''旋转图像45度，并显示出来，但不会改变原来的图片'''
# img_obj1.rotate(45).show()

'''图像灰度化'''
# img_obj2 = Image.open('.\images\me.jpg').convert('L')
# img_obj2.show()


'''为了处理文件夹下所有图片在path路径下创建一个包含该文件夹中所有图像文件的文件名列表'''
# os.listdir()返回指定的文件夹包含的文件或文件夹的名字的列表
path = './images/'
def get_imglist(path):
    # return [f for f in os.listdir(path) if f.endswith('.jpg')]
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]  # 返回jpg格式的图片的地址
# print(get_imglist(path))

'''转换图像格式'''
# for infile in get_imglist(path):
#     # os.path.splitext():将文件名和扩展名分开
#
#     # 取得get_imglist()函数函数返回的图像路径，并拿掉图片的拓展名
#     # 然后将其变成jpg格式的图片
#     outfile = os.path.splitext(infile)[0] + '.jpg'
#     if infile != outfile:
#         try:
#             # open() 函数用于创建 PIL 图像对象，save() 方法用于保存图像到具有指定文件名的文件。
#             # 除了后缀变为“.jpg”，新文件名和原文件名相同
#             Image.open(infile).save(outfile)
#         except IOError:
#             print("failed", infile)

'''创建图片缩略图'''

# thumbnail() 方法接受一个元组参数（该参数指定生成缩略图的大小），然后将图像转换成符合元组参数指定大小的缩略图。
# for f in get_imglist(path):
#     img_obj1 = Image.open(f)
#     img_obj1.thumbnail((128, 128))
#     img_obj1.show()

'''赋值和粘贴图像区域'''
# 四元组的坐标依次是（左，上，右，下）。PIL 中指定坐标系的左上角坐标为（0，0）
coordinate = (200, 200, 600, 600)
# 剪切指定区域
region = img_obj1.crop(coordinate)  # 返回Image对象
# print(type(region))
# region.show()

'''旋转该区域'''
# region = region.transpose(Image.ROTATE_180)  # 旋转180度，返回Image对象
# img_obj1.paste(region, coordinate)  # 将旋转过的区域放回原来的位置
# region.show()

'''new()函数'''
# Image.new(mode, size) ⇒ image，默认是黑色
# im1 = Image.new("RGB", (512, 512))
# im1.show()
# Image.new(mode, size, color) ⇒ image
# im2 = Image.new("RGB", (512, 512), "white")
# im2.show()

'''open()函数'''
# Image.open(file) ⇒ image
# im3 = Image.open('.\images\ex2.jpg')
# Image.open(file, mode) ⇒ image，mode如果有，则必须是'r'
# im4 = Image.open('.\images\ex2.jpg', 'r')
# im4.show()

'''blend()函数'''
# 把一个图片插入到另一个图片，图片大小要相同，如果alpha为0，那么返回第一个图片，如果为1，返回第二个图片
# Image.blend(image1, image2, alpha) ⇒ image，其中alpha为透明度
image1 = Image.open('.\images\ex3.jpg')
image2 = Image.open('.\images\ex4.jpg')
# print(image1.size)
# im5 = Image.blend(image1, image2, 0.5)  # 返回图片对象
# print(type(out_image))
# out_image = '.\images\\blend.jpg'
# im5.save(out_image)

'''composite()函数
通道
一个图片可以包含一到多个数据通道，如果这些通道具有相同的维数和深度，Pil允许将这些通道进行叠加
模式 
1 1位像素，黑和白，存成8位的像素 
L 8位像素，黑白 
P 8位像素，使用调色板映射到任何其他模式 
RGB 3×8位像素，真彩 
RGBA 4×8位像素，真彩+透明通道 
CMYK 4×8位像素，颜色隔离 
YCbCr 3×8位像素，彩色视频格式 
I 32位整型像素 
F 32位浮点型像素

'''
# 使用两幅给出的图片和一个与 alpha 参数相似用法的 mask 参数，其值可为："1", "L", "RGBA" 。两幅图片的 size 必须相同
# Image.composite(image1, image2, mask) ⇒ image
# mask = Image.open('.\images\l.bmp')
# im6 = Image.composite(image1, image2, mask)
# out_image = '.\images\\blend.jpg'  # 因为有个\b
# im6.save(out_image)





