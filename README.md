# Introduction

The goal of the project is to be able to detect the removal of items from a chiller using visual techniques. The readme file will be updated as and when new code and functionality is pushed to the repository.

# System set up.

The repository has a package_requirements file that includes all the packages required to run code. The ideal set up would be to use create a virtual environment and run the following command to automatically download the required packages.

```

pip install -r package_requirements.txt

```

# The Google cloud setup.

The following are steps to be followed to setup the google cloud platform. Note that in order to avail use of GPU one has to register with a credit card but GCP does offer 300$ free credit. For more information click [here](cloud.google.com).

1.Most of the steps followed are similar to the instructions provided by [fastai](https://course.fast.ai/start_gcp.html). Following these instructions one should be able to install the google cloud CLI installed on their local system. Once the CLI is installed and setup the next step is to create an instance. One issue I faced while trying to apt-get the CLI was the issue of package version issues, which is easily solved by deleting the older and unnecessary version of certain packages. A simple google search solves the issue.

2.For our purposes I created an instance called fastai since our initial models will be using the fastai module. This can be done using the create an instance step given in the fastai guide. It is important to note that although they recommend using a preemptible instance I found that this is prone to being shut down without any warnings which can be both annoying and counter productive hence I believe it is better to create just a regular instance.

3. Once the instance is created it should be visible in the [VM instances page](https://console.cloud.google.com/compute/), check to see if the instance is running.

4. The next step is to SSH into the remote host. To do this first use the cloud shell on the instances page, using this you should be able to ssh into the system. Once this is done at the rsa public key of your local system to the authorized keys of the remote host this allows us to SSH into the remote host. After this it should be possible to SSH from the local machine. In case the connection still times it out could be that your ISP blocks the specific port to which we are trying to connect verify this by trying to connect to another server on the same port, if it fails get access to the specific port.

5. You should now be able to SSH into the remote host, the following command should allow access to the jupyter notebook as localhost.

```

export ZONE="us-west1-b"
export INSTANCE_NAME="my-fastai-instance" 
# check if the variables have been initialised correctly 
echo $ZONE
echo $INSTANCE_NAME
gcloud compute ssh --zone=$ZONE jupyter@$INSTANCE_NAME -- -L 8080:localhost:8080

```



6. Once the command is run you should have ssh'd into the host, then open [notebook](localhost:8080/tree) on your browser.


# Using the Jupyter notebook.

1. First checkout the notebook0.pynb that is part of the nb directory in fastai. This runs through the basics of using jupyter notebooks.

2. Next I would recommend watching the [first video](https://course.fast.ai/videos/?lesson=1) of the DL-1 fastai series. This runs through the basics of building a classifier using Resnet.

3. Once you have gone through the video check out colourclassifier.pynb which is the colour classifier I built based entirely on what is discussed in lecture-1.


