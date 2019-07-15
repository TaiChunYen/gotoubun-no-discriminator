# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:29:19 2019

@author: taita
"""

import torch
import torchvision.models as models
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from torch.autograd import Variable
import sys
import os
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QPushButton, QFileDialog
from myui import Ui_Form
class MyDlg(QDialog):
    def __init__(self):
        super(MyDlg, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.cwd = os.getcwd()
        
        with open(self.cwd + "/" + 'gotoubun_title.png', 'rb') as f:
            ttimg = f.read()
        ttimage = QImage.fromData(ttimg)
        ttpixmap = QPixmap.fromImage(ttimage)
        self.ui.label_3.clear
        ttpixmap=ttpixmap.scaled(self.ui.label_3.width(),self.ui.label_3.height(),QtCore.Qt.KeepAspectRatio)
        
        self.ui.label_3.setPixmap(ttpixmap)
        
        self.ui.pushButton.clicked.connect(lambda:show_pic(self))        
        self.img_dir = ""
        self.ui.pushButton_2.clicked.connect(lambda:show_result(self))
        self.ui.radioButton.isChecked
def main_start():
    app = QApplication(sys.argv)
    window = MyDlg()
    window.show()
    sys.exit(app.exec_())
    
def show_pic(self):
    fileName, filetype = QFileDialog.getOpenFileName(self,"choice file",self.cwd,"Image Files (*.jpg;*.jpeg;*.png)")  
    if fileName != "":
        dirction = fileName
        self.img_dir = dirction                                
        with open(dirction, 'rb') as f:
            img = f.read()
        image = QImage.fromData(img)
        pixmap = QPixmap.fromImage(image)
        self.ui.label.clear
        pixmap=pixmap.scaled(self.ui.label.width(),self.ui.label.height(),QtCore.Qt.KeepAspectRatio)
        
        self.ui.label.setPixmap(pixmap)
        
    
def show_result(self):
    if self.img_dir != "":
        if self.ui.lineEdit.text != "":            
            
            model_dir = self.cwd + "/" + self.ui.lineEdit.text()
            #print(model_dir)
            if self.ui.radioButton.isChecked():
                model = models.alexnet(num_classes=5).cuda()
                model.load_state_dict(torch.load(model_dir))
                model.eval()
            
            elif self.ui.radioButton_2.isChecked():
                model = models.resnext50_32x4d(num_classes=5).cuda()
                model.load_state_dict(torch.load(model_dir))
                model.eval()

            imsize = 224
            loader = transforms.Compose([transforms.Resize(imsize),transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])])

            def image_loader(image_name):
                """load image, returns cuda tensor"""
                image = Image.open(image_name)
                image = loader(image).float()
                image = Variable(image, requires_grad=True)
                image = image.unsqueeze(0)  #this is for VGG, may not be needed for ResNet
                return image.cuda()  #assumes that you're using GPU

            image = image_loader(self.img_dir)

            classes = ('1', '2', '3', '4','5')


            out = model(image)
            _, predicted = torch.max(out.data, 1)
            
    
            if classes[predicted]=='1':
                with open(self.cwd + "/" + 'ichiha.jpg', 'rb') as f:
                    img = f.read()
                    image = QImage.fromData(img)
                    pixmap = QPixmap.fromImage(image)
                    self.ui.label_2.clear
                    pixmap=pixmap.scaled(self.ui.label_2.width(),self.ui.label_2.height(),aspectRatioMode=QtCore.Qt.KeepAspectRatio)
                    self.ui.label_2.setPixmap(pixmap)
        
            elif classes[predicted]=='2':
                with open(self.cwd + "/" + 'nino.jpg', 'rb') as f:
                    img = f.read()
                    image = QImage.fromData(img)
                    pixmap = QPixmap.fromImage(image)
                    self.ui.label_2.clear
                    pixmap=pixmap.scaled(self.ui.label_2.width(),self.ui.label_2.height(),aspectRatioMode=QtCore.Qt.KeepAspectRatio)
                    self.ui.label_2.setPixmap(pixmap)
        
            elif classes[predicted]=='3':
                with open(self.cwd + "/" + 'miku.jpg', 'rb') as f:                   
                    img = f.read()
                    image = QImage.fromData(img)
                    pixmap = QPixmap.fromImage(image)
                    self.ui.label_2.clear
                    pixmap=pixmap.scaled(self.ui.label_2.width(),self.ui.label_2.height(),aspectRatioMode=QtCore.Qt.KeepAspectRatio)
                    self.ui.label_2.setPixmap(pixmap)
        
            elif classes[predicted]=='4':
                with open(self.cwd + "/" + 'yotsuba.jpg', 'rb') as f:
                    img = f.read()
                    image = QImage.fromData(img)
                    pixmap = QPixmap.fromImage(image)
                    self.ui.label_2.clear
                    pixmap=pixmap.scaled(self.ui.label_2.width(),self.ui.label_2.height(),aspectRatioMode=QtCore.Qt.KeepAspectRatio)
                    self.ui.label_2.setPixmap(pixmap)
        
            elif classes[predicted]=='5':
                with open(self.cwd + "/" + 'itsuki.jpg', 'rb') as f:
                    img = f.read()
                    image = QImage.fromData(img)
                    pixmap = QPixmap.fromImage(image)
                    self.ui.label_2.clear
                    pixmap=pixmap.scaled(self.ui.label_2.width(),self.ui.label_2.height(),aspectRatioMode=QtCore.Qt.KeepAspectRatio)
                    self.ui.label_2.setPixmap(pixmap)

    


if __name__ == '__main__':
    main_start()