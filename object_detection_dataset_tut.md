# Introduction

This is a tutorial to make an object detection dataset from regular images with single/multiple objects. 

# Collecting data

The first step is to collect sufficient amount of data, ideally we would require the dataset to have equal proportions of each the classes that need to be identified. It is also important that the dataset contains multiple combination of each of the objects, it need not be all possible permutations but a few combinations of each objects is necessary.

Say there are n distinct objects in the dataset then we would require an equal number of images in each subset i.e n-1, n-2...1.

A few sample images are shown below.

![IMG-20200729-WA0005](https://user-images.githubusercontent.com/41626118/88930098-a39c1a80-d298-11ea-8b9f-1f5208d979fb.jpg)
![IMG-20200729-WA0013](https://user-images.githubusercontent.com/41626118/88930117-aa2a9200-d298-11ea-909f-b3265af6a7e6.jpg)
![IMG-20200729-WA0004](https://user-images.githubusercontent.com/41626118/88930132-aeef4600-d298-11ea-8eab-6f738dadf454.jpg)
![IMG-20200729-WA0010](https://user-images.githubusercontent.com/41626118/88930139-b282cd00-d298-11ea-9595-5180291267f0.jpg)





# Splitting the data

The next step would be to split the data into a train, test sets. We use an 90:10 split, hence 90% of our data is used for training and 10% test.
The git repo contains a python script that will automate this.

The scipt takes two inputs

1. Input path to folder containing all images.
2. Input path to folder that will contain the train and test folders.

One can use the script if a test set needs to be created.


# Bounding box

For this we use the [labelImg](https://github.com/tzutalin/labelImg) package. 

For installation in an Ubuntu based system

```
pip install labelImag

```

Once installed run the software the GUI will open, point to the directory containing the train and valid datasets.

Open the train dataset and open start with the first image.

Click on the PascalVOC button to change to YOLO format.

Use the create \nReactBox to draw a tightly fit box around each object. Enter the correct label name after drawing the box and click save.

This will each of the bounding boxes as xml files with the same name as the corresponding image.

Repeat the process for all the images.
