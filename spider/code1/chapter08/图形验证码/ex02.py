import tesserocr
from PIL import Image


def main():
    image = Image.open('./CheckCode2.jpg')
    # result = tesserocr.image_to_text(image)
    # print(result)  # 5P9].

    """
    显然上面的输出是有误的
    """
    # 方法二 - 转灰度，二值化等
    # image = image.convert('L')  # 转灰度
    # image = image.convert('1')  # 二值化
    # image.show()

    # 方法三 - 指定二值化的阈值
    image = image.convert('L')
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    image.show()
    result = tesserocr.image_to_text(image)
    print(result)


if __name__ == '__main__':
    main()
