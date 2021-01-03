import cv2
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.widgets import Button

matplotlib.rc('font', **{'sans-serif': 'Arial',
                         'family': 'sans-serif'})


class AttackDefense:
    def __init__(self, img):
        self.img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.figure = plt.figure("縮放攻擊防禦Demo by Jun Hu", figsize=(20, 4))

    def select_img(self):
        pass

    def filter_img(self):
        self.avg_blur = cv2.blur(self.img, (5, 5))
        self.gau_blur = cv2.GaussianBlur(self.img, (5, 5), 0)
        self.median_blur = cv2.medianBlur(self.img, 5)
        self.bilate_blur = cv2.bilateralFilter(self.img, 9, 75, 75)

    def resize(self, dst_size):
        self.org_output = cv2.resize(self.img, dst_size)
        self.avg_output = cv2.resize(self.avg_blur, dst_size)
        self.gau_output = cv2.resize(self.gau_blur, dst_size)
        self.median_output = cv2.resize(self.median_blur, dst_size)
        self.bilate_output = cv2.resize(self.bilate_blur, dst_size)

    def add_img(self, coord, img, title=None):
        if isinstance(coord, tuple):
            sp = self.figure.add_subplot(*coord)
        else:
            sp = self.figure.add_subplot(coord)
        sp.imshow(img)
        if title:
            sp.set_title(title)
        sp.set_xticks([])
        sp.set_yticks([])
        return sp

    def plot(self):
        sp = self.add_img(251, self.img, "Original")
        sp.set_ylabel("Input", rotation="horizontal", size=12, labelpad=15)
        self.add_img(252, self.avg_blur, 'Avg Blurred')
        self.add_img(253, self.gau_blur, 'Gaussian Blurred')
        self.add_img(254, self.median_blur, 'Median Blurred')
        self.add_img(255, self.bilate_blur, 'Bilateral Blurred')
        sp = self.add_img(256, self.org_output)
        sp.set_ylabel("Scaled", rotation="horizontal", size=12, labelpad=60)
        self.add_img(257, self.avg_output)
        self.add_img(258, self.gau_output)
        self.add_img(259, self.median_output)
        self.add_img((2, 5, 10), self.img)
        self.figure.tight_layout()


if __name__ == '__main__':
    img = cv2.imread('../scaling_camouflage/gene_to_802_l2.png')
    demo = AttackDefense(img)
    demo.filter_img()
    demo.resize((258, 258))
    demo.plot()
    plt.show()
