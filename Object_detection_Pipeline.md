# Pipeline for object detection.

A detailed tutorial can be found [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html)

## Collecting the data.

1. The first step is to collect sufficient data to be able to perform object detection.
2. There is no hard and fast rule that gives a measure of the volume of data required, the volume required varies largely with the number of classes
we have (no of different items). 
3. Since we have to perform multiple object detection, i.e. multiple objects in the same image we require images with multiple objects in them in different combinations. Recall that,
  1. Image Classification -  Predicting the category of a single image. Input - Single object image, Output - Classification of object.
  2. Object Detection - Predicting the label and bounding box for each object in an image(Containing multiple objects). Input - Image with single or multiple objects. Output - Bounding box for each object along with prediction for each object.
4. More on data preparation [here](https://github.com/shreyasrajesh0308/chiller_vision/blob/master/object_detection_dataset_tut.md)

## Processing the data.

The next step is to convert the raw image files we have into files that can be fed into the object detection model. This conversion comprises of the following steps,

1. Split the data into two folders train and test (Usual split precentage is about 90:10).
2. Draw bounding boxes for each of the images this is performed using [labelImg](https://github.com/tzutalin/labelImg), a graphic annotation tooling kit.
This has to be performed for each of the images in both folders, it will generate xml files for each of the images. This xml file contains the bounding box 
coordinates of each object in the  image along with labels. Shown below is an example input to the program and the final XML is the output generated by the labelling tool.

![Example Image](https://user-images.githubusercontent.com/41626118/89707071-b0033000-d988-11ea-9e9e-eb5deae53490.jpg)
![labelImg](https://user-images.githubusercontent.com/41626118/89754590-24111580-dafa-11ea-8970-70dc19430abb.png)
![Snapshot of xml corresponding file](https://user-images.githubusercontent.com/41626118/89707084-c7dab400-d988-11ea-8532-a168d80d74ba.png)

Shown below is a snapshot of how the train/test directory looks once it is run on all the images

![Directory_snapshot](https://user-images.githubusercontent.com/41626118/89708706-0bd4b580-d997-11ea-920d-575bed5e8641.png)


3. We then create a label_map which gives an id to each of the classes (types of objects) in our dataset, this is saved as a .pbtxt file. Our label map is shown below 

![label_map](https://user-images.githubusercontent.com/41626118/89707188-90b8d280-d989-11ea-84c2-5a14f3332f0d.png)

4. Once the xml records are generated for each image we have to convert this combination of image+xml into a format suitable to input to our model. A small 
script takes all the xml files and images in a folder and converts them into one .record file, this will be our input to the model. We run the script as shown below twice , once on each directory 

```python 

# Create train data:
python generate_tfrecord.py -x [PATH_TO_IMAGES_FOLDER]/train -l [PATH_TO_ANNOTATIONS_FOLDER]/label_map.pbtxt -o [PATH_TO_ANNOTATIONS_FOLDER]/train.record

# Create test data:
python generate_tfrecord.py -x [PATH_TO_IMAGES_FOLDER]/test -l [PATH_TO_ANNOTATIONS_FOLDER]/label_map.pbtxt -o [PATH_TO_ANNOTATIONS_FOLDER]/test.record

```



over the train directory and once on the test directory this gives us two .record files, train.record and test.record.

5. The train.record is used as the input to the model and the test.record file is used to evaluate the performance of our model.


## Training the model.

We use the [Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) provided by tensorflow to train a model.

1. Using the [Tensorflow model detection zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)  we have access 
to a number of extensively pre trained models (trained on the [COCO 2017 dataset](https://cocodataset.org/#home) ), for our purposes I have chosen SSD_mobilnet since it has good speed (since we require detection in **real time video**, we need to be able to detect objects fast while also maintaining reasonable accuracy ) with reasonable accuracy.
1. Each model comes with a configuration file, this helps us configure the training to our needs, mainly providing the model with the number of classes in our dataset 
and the label_map. Be sure to check the tutorial mentioned above to get this step perfectly right. The following are to be altered in the configuration file:
    1. num_classes : Set to number of classes in the dataset. (3 since we have 3 classes)
    1. label_map path : Path to label_map file (Enter absolute path to label map file)
    1. Location to checkpoint file for pretrained model. (Enter absolute path to checkpoint file for model) 
    1. Input train path : Path to input train record file (Enter absolute path to input train record file)
    1. Input test path : Path to input test record file (Enter absolute path to input test record file)
    
1. Once the configuration is set to our requirments, we train the model. We let the model learn until we see a saturation in the error percentage while being
careful not to [overfit](https://en.wikipedia.org/wiki/Overfitting).
1. Once the training is done we evaluate the model on our test dataset to see how well it generalizes to images it has not seen before.
1. We can then export the model and use it to detect object removal from the chiller.

## Results.

Following are a few of the outputs after using the trained model for prediction. The bounding box and the predictions are generated by the model.

**Note**:
The accuracies below are always close to 100% but this is not representative of how it generally works especially with multiple objects in the same image,
hence as complexity increases  the accuracy is also expected to drop off.


Detected as KFC burger with 100% certainity.

![34detected](https://user-images.githubusercontent.com/41626118/89707123-11c39a00-d989-11ea-88d9-3ea2049092d8.jpg)


Detected as KFC burger with 100% certainity.


![33detected](https://user-images.githubusercontent.com/41626118/89707124-12f4c700-d989-11ea-9dcc-ea37a4477efd.jpg)


Detected as KFC popcorn with 100% certainity.


![31detected](https://user-images.githubusercontent.com/41626118/89707125-138d5d80-d989-11ea-9db3-ff4285eb98d3.jpg)


Detected as Dominos burger with 100% certainity.



![14detected](https://user-images.githubusercontent.com/41626118/89707126-1425f400-d989-11ea-8203-72dd6274d2b0.jpg)



