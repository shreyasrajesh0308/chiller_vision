
# Introduction

This report details the progress in the chiller vision project for NUTY from the start of the project until the 7th of July.

# GCP setup

1. The first step was to set up the google cloud platform. There was initially an issue with SSh'ing into the server which we managed to fix in a day. 

2. Next, we set up an instance on the compute engine, initially we set up a preemptible instance which is cheaper than a regular instance but it can be shut off at any time without a warning this proved to be a big hindrance to progress since it seem to shut off every 5 mins. We hence switched to a normal instance.

# Initial network and experiments.

1. Once the GCP setup was completed we moved on to training a neural network on fabricated data to see the performance.

2. We created a shapes dataset with colors filled in, we wanted to see using this dataset if we could teach the network to identify colors/

3. We noticed that even though the network achieved a very small error rate and training loss it did not do very well in classifying images that were not shapes that were used in training, hence it had difficulty in identifying any real life objects.

# Experimenting with initial NUTY data.

1. We then used the data provided by NUTY to train a network.

2. The training loss again was excellent with there essentially being no validation loss, the network did an excellent job in distinguishing between Dominos burger, KFC burger and KFC popcorn containers.

3. But the network did suffer with images that were hindered, for example images like

![Popcorn chicken image](https://www.google.com/imgres?imgurl=https%3A%2F%2Fassets.change.org%2Fphotos%2F3%2Fie%2Fsq%2FBkIeSqNGinVhbuK-800x450-noPad.jpg%3F1532525708&imgrefurl=https%3A%2F%2Fwww.change.org%2Fp%2Fthe-public-bargain-buckets-of-popcorn-chicken-to-be-sold-at-kfc&tbnid=xOOleaakJqvglM&vet=12ahUKEwj5_Jm96LrqAhVm_TgGHS8oC5EQMygLegUIARDfAQ..i&docid=iOin5GD5VJwaaM&w=676&h=380&q=kfc%20popcorn%20chicken%20&ved=2ahUKEwj5_Jm96LrqAhVm_TgGHS8oC5EQMygLegUIARDfAQ)

were not identified correctly. Hence it is important that we identify what type of images we need to identify and make sure we have training data that takes care of these conditions.

4. The training set provided by NUTY contained images were the image was shot at the same angle with the object rotated this does not create a diverse dataset, since the network intrinsically does some amount of rotation, hence it would be more useful to get images of the object at different angles as well as different images from the same company (Again based on the use case).

5. Finally, all our training is done on python using the [fastai](https://www.fast.ai/) python library which makes use of extensively trained neural networks based on [pytorch](https://pytorch.org/)
