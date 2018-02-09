from PIL import Image


def rotate(l, n):
    return l[n:] + l[:n]


if __name__ == "__main__":
    with open('rainbow_pallette.txt', 'r') as o:
        rainbow_pallette = o.readline().strip().split(',')
    rainbow_pallette = map(int, rainbow_pallette)
    im = Image.open("corgi.gif")
    gif_frames = []
    N = 8
    for i in range(N):
        im.putpalette(rainbow_pallette)
        gif_frames.append(im)
        rotate(rainbow_pallette, 3*N)

    im.save('corgi_new.gif', save_all=True, append_images=gif_frames)
