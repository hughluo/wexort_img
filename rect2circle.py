from PIL import Image
from math import sqrt
from sys import argv


def rect2square(img):

    w, h = img.size
    if w > h:
        padding = (w - h) / 2
        cropped_img = img.crop((padding, 0, padding + h, h))
    else:
        padding = (h - w) / 2
        cropped_img = img.crop((0, padding, w, padding + w))

    return cropped_img


def square2circle(img):

    if not img.size[0] == img.size[1]:
        raise SystemExit('Input Image is not square')
    else:
        img = img.convert("RGBA")
        pixels = img.load() # create the pixel map

        center_plot = int((img.size[0]) / 2)

        for i in range(img.size[0]):    # for every col:
            for j in range(img.size[1]):    # for every row
                distance = sqrt((i - center_plot) ** 2 + (j - center_plot) ** 2)
                if distance > center_plot:
                    pixels[i,j] = (255, 255, 255, 0) # set the colour accordingly

    # img.show()
    # out_path = image_path.split('.')[0] + '_out.png'
    return img


def rect2circle(img):

    return square2circle(rect2square(img))


def main():
    try:
        in_img = Image.open('input.png')
    except FileNotFoundError:
        try:
            in_img = Image.open('input.jpg')
        except FileNotFoundError:
            raise SystemExit('No file named input.png or input.jpg')

    out_path = 'output.png'
    # in_img = Image.open(in_path)
    out_img = rect2circle(in_img)
    # out_img.show()
    out_img.save(out_path, "PNG")


if __name__ == '__main__':
    main()
