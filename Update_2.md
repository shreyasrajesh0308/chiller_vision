# Update

1. This is an update after the initial update provided where we showed how the neural network works with toy data and initial NUTY dataset.

2. The model we have can be extended to perform object recognition of various classes but it is limited in the sense that it can only perform single image classification. That is given an image with one image the model will be able to recognize the object.
That is  an object like 

![Single_label](https://user-images.githubusercontent.com/41626118/88027689-3fb97980-cb55-11ea-9cda-177eda69b966.png)

can be identified but we cannot perform a classification for images with multiple objects. For example, an image with both a KFC box and a Dominos box.

3. The effectiveness of the neural network has to be tested against a dataset that is not shown to the network while training. This form the test dataset and it is the only true measure of how well the network has trained. An article on the difference between the different types of datasets can be found [here](https://towardsdatascience.com/train-validation-and-test-sets-72cb40cba9e7).

4. If classification has to be done using a camera inside the chiller , we have two cases of what has to be done.

	1. We have a single object that has to be recognized, this is possible with our current model.
	
	2. If multiple objects have to be identified, our present model is not sufficient. In this case we'd have to perform [object detection](https://en.wikipedia.org/wiki/Object_detection) which would require a dataset that has, around each of the objects in an image, a rectangular box called the bounding box that encapsulates the entire object.
		
	3. Generating this dataset is not an easy task but unfortunately there is no way around it. A [paper](https://arxiv.org/pdf/1904.09781.pdf) by Yi et al. discuss a possible use case where the generate bounding boxes for the images while classification but train without any such requirments. 
	
	4. While we could try and work on implementing this paper this is just a research idea this will take time to implement and there is no guarantee that this will work well for our use case.
	
5. The idea of using some form of edge detection for the bounding box is also not very viable, the image below shows the output of an image  when we try running an edge detection algorithm.

![edged image](https://user-images.githubusercontent.com/41626118/87909347-b5eeab00-ca85-11ea-9df6-532346fe5c9d.png)

6. We also require the specification of the embedded device we will be working on, in order to continuosly test if the developed model runs well on the edge device.
