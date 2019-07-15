import argparse
import torchvision
import torch
import torchvision.models as models
import torch.nn as nn


parser = argparse.ArgumentParser()
parser.add_argument("--n_epochs", type=int, default=200, help="number of epochs of training")
parser.add_argument("--batch_size", type=int, default=16, help="size of the batches")
parser.add_argument("--n_classes", type=int, default=5, help="number of classes for dataset")
parser.add_argument("--dataroot", type=str, default='./gotobun/', help="images")
parser.add_argument("--testroot", type=str, default='./dataset/', help="images")
opt = parser.parse_args()

img_data = torchvision.datasets.ImageFolder(opt.dataroot,transform=torchvision.transforms.Compose([torchvision.transforms.RandomResizedCrop(224),torchvision.transforms.RandomHorizontalFlip(),torchvision.transforms.ToTensor(),torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])]))

test_data = torchvision.datasets.ImageFolder(opt.testroot,transform=torchvision.transforms.Compose([torchvision.transforms.ToTensor(),torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])]))

data_loader = torch.utils.data.DataLoader(img_data, batch_size=opt.batch_size,shuffle=True)

test_loader = torch.utils.data.DataLoader(test_data, batch_size=17,shuffle=False)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

resnext = models.resnext50_32x4d(num_classes=opt.n_classes).to(device)

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(resnext.parameters())

for epoch in range(opt.n_epochs):
    print('[epoch:%d]'%(epoch + 1))
    running_loss = 0.0
    for i, (imgs, labels) in enumerate(data_loader):
        resnext=resnext.train()
        optimizer.zero_grad()
        
        outputs = resnext(imgs.to(device))
        loss = criterion(outputs, labels.to(device))
        loss.backward()
        optimizer.step()

        print(i, loss.item())
        resnext=resnext.eval()
        total = 0
        correct = 0
        test = resnext(imgs.to(device))
        _, predicted = torch.max(test.data, 1)
        total += labels.size(0)
        correct += (predicted == labels.to(device)).sum().item()
        print('Accuracy: %d %%' % (100 * correct / total))
        total = 0
        correct = 0

        '''running_loss += loss.item()
        if i % 8 == 7:    # print every 2000 mini-batches
            print('[epoch%d] loss: %.3f' %
                  (epoch + 1, running_loss / 8))
            running_loss = 0.0'''

    for j, (t_imgs, t_labels) in enumerate(test_loader):
        
        resnext=resnext.eval()
        t_total = 0
        t_correct = 0
        t_test = resnext(t_imgs.to(device))
        _, t_predicted = torch.max(t_test.data, 1)
        t_total += t_labels.size(0)
        t_correct += (t_predicted == t_labels.to(device)).sum().item()
        print('Test Accuracy: %d %%' % (100 * t_correct / t_total))
        t_total = 0
        t_correct = 0

    if epoch%10==9:
        torch.save(resnext.state_dict(),'./model-%s.pkl'%str(epoch+1))
        
    

print('Finished Training')

torch.save(resnext.state_dict(),'./model-last.pkl')






