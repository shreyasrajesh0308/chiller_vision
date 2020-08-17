# Introduction

This is a tutorial to make an object detection dataset from regular images with single/multiple objects. 

# Collecting data

1. The first step is to collect sufficient amount of data, ideally we would require the dataset to have equal proportions of each the classes that need to be identified.
2. It is also important that the dataset contains multiple combination of each of the objects, it need not be all possible permutations but a few combinations of each objects is necessary.
3. The dataset should represent all possible use cases, hence we need images that involved objects being obscured, images taken in low light etc.


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

For installation in an Ubuntu based system running **python3**.

```
pip install labelImag

```

1. Once installed run the software the GUI will open, point to the directory containing the train and valid datasets.

```
labelImg

```

2. Open the train dataset and open start with the first image.

3. Use the create *\nRectBox* to draw a tightly fit box around each object in the image. Enter the correct label name after drawing the box and click save. The GUI is shown below

**NOTE**: Bounding Box and labels have to be given for all the objects in the image

![labelImg](https://user-images.githubusercontent.com/41626118/89758823-5d4f8280-db06-11ea-8060-887e24908d05.png)


4. This will generate an xml file (with the same name as the corresponding image) for each of the bounding boxes 
5. Repeat the aforementioned process for each of the the images.
