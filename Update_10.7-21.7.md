# Update from 10/7 to 21/7

1. This is an update after the initial update provided where we showed how the neural network works with toy data and initial NUTY dataset.

2. The model we have can be extended to perform object recognition of various classes but it is limited in the sense that it can only perform single image classification. That is given an image with one image the model will be able to recognize the object.
That is  an object like 

![Single_label](https://user-images.githubusercontent.com/41626118/88027689-3fb97980-cb55-11ea-9cda-177eda69b966.png)

can be identified. 

3. The effectiveness of the neural network has to be tested against a dataset that is not shown to the network while training. The data given to us by NUTY was split into train and validation, the train set is used to train the neural network while the performance of the network is measured against the validation set while training, this helps tune parameters to improve performance. Once the network has been trained completely it is tested against a dataset that is not part of the train or validation set. This is called the test dataset. We hence require a test dataset to evaluate the performance of our neural network.

An article on the difference between the different types of datasets can be found [here](https://towardsdatascience.com/train-validation-and-test-sets-72cb40cba9e7). 

4. If classification has to be done using a camera inside the chiller , we have two cases of what has to be done.

	1. We have a single object that has to be recognized, this is possible with our current model.
	
	2. If multiple objects have to be identified, our present model is not sufficient. In this case we'd have to perform [object detection](https://en.wikipedia.org/wiki/Object_detection) which would require a dataset that has, around each of the objects in an image, a rectangular box called the bounding box that encapsulates the entire object. For example,
	
	![INPUT_IMG_BB](https://user-images.githubusercontent.com/41626118/88045541-50291e80-cb6c-11ea-98e7-2fcc37e1c4aa.png)

	
## Difference between Image Classification and Object Detection.

**Image Classification** - Predicting the category of a single image. Input - Single object image, Output - Classification of object.

**Input**

![Classification](https://user-images.githubusercontent.com/41626118/88037339-603c0080-cb62-11ea-9d14-73cb20daeaf3.png)

**Output**

Dog

**Object Detection** - Predicting the label and bounding box for each object in an image(Containing multiple objects). Input - Image with single or multiple objects. Output - Bounding box for each object along with prediction for each object.

**Input**

![WITHOUT BB](https://user-images.githubusercontent.com/41626118/88043221-caf13a00-cb6a-11ea-937d-f2d7f9583d3d.png)

**Ouput**

![WITH BB](https://user-images.githubusercontent.com/41626118/88043139-ad23d500-cb6a-11ea-9cf4-3dd38c412d39.png)

		
5. Generating this dataset is not an easy task but unfortunately there is no way around it. For this we have an open source software called [labelImg](https://github.com/tzutalin/labelImg#installation) which makes it easy to draw a bounding box for each of our images, but we have to go through the painstaking process of drawing a bounding box for each of the images. 
	
6.  A [paper](https://arxiv.org/pdf/1904.09781.pdf) by Yi et al. discuss a possible use case where the generate bounding boxes for the images while classification but train without any such requirments. While we could try and work on implementing this paper this is just a research idea this will take time to implement and there is no guarantee that this will work well for our use case.
	
7. The idea of using some form of edge detection for the bounding box is also not very viable, the image below shows the output of an image  when we try running an edge detection algorithm.

![edged image](https://user-images.githubusercontent.com/41626118/87909347-b5eeab00-ca85-11ea-9df6-532346fe5c9d.png)


## Present requirements

1. The most urgent requirment is data corresponding to the use case. If the use case is only single object classification then more classes of single object images. If the requirment is multi object detection then images with multiple objects is required.

2. We also require the specification of the embedded device we will be working on, in order to continuously test if the developed model runs well on the edge device.
