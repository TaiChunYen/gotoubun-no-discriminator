import argparse
import torchvision
import torch
import torchvision.models as models
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from torch.autograd import Variable

parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, default='./a_model-last.pkl', help="model")
parser.add_argument("--n_classes", type=int, default=5, help="number of classes for dataset")
parser.add_argument("--root", type=str, default='./test.jpg', help="images")
opt = parser.parse_args()

alexnet = models.alexnet(num_classes=opt.n_classes).cuda()
alexnet.load_state_dict(torch.load(opt.model))
alexnet.eval()

imsize = 224
loader = transforms.Compose([transforms.Resize(imsize),transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])])

def image_loader(image_name):
    """load image, returns cuda tensor"""
    image = Image.open(image_name)
    image = loader(image).float()
    image = Variable(image, requires_grad=True)
    image = image.unsqueeze(0)  #this is for VGG, may not be needed for ResNet
    return image.cuda()  #assumes that you're using GPU

image = image_loader(opt.root)

classes = ('1', '2', '3', '4','5')

out = alexnet(image)
_, predicted = torch.max(out.data, 1)

print(classes[predicted])
