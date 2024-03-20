import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

#KONCEPT
class ImageAnnotationApp:
    def __init__(self, image_path):
        self.image = plt.imread(image_path)
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.image)
        self.annotations = []

        self.rect = None
        self.start_point = None

        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)

    def on_press(self, event):
        if event.button == 1:
            self.start_point = (event.xdata, event.ydata)
            self.rect = Rectangle((event.xdata, event.ydata), 1, 1, linewidth=1, edgecolor='r', facecolor='none')
            self.ax.add_patch(self.rect)
            self.fig.canvas.draw()

    def on_release(self, event):
        if event.button == 1:
            end_point = (event.xdata, event.ydata)
            width = end_point[0] - self.start_point[0]
            height = end_point[1] - self.start_point[1]
            self.rect.set_width(width)
            self.rect.set_height(height)
            self.annotations.append((self.start_point, (width, height)))
            self.fig.canvas.draw()

    def show_annotations(self):
        print("Annotations:")
        for i, ann in enumerate(self.annotations):
            print(f"Annotation {i+1}: Start Point: {ann[0]}, Width: {ann[1][0]}, Height: {ann[1][1]}")

        plt.show()

# Ścieżka do obrazu
image_path = 'image.jpg'

# Uruchomienie aplikacji
app = ImageAnnotationApp(image_path)
app.show_annotations()
