# Introduction

This is a project log containing ideas and discussions between Deva and Shreyas. Log starts from July 9th.

# July 9th

* Goal of the  day was to obscure certain parts of the image and see how well the network identifies objects.
* 3 Cases for each of the classes were taken from each view, obscured using a black marker without any methodology using GIMP.
* Dominos boxes were easily recognized but some struggle was present in recognising KFC boxes especially in the side angle, popcorn boxes were also recognized again except the side angle which was recognised as a KFC burger box.
* It is important to remember that our data is slightly **biased towards Dominos boxes since there are 276 cases of such boxes vs 150 and 103 each of the KFC boxes** this results in an imbalanced dataset. This could be the reason why the network finds it easier to identify Dominos boxes simply because it has seen more of them that the others. Hence it is important we try to maintain balance within the classes in the data.
* Next, we have to come up with a way to formalize and generalize this process, Deva suggested cropping out some part of the image and seeing how well the classifer works.
* For the next set of incoming data, we should also ask for obscured data embedded in the dataset itself. That is, images with hands picking up the boxes and essentially obscurring the camer ain any way possible.
