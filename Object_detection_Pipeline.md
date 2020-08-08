# Pipeline for object detection.

A detailed tutorial can be found [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html)

## Collecting the data.

1. The first step is to collect sufficient data to be able to perform object detection.
2. There is no hard and fast rule that gives a measure of the amount of data required, the amount required varies largely with the number of classes
we have (no of different items). 
3. If we plan to do multiple object detection, i.e. multiple objects in the same image we require images with multiple objects in them in different combinations.
4. More on data preparation in the data_prep document.

## Processing the data.

The next step is to convert the raw image files we have into files that can be fed into the object detection model. This conversion comprises of the following steps,

1. Split the data into two folders train and test (Usual split precentage is about 9:1).
2. Draw bounding boxes for each of the images this is performed using [labelImg](https://github.com/tzutalin/labelImg), a graphic annotation tooling kit.
This has to be performed for each of the images in both folders, it will generate xml files for each of the images. This xml file contains the bounding box 
coordinates of each object in the  image along with labels. An example of an image and a snippet of the corresponding xml file are shown below.

![Example Image](https://user-images.githubusercontent.com/41626118/89707071-b0033000-d988-11ea-9e9e-eb5deae53490.jpg)
![Snapshot of xml corresponding file](https://user-images.githubusercontent.com/41626118/89707084-c7dab400-d988-11ea-8532-a168d80d74ba.png)

3. We then create a label_map which gives an id to each of the classes (types of objects) in our dataset. Our label map is shown below 

![label_map](https://user-images.githubusercontent.com/41626118/89707188-90b8d280-d989-11ea-84c2-5a14f3332f0d.png)

4. Once the xml records are generated for each image we have to convert this combination of image+xml into a format suitable to input to our model. A small 
script takes all the xml files and images in a folder and converts them into one .record file, this will be our input to the model. We run this script twice, once 
over the train directory and once on the test directory this gives us two .record files, train.record and test.record.
5. The train.record and test.record files are the input to our model.


## Traning the model.

We use the [Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) provided by tensorflow to train a model.

1. Using the [Tensorflow model detection zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)  we have access 
to a number of excessively pre trained models (trained on the [COCO 2017 dataset](https://cocodataset.org/#home) ), for our purposes I have chosen SSD_mobilnet since it has good speed (required for our use case) with decent accuracy.
2. Each model comes with a configuration file, this helps us configure the training to our needs, mainly providing the model with the number of classes in our dataset 
and the label_map.
3. Once the configuration is set to our requirments, we train the model. We let the model learn until we see a saturation in the error percentage while being
careful not to [overfit](https://en.wikipedia.org/wiki/Overfitting).
4. Once the training is done we evaluate the modelon our test dataset to see how well it generalizes to images it has not seen before.
5. We then export the trained model and use it on images.

## Results.

Following are a few of the outputs after using the trained model for prediction.

![34detected](https://user-images.githubusercontent.com/41626118/89707123-11c39a00-d989-11ea-88d9-3ea2049092d8.jpg)
![33detected](https://user-images.githubusercontent.com/41626118/89707124-12f4c700-d989-11ea-9dcc-ea37a4477efd.jpg)
![31detected](https://user-images.githubusercontent.com/41626118/89707125-138d5d80-d989-11ea-9db3-ff4285eb98d3.jpg)
![14detected](https://user-images.githubusercontent.com/41626118/89707126-1425f400-d989-11ea-8203-72dd6274d2b0.jpg)

