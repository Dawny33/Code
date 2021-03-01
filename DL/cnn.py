import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
import pandas as pd

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
    

train, test = download(path_data)
explore(train, test)


