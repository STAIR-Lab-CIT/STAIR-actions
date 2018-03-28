# STAIR Actions
"STAIR Actions" is a large-scale video dataset for action recognition research.  It consists of 100 categories of everyday human actions, which is listed in this [table](actionlist.csv).  For each action, there 1000 videos, 10% of which are kept unpublished for possible future c ompetition.  For detailed information about STAIR Actions, please refer to http://actions.stair.center .

STAIR Actions consists of two parts.  One is called "STAIR Actions (C) that is a collection of videos newly created by crowd workers for this purpose.  Note that various form of papers reading "Stair lab." may appear in the videos.  Indeed, this is a sign of "a video was newly-created on our demand."  The other part is called "STAIR Actions (Y) that is a collection of metadata of YouTube videos.  STAIR Actions (Y) is provided in the form of JSON format.  Each metadata indicates some segment of a video captures certain action.

## File name format

Format of a video file name is the following:  

     a[nnn]-[mmmm][source].mp4  

where  

    [nnn] is a 3-digit number id of an action category. [actionlist.csv](actionlist.csv) shows correspondence between numbers and actions.
    
    [mmmm] is a 4-digit number to discrinate individual files within a category.  
    
    [source] is a character, either C/X/Y/Z, each indicates the following  

> >        "C" means a video from STAIR Actions (C)  

> >        "Y" and "Z" mean a video from STAIR Actions (Y) with Creative Commons lisence  

> >        "X" means a video from STAIR Actions (X) with ordinary YouTube license  

# How to get STAIR Actions

## How to get STAIR Actions (C)

## How to get STAIR Actions (Y)

# Version 1.0 Release Notes
Files in the following lists are recommended to be removed.
 [inappropriate.csv](inappropriate.csv) includes files, the contents of which is regarded as "inappropriate" by anonymous reviewers.

 [audio_problem.csv](audio_problem.csv) includes files that have some trouble in audio channel.

 [tooshort_toolong.csv](tooshort_toolong.csv) includes files too short (less than 3 sec) or too long (longer than 10 sec).

Some movies may be wrongly categorized.  The following list includes known mistakes with recommended categories.

[recommend_recategorize.csv](recommend_recategorize.csv)


# Reference

Yuya Yoshikawa, Akikazu Takeuchi, "Constructing a Large-Scale Video Dataset for Human Action Recognition at Home and Office," Annual Meeting of the Japanese Society for Artificial Intelligence (JSAI2017), 2017. (In Japanese) [[PDF](https://kaigi.org/jsai/webprogram/2017/pdf/230.pdf)]

# Terms of use

Purpose of the usage of this dataset is limited to research of machine learning.  By downloading the dataset, it is understood that a user agrees to this condition.

Under the abovementioned agreement, STAIR Actions (Y) is delivered under the license Creative Commons Attribution 4.0 International license (CC BY 4.0)  https://creativecommons.org/licenses/by/4.0/legalcode , and STAIR Actions (C) is delivered under the license Creative Commons CC0 Public Domain Dedication https://creativecommons.org/publicdomain/zero/1.0/deed.en .

Other code in this repository is delivered under the Apache 2 license.

