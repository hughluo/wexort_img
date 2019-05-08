from PIL import Image
from math import sqrt
from sys import argv


def rect2square(image_path):

    img = Image.open(image_path)
    w, h = img.size
    img.crop

def square2circle(image_path):

    img = Image.open(image_path)
    if not img.size[0] == img.size[1]:
        raise SystemExit('Input Image is not square')
    else:
        img = img.convert("RGBA")
        pixels = img.load() # create the pixel map

        center_plot = int((img.size[0]) / 2)

        for i in range(img.size[0]):    # for every col:
            for j in range(img.size[1]):    # For every row
                distance = sqrt((i - center_plot) ** 2 + (j - center_plot) ** 2)
                if distance > center_plot:
                    pixels[i,j] = (255, 255, 255, 0) # set the colour accordingly

    # img.show()
    # out_path = image_path.split('.')[0] + '_out.png'
    out_path = 'output.png'
    img.save(out_path, "PNG")


def main():
    img_path = 'input.jpg'
    square2circle(img_path)


if __name__ == '__main__':
    main()