
# Introduction

This report details the progress in the chiller vision project for NUTY from the start of the project until the 7th of July.

# GCP setup

1. The first step was to set up the google cloud platform. There was initially an issue with SSh'ing into the server which we managed to fix in a day. 

2. Next, we set up an instance on the compute engine, initially we set up a preemptible instance which is cheaper than a regular instance but it can be shut off at any time without a warning this proved to be a big hindrance to progress since it seem to shut off every 5 mins. We hence switched to a normal instance.

3. Setup instructions for GCP are detailed in the README.

# Initial network and experiments.

1. Once the GCP setup was completed we moved on to training a neural network on fabricated data to see the performance.

2. While waiting for the NUTY data we created a shapes dataset with colors filled in, we wanted to see using this dataset if we could teach the network to identify colors like 

![shapes_colored](https://user-images.githubusercontent.com/41626118/86822769-ac3e6e00-c0a9-11ea-9da9-ed79fc1abcb9.png)

we prepared and trained 2 datasets with this same idea. 
  
  1. Colored shapes with a black background - We have 8 classes namely blue, orange, red, brown, white, green, yellow, purple each containing 30 ellipses, 30 rectangles and 50 polygons.
  2. Colored shapes with a white background - We have 8 classes namely blue, orange, red, brown, black, green, yellow, purple each containing 30 ellipses, 30 rectangles and 50 polygons.

These images were generating using a python screen available on this repository.

3. Training and Validation loss is shown in the image below along with error percentages. 20% of the images are used for validation.

![train_test_error](https://user-images.githubusercontent.com/41626118/86776782-19d0a700-c076-11ea-9ff5-fce83e38fb4d.png)

Although we achieve a low error percentage, the network did poorly while trying to classify real life objects of a certain colour like
![blue](https://user-images.githubusercontent.com/41626118/86824841-4f908280-c0ac-11ea-971a-9a2c1d34f719.jpg)

A possible reason is because our neural network has no past experience looking at such images, hence we have built a goof colored shape classifier but not a good color identifier.

# Training loss, Validation loss and error rate.

Here we explain the terms used in the error tables shown earlier. Here validation set refers to a portion of trainning data that is not used to train the network but the network performance is measured on this network since the network has not seen this data while training.

1. **Error rate** - On the validation set we compare the predicted output class of the input vs the actual class and the error rate is the measure of how often the prediction is incorrect on average.
2. **Training loss** - This is the [cross entropy loss](https://datascience.stackexchange.com/questions/20296/cross-entropy-loss-explanation) calculated on the training data.
3. **Validation loss** - This is the cross entropy loss calcullated on the validation data.

# Experimenting with initial NUTY data.

1. We then used the data provided by NUTY to train a network.

2. NUTY provided us with 3 classes of images. 276 images of Dominos burger box, 103 images of KFC burger box and 150 images of KFC popcorn box.A sample of images as shown below

![NUTY_sample](https://user-images.githubusercontent.com/41626118/86824615-02acac00-c0ac-11ea-84aa-e878a1a77015.png)


3. The training loss again was excellent with there essentially being no validation loss, the network did an excellent job in distinguishing between Dominos burger, KFC burger and KFC popcorn containers. The training validation loss as well as the error rates are shown below.

![train_test_error_NUTY](https://user-images.githubusercontent.com/41626118/86777259-89469680-c076-11ea-8d47-1ec67f117af0.png)

4. But the network did suffer with images that were hindered, for example images like

![Popcorn chicken image](https://hype.my/wp-content/uploads/2019/04/1-POPCORN-A-la-Carte-e1554090941249.jpg)

were not identified correctly. Hence it is important that we identify what type of images we need to identify and make sure we have training data that takes care of these conditions.

5. But this is expected since the network never encountered such images and has not learnt suitably to identify these images.

6. The training set provided by NUTY contained images were the image was shot at the same angle with the object rotated this does not create a diverse dataset, since the network intrinsically does some amount of rotation, hence it would be more useful to get images of the object at different angles as well as different images from the same company (Again based on the use case).

7. It is also to be noted that these images are of taken from a cell phone and are hence of high quality, we would need to also get access to camera photographs of lower quality to be able to see how well our network has learnt each specific class.

8. Finally, all our training is done on python using the [fastai](https://www.fast.ai/) python library which makes use of extensively trained neural networks based on [pytorch](https://pytorch.org/)

# Future steps 

1. Once we are provided with more data pertaining to each class we use this to build our first stage classifier and see how good of a classifier it is.

2. We would then need to use our saved model on an edge computer for real time classification.
