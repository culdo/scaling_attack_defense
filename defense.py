import cv2
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.widgets import Button

matplotlib.rc('font', **{'sans-serif': 'Arial',
                         'family': 'sans-serif'})


class AttackDefense:
    def __init__(self, img, fig=None):
        self.load_img(img)
        if fig:
            self.figure = fig
        else:
            self.figure = plt.figure("縮放攻擊防禦Demo by Jun Hu", figsize=(20, 4))
        self.init_plot()

    def load_img(self, img):
        img = cv2.imread(img)
        self.img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

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

    def add_plot(self, coord, title=None):
        if isinstance(coord, tuple):
            sp = self.figure.add_subplot(*coord)
        else:
            sp = self.figure.add_subplot(coord)
        if title:
            sp.set_title(title)
        sp.set_xticks([])
        sp.set_yticks([])
        return sp

    def init_plot(self):
        self.img_sp = self.add_plot(251, "Original")
        self.img_sp.set_ylabel("Input", rotation="horizontal", size=12, labelpad=15)
        self.avg_blur_sp = self.add_plot(252, 'Avg Blurred')
        self.gau_blur_sp = self.add_plot(253, 'Gaussian Blurred')
        self.median_blur_sp = self.add_plot(254, 'Median Blurred')
        self.bilate_blur_sp = self.add_plot(255, 'Bilateral Blurred')
        self.img_output_sp = self.add_plot(256)
        self.img_output_sp.set_ylabel("Scaled", rotation="horizontal", size=12, labelpad=60)
        self.avg_output_sp = self.add_plot(257)
        self.gau_output_sp = self.add_plot(258)
        self.median_output_sp = self.add_plot(259)
        self.bilate_output_sp = self.add_plot((2, 5, 10))
        self.figure.tight_layout()

    def plot(self):
        self.img_sp.imshow(self.img)
        self.avg_blur_sp.imshow(self.avg_blur)
        self.gau_blur_sp.imshow(self.gau_blur)
        self.median_blur_sp.imshow(self.median_blur)
        self.bilate_blur_sp.imshow(self.bilate_blur)
        self.img_output_sp.imshow(self.org_output)
        self.avg_output_sp.imshow(self.avg_output)
        self.gau_output_sp.imshow(self.gau_output)
        self.median_output_sp.imshow(self.median_output)
        self.bilate_output_sp.imshow(self.bilate_output)

    def run(self, size):
        self.filter_img()
        self.resize(size)
        self.plot()


if __name__ == '__main__':
    demo = AttackDefense('../scaling_camouflage/gene_to_802_l2.png')
    demo.run((258, 258))
    plt.show()
