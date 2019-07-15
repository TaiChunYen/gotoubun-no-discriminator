# 五等分辨識器
![image](https://github.com/TaiChunYen/gotoubun-no-discriminator/blob/master/readme_p/gotoubun-no-hanayome2.png)
## 動機
![image](https://github.com/TaiChunYen/gotoubun-no-discriminator/blob/master/readme_p/gotobun_re.png)
## file overview
train.py [parameter]  
parameter list:  
--n_epochs  
--batch_size  
--n_classes  
--dataroot  
--testroot  

test.py [parameter]  
parameter list:  
--model(trained model dir)  
--n_classes  
--root(test_img dir)  

(if vram out of memory use train_alex.py & test_alex.py or train_on_colab.ipynb)  

gotobun_qt/PyGui.py(run the GUI)  

gotobun_qt/myui.py(GUI sturcture)  

dataset/(training data)  

gotoubun/(testing data)  


## 訓練模型
resnext50_32x4d  
AlexNet  

## 訓練過程
accuracy(resnext50_32x4d):  
![image](https://github.com/TaiChunYen/gotoubun-no-discriminator/blob/master/readme_p/train_acc.png)

loss(resnext50_32x4d):  
![image](https://github.com/TaiChunYen/gotoubun-no-discriminator/blob/master/readme_p/train_loss.png)

## GUI(pyqt5)
![image](https://github.com/TaiChunYen/gotoubun-no-discriminator/blob/master/readme_p/gui.png)

## 結果
python3.6 ./gotobun_qt/PyGui.py  

![image](https://github.com/TaiChunYen/gotoubun-no-discriminator/blob/master/readme_p/r1.png)
![image](https://github.com/TaiChunYen/gotoubun-no-discriminator/blob/master/readme_p/r2.png)
![image](https://github.com/TaiChunYen/gotoubun-no-discriminator/blob/master/readme_p/r3.png)
![image](https://github.com/TaiChunYen/gotoubun-no-discriminator/blob/master/readme_p/r4.png)
![image](https://github.com/TaiChunYen/gotoubun-no-discriminator/blob/master/readme_p/r5.png)


## 誌謝
感謝凶宸提供data來源！
