import tesserocr
from PIL import Image


def main():
    image = Image.open('./CheckCode.jpg')
    result = tesserocr.image_to_text(image)
    print(result)  # LYGT
    # print(tesserocr.file_to_text('./CheckCode.jpg'))


if __name__ == '__main__':
    main()
