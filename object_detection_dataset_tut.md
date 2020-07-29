# Introduction

This is a tutorial to make an object detection dataset from regular images with single/multiple objects. 

# Collecting data

The first step is to collect sufficient amount of data, ideally we would require the dataset to have equal proportions of each the classes that need to be identified. Collect the data and put all the data in one folder.

# Splitting the data

The next step would be to split the data into a train, test sets. We use an 90:10 split, hence 90% of our data is used for training and 10% test.
The git repo consists two scripts that will automate this, one a jupyter notebook and the other a python script which take as input folder names.

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
