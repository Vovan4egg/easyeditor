#создай тут фоторедактор Easy Editor!
import os #модуль для работы с операционной системой
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog, #Диалог открытия файлов (и папок) 
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
) #подключаем нужные модули

from PyQt5.QtCore import Qt #нужна константа Qt.KeepAspectRaеio для изменения размеров с сохранением пропорций
from PyQt5.QtGui import QPixmap #оптимизированная для показа на экране картинка

from PIL import Image #модуль для получения формата картинки, размеров и модов
from PIL.ImageQt import ImageQt #для перевода графики из Pillow в Qt
from PIL import ImageFilter
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
    GaussianBlur, UnsharpMask
)

app = QApplication([]) #создаём приложение
win = QWidget() #создаём окно приложения
win.resize(700, 500) #устанавливаем размер окну
win.setWindowTitle('Easy Editor') #даём окну название
lb_image = QLabel('Картинка') #создаём текст Картинка
btn_dir = QPushButton('Папка') #создаём кнопку Папка
lw_files = QListWidget() #создаём список

btn_left = QPushButton('Лево') #создаём кнопку Лево
btn_right = QPushButton('Право') #создаём кнопку Право
btn_flip = QPushButton('Зеркало') #создаём кнопку Зеркало
btn_sharp = QPushButton('Резкость') #создаём кнопку Резкость
btn_bw = QPushButton('Ч/Б') #создаём кнопку Ч/Б
btn_test = QPushButton('Contour') #создаём кнопку Contour
btn_blur = QPushButton('Blur') #создаём кнопку Blur
btn_smooth = QPushButton('Smooth') #создаём кнопку Smooth 
btn_emboss = QPushButton('Emboss') #создаём кнопку Emboss
btn_detail = QPushButton('Detail') #создаём кнопку Detail
btn_findEdges = QPushButton('Find Edges') #создаём кнопку Find Edges

row = QHBoxLayout() #основная линия
col1 = QVBoxLayout() #делится на два столба
col2 = QVBoxLayout() 
col1.addWidget(btn_dir) #в первом - кнопка выбора директории
col1.addWidget(lw_files) #и список файлов
col2.addWidget(lb_image, 95) #во втором - картинка
row_tools = QHBoxLayout() #и строка кнопок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_test)
row_tools.addWidget(btn_blur)
row_tools.addWidget(btn_smooth)
row_tools.addWidget(btn_emboss)
row_tools.addWidget(btn_detail)
row_tools.addWidget(btn_findEdges)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

win.show()

workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkdir(): #выбрать директорию папки
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList(): #функция показа названий файлов
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)

    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)

class ImageProcessor():
    def __init__(self): #функция конструктор
        self.image = None #файл
        self.dir = None #путь к папке
        self.filename = None #имя файла
        self.save_dir = "Modfied/" #папка для сохранения обработаных фото

    def loadImage(self, dir, filename):
        '''при загрузке запоминаем путь и имя файла'''
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename) #склеивает путь к папке с именем
        self.image = Image.open(image_path) #открываем фото

    def do_bw(self):
        self.image = self.image.convert("L") #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении
    
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90) #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении
    
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270) #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении
    
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT) #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении

    def do_sharpen(self):
        self.image = self.image.filter(SHARPEN) #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении
    
    def do_1(self):
        self.image = self.image.filter(CONTOUR) #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении
    
    def do_blur(self):
        self.image = self.image.filter(BLUR) #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении
    
    def do_smooth(self):
        self.image = self.image.filter(SMOOTH) #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении

    def do_emboss(self):
        self.image = self.image.filter(EMBOSS) #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении
    
    def do_detail(self):
        self.image = self.image.filter(DETAIL) #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении

    def do_findEdges(self):
        self.image = self.image.filter(FIND_EDGES) #метод обработки из PIL
        self.saveImage() #сохраняет обработанное фото
        image_path = os.path.join(self.dir, self.save_dir, self.filename)#склеивает путь к папке с именем
        self.showImage(image_path) #показываем фото в приложении

    def saveImage(self): #функция сохранения картинки
        '''сохраняет копию файла в подпалке'''
        path = os.path.join(self.dir, self.save_dir) #склеивает путь к папке с именем
        if not(os.path.exists(path) or os.path.isdir(path)): #exists и isdir проверяют нет ли папки с названием Modfied
            os.mkdir(path) 
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    
    def showImage(self, path): #функция показа картинки
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

def showChosenImage(): #функция показа выбранной картинки
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

workimage = ImageProcessor() #текущая рабочая картинка для работы
lw_files.currentRowChanged.connect(showChosenImage)

btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharpen)
btn_flip.clicked.connect(workimage.do_flip)
btn_test.clicked.connect(workimage.do_1)
btn_blur.clicked.connect(workimage.do_blur)
btn_smooth.clicked.connect(workimage.do_smooth)
btn_emboss.clicked.connect(workimage.do_emboss)
btn_detail.clicked.connect(workimage.do_detail)
btn_findEdges.clicked.connect(workimage.do_findEdges)

app.exec()