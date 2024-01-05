
from distutils import extension
from importlib.metadata import files
from tkinter import Image
from tkinter import video
from turtle import width
from turtle import height
import cv2
import os
from grpc import Channel
from cv2 import Project


path = "Images/"

Images = []
frame = []
count = len(Images)

os.listdir(path)
os.splitext(files)

if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
    file_name = path+"/"+files

    print(file_name)

Image.append()

frame = cv2.imread(Images[0])
frame.shape(width,height,Channel)
size = (width, height)
print(size)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    cv2.imread()
    out.write()

    print("Done")
