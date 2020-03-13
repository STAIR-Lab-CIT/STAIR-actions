# STAIR Actions (version 1.1)
"STAIR Actions" is a large-scale video dataset for action recognition research.  It consists of 100 categories of everyday human actions, which is listed in this [table](actionlist.csv).  For each action, there are around 1000 videos, 10% of which are kept unpublished for possible future competition.  For more detailed information, please refer to http://actions.stair.center .

The current version of STAIR Actions is v1.1.
The summary of difference between v1.0 and v1.1 is [here](data/diff_train_from_v1.0_to_v1.1.csv).

# Terms of Use
By downloading "STAIR Actions" (the Dataset), you agree to the following terms.
* You will use the Dataset only for the purpose of AI research.
* You will NOT distribute the Dataset or any parts thereof.
* You will treat people appearing in the Dataset with respect and dignity.
* The Dataset comes with no warranty or guarantee of any kind, and you accept full liability.

# License
Assuming you agree the terms of use, 
* STAIR Actions metadata file (.json) is licensed under Creative Commons Attribution 4.0 International license (CC BY 4.0)
  - (https://creativecommons.org/licenses/by/4.0/legalcode)
* The type field of STAIR Actions medata file (.json) indicates license condition of individual movie file by one character, where C, X, Y indicate Creative Commons CC0 Public Domain Dedication, ordinary YouTube license, CC BY, respectively. 
  - (https://creativecommons.org/publicdomain/zero/1.0/deed.en)
* Other code in this repository is delivered under the Apache 2 license.

# Release Notes

## v1.1
- Some YouTube videos have been newly added. 
- Videos in the following files have been removed.
  - [inappropriate.csv](https://github.com/STAIR-Lab-CIT/STAIR-actions/blob/v1.0/inappropriate.csv) includes files, the contents of which is regarded as "inappropriate" by anonymous reviewers.
  - [audio_problem.csv](https://github.com/STAIR-Lab-CIT/STAIR-actions/blob/v1.0/audio_problem.csv) includes files that have some trouble in audio channel.
  - [tooshort_toolong.csv](https://github.com/STAIR-Lab-CIT/STAIR-actions/blob/v1.0/tooshort_toolong.csv) includes files too short (less than 3 sec) or too long (longer than 10 sec).
- Videos in the following file have been recategorized.
  - [recommend_recategorize.csv](https://github.com/STAIR-Lab-CIT/STAIR-actions/blob/v1.0/recommend_recategorize.csv)
- The summary of difference between v1.0 and v1.1 is [here](data/diff_train_from_v1.0_to_v1.1.csv).

## v1.0
- Files in the following lists are recommended to be removed.
  - [inappropriate.csv](https://github.com/STAIR-Lab-CIT/STAIR-actions/blob/v1.0/inappropriate.csv) includes files, the contents of which is regarded as "inappropriate" by anonymous reviewers.
  - [audio_problem.csv](https://github.com/STAIR-Lab-CIT/STAIR-actions/blob/v1.0/audio_problem.csv) includes files that have some trouble in audio channel.
  - [tooshort_toolong.csv](https://github.com/STAIR-Lab-CIT/STAIR-actions/blob/v1.0/tooshort_toolong.csv) includes files too short (less than 3 sec) or too long (longer than 10 sec).
- Some movies may be wrongly categorized.  The following list includes known mistakes with recommended categories.
  - [recommend_recategorize.csv](https://github.com/STAIR-Lab-CIT/STAIR-actions/blob/v1.0/recommend_recategorize.csv)

# How to get STAIR Actions v1.1

We provide a download script for STAIR Actions `download.sh`, which enables you to download both STAIR Actions (C) and (Y) at one time.
**We highly recommend that you will run the script on a storage with over 1TB space.**

**The download script uses the crawler included in [ActivityNet repository](https://github.com/activitynet/ActivityNet) to get YouTube videos.
To run the crawler, you need to construct python environment, following this [README](https://github.com/activitynet/ActivityNet/blob/master/Crawler/Kinetics/README.md).
Additionally, you need to install git, [ffmpeg](https://www.ffmpeg.org/) and [jq](https://stedolan.github.io/jq/) in advance to run the download script.**

After the construction of the enviromnent, 
you can download STAIR Actions by just executing the following command.
```
$ bash download.sh
```
It will takes a few days until the end of the execution. 
Finally, STAIR Actions will be created in `STAIR_Actions_[version]/` directory, where [version] is the version number of STAIR Actions to be downloaded.
Note that some video clips will not be generated because some YouTube videos cannot be downloaded ater constructing this dataset.

## FAQ
### No videos in downloaded zip files
Some actions such as walking do not have videos shot by crowdsourcing.
Therefore, zip files for such actions contain an empty directory only.

# Benchmark Results
The following table shows benchmark results on validation set using our Chainer implementations of [3D-ResNets](https://github.com/kenshohara/3D-ResNets-PyTorch).
All the models started training using the provided pretrained models in [3D-ResNets](https://github.com/kenshohara/3D-ResNets-PyTorch) which are learned on Kinetics-400 dataset.
Then, we learned these models in two phases by changing hyperparameters.
In the first phase, we trained the models by MomentumSGD (lr=0.001, momentum=0.9) and weight decay (rate=1e-05), and kept the model which achieved best accuracy on the validation set.
In the second phase, we set the parameters of the best model as initial values, and trained the model again by MomentumSGD (lr=0.0001, momentum=0.9) and weight decay (rate=1e-05).

|                      	| ResNet-50 	| ResNet-101 	| ResNet-152 	| ResNeXt-101 	|
|---------------------:	|----------:	|-----------:	|-----------:	|------------:	|
|     UCF101 (split-1) 	|    0.8699 	|     0.7295 	|     0.7079 	|      0.8517 	|
|     HMDB51 (split-1) 	|    0.5738 	|     0.4464 	|     0.4686 	|      0.5516 	|
| STAIR Actions (v1.1) 	|    0.7656 	|     0.7766 	|     0.7666 	|      0.8168 	|

# References
- Yuya Yoshikawa, Jiaqing Lin, Akikazu Takeuchi, "STAIR Actions: A Video Dataset of Everyday Home Actions," arXiv:1804.04326, Apr. 2018. [[PDF](https://arxiv.org/abs/1804.04326)]
- Yuya Yoshikawa, Akikazu Takeuchi, "Constructing a Large-Scale Video Dataset for Human Action Recognition at Home and Office," Annual Meeting of the Japanese Society for Artificial Intelligence (JSAI2017), 2017. (In Japanese) [[PDF](https://kaigi.org/jsai/webprogram/2017/pdf/230.pdf)]




