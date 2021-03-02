import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt 

path_data = './data/'


def download(path):
    """Getting the data (CIFAR10)

    Args:
        path ([str]): Path for downloading the data to
    """
    train = torchvision.datasets.CIFAR10(root=path_data, train=True, download=False)
    test = torchvision.datasets.CIFAR10(root=path_data, train=False, download=False)
    return train, test

def explore(train, test):
    """Exploring the loaded train and test sets

    Args:
        train ([torchvision.datasets.cifar.CIFAR10]): Train split of CIFAR10 dataset
        test ([torchvision.datasets.cifar.CIFAR10]): Test split of CIFAR10 dataset
    """
    print("classes in the dataset: ", train.classes)
    # print("idx of the classes: ", train.targets)
    print("class-to-idx map: ", train.class_to_idx)
    # print("Training data as an ndarray: ", train.data)
    # print("See all the properties of data: ", train.__dict__)
    
def transform(data):
    """Apply transforms on dataset

    Args:
        data : Dataset
    """
    cifar_transform = transforms.Compose([
        transforms.ToTensor(),  # converts ndarray to tensor format
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # Normalization
        # Ref: https://discuss.pytorch.org/t/understanding-transform-normalize/21730/2
    ])

    data.transform = cifar_transform
    data.transforms = torchvision.datasets.vision.StandardTransform(cifar_transform)


train, test = download(path_data)
#explore(train, test)
transform(train)
transform(test)
# The data (train.data) shall remain unscaled  even after the above line
# The transforms shall be applied only with the DataLoader
trainLoader = torch.utils.data.DataLoader(train, batch_size=4, shuffle=True)
testLoader = torch.utils.data.DataLoader(test, batch_size=4, shuffle=False)

# Trying to convert trainLoader to an iterater for east exploration
train_iter = iter(trainLoader)
images, labels = train_iter.next()
# Confirming if the scaling happened, by looking at the tensor
# print(images[0])
# Looking at the size of the tensor:
# print(images.size())  # torch.Size([4, 3, 32, 32]) <- Batch Size = 4
# ^ The remaining 3, 32, 32 is because the original data has shape (50000, 32, 32, 3)


import torch.nn as nn
import torch.nn.functional as F

# Input to a nn.Conv2d should be of shape (nSamples x nChannels x Height x Width)
# nn.Linear(in_features, out_features)
#  in_features => neurons coming into the layer, out_features => neurons going out of the later
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # nn.Conv2d(in_channels, out_channels, kernel_size)
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        # in_channel below is 6 cause the out_channel for conv1 is 6
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 5*5 below comes from the dimension of conv2
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        # -1 means that the first axis has to be inferred depending on x
        # The other axis is 16*16*5
        x = x.view(-1, 16*5*5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        # No activation function for final layer
        x = self.fc3(x)
        return x

net = Net()


import torch.optim as optim
criterion = nn.CrossEntropyLoss()
# lr => learning rate
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# Training the model on the data
running_loss = 0
printfreq = 1000
# Mention the number of epochs inside the range
for epoch in range(0):
    for i, data in enumerate(trainLoader):
        inputs, labels = data
        # Resetting the gradient after each epoch
        optimizer.zero_grad()
        outputs = net(inputs)  # forward pass
        loss = criterion(outputs, labels)
        loss.backward()  # backprop
        optimizer.step()  # update the weights
        running_loss += loss.item()
        if i % printfreq == printfreq-1:
            print(epoch, i+1, running_loss / printfreq)
            running_loss = 0

# Saving the model
"""
for param_tensor in net.state_dict():
    print(param_tensor, "\t", net.state_dict()[param_tensor].size())

print(optimizer.state_dict().keys())
print(optimizer.state_dict()['param_groups'])
"""
fname = './models/CIFAR10_cnn.path'
torch.save(net.state_dict(), fname)
loaded_dict = torch.load(fname)
net.load_state_dict(loaded_dict)

# print(net.eval())  # Check loaded model


