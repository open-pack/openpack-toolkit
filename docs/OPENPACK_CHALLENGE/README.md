# OpenPack Pilot Challenge - Work Operation Recognition Competition (Private)

- Competition Site (TBA)
- [HomePage](https://open-pack.github.io/)
- [zenodo (Dataset Repogitory)](https://doi.org/10.5281/zenodo.5909086)
- [GitHub - open-pack/openpack-toolkit (Dataset description and utilities)](https://github.com/open-pack/openpack-toolkit)
- [GitHub - open-pack/openpack-torch (Code samples)](https://github.com/open-pack/openpack-torch)

## Overview

Other than in daily life settings, Human Activity Recognition, has been applied to industrial domains to improve the efficiency of manual work.
Work processes, such as production line systems inside factories or packaging tasks at logistics centers, mainly depend on human workers.
To deal with the rapidly changing demands of customers and suppliers, works by human workers are expected to continue to play an important role in the future.
Therefore, quantifying such manual works is crucial for streamlining the work process, finding bottlenecks, assessing a worker’s performance, and detecting outliers.

In many manual works, such as packing tasks in the logistic domain, human workers repetitively perform a typical series of operations is iterated, with each iteration (i.e., work period) comprising a sequence of operations
such as assembling a shipping box and filling the box with items.
Getting information on each operation such as temporal location, duration, and anomalies is crucial for the optimization of the work process.
However, because the size of items to pack, the number of items, and the size of shipping items depend on shipping orders, sensor
data collected in different work periods and the duration of the same operation in different work periods vary.
These characteristics of the packaging work make the recognition task challenging.

In this competition, you’ll develop a model to recognize operations in packaging work from 4 IMU data and keypoint data.
The packaging work consists of 9 operations (i.e., activity classes) described below.
To quantify the operations as precisely as possible, dense labeling is required.
You must predict activity classes for each 1second-long timeslot.
You can use data from 4 subjects to develop your model.
The test data is 5 sessions from user U0107, 69 periods in total.

If successful, your work will help the ubiquitous research community improve current smart factories and better integrate human factors into the smart factory optimization process.

### Timeline

- Competition Site  Open: TBA
- Development Phase (Start): TBA
- Final Phase (Start): TBA
- Competition End: TBA

## Task & Evaluation

The problem to be solved is the multiclass classification problem of time-series data.
You must predict ["operation class"](../ANNOTATION.md#1-openpack_operations) for each timeslot.
The size of timeslot is set to 1 second in this challenge.

The F1 measure (macro-average) is used as the evaluation metric.
F1-measure is calculated for each class and the average of them is used as the score.
Segments corresponding to the "Null" class are excluded before evaluation.
The winner will be selected based on this metric evaluated on the test data.

Script to calculate your score is available at [`optk.codalab.eval_operation_segmentation()`](../../openpack_toolkit/codalab/operation_segmentation/eval.py)!

### Activity Class

[`OPENPACK_OPERATIONS`](../ANNOTATION.md#1-openpack_operations)

- 10 activity classes + `Null` class
- Samples with the `Null` label is ignored from the evaluation.

### Data Split

Train, Val, Test, and Submission split is described in [DATA_SPLIT](../DATA_SPLIT.md).
In the **Development** phase, you need to follow [**Debug** split](../DATA_SPLIT.md#1-debug).
In the **Final** phase, you need to follow [**Pilot Challenge** split](../DATA_SPLIT.md#2-pilot-challenge).
Therefore the submission file should contain prediction results of S0100, S0200, S0300, and S0500 of U0107, 69 periods in total.

NOTE: Validation and test sets are defined on the above page, but you can change them as you want.

## Data

For this challenge, you are given the sensor data (acceleration, etc.) and keypoints along with supporting metadata.
Your challenge is to predict activity classes at each timestep corresponding to the sensor data.
You can use data from 4 subjects (U0102, U0103, U0105, U0106) for training.
Data from U0107 is a submission set, so the annotation data is unavailable.

You can download the data from [zenodo - "OpenPack: Public multi-modal dataset for packaging work recognition in logistics domain"](https://zenodo.org/record/6697990).
Data structure information and data download utilities are described in [openpack-toolkit](../../).

### Quick Download

You can download all data (annotation, IMU, keypoints) with the following command.

```bash
pip install openpack-tooklit
mkdir -p ../data/datasets/
optk-download -d ../data/datasets/ -v v0.2.0 -s atr-qags,openpack-operations,kinect-2d-kpt
```

## Code Samples

Code samples written in PyTorch are available in [open-pack/openpack-torch](https://github.com/open-pack/openpack-torch).

---

## Registration

Registration is required to join this competition.
Please sign up from these two forms.

1. Participate Tab in Codalab >> Click "Sign Up"
1. [Google Form](https://docs.google.com/forms/d/e/1FAIpQLScSLsf7zbFH_KsRflnCqu_3ICqVI9KmOFt6XrBSR2G5J3aBfg/viewform?usp=sf_link)

From the Google Form, please register the team name, leader, and members of your team and agree to our competition
terms.
To sign up as Team, please refer to [this document](<https://github.com/codalab/codalab-competitions/wiki/User_Teams>).
The organizers will approve your team after submitting both forms and then now you can submit your predictions.
There is no limit to the number of team members.
Only one team from a single laboratory or equivalent group may participate to avoid private sharing.

## Submission Format

To submit your results to this competition you must construct a submission zip file containing a single file named `submission.json` containing your model’s prediction (operation ID) on the submission set and corresponding timestamp.
This file should follow the format detailed in the subsequent section.

```json
{
    "U0107-S0100": {
        "unixtime": [1634885785000, 1634885786000, 1634885787000, ...], // unixtime corresponding to prediction.
        "prediction": [100, 100, 100, ...], // Predicted Operation ID.
    },
    "U0107-S0200": {
        "unixtime": [1634885785000, 1634885786000, 1634885787000, ...],
        "prediction": [100, 100, 100, ...],
    },
    ...
}
```

Sample submission files for `Development Phase` are available from here.

- [submission.json](./submission.json)
- [submission.zip](./submission.zip)

---

## Terms and Conditions

### One Account per Team

Only the submission from the registered team leader will be considered in the leaderboard.
Submissions from the not registered user are ignored.

### No Private Sharing Outside Teams

Privately sharing code or data outside of teams is not permitted.
It’s OK to share code if made available to all participants on the forum.

### External Dataset

You may use data other than the competition data to develop and test your submission.
However, you will ensure the external data is publicly accessible without any cost.

### Winner

The winner is determined by the F1-measure (macro average) which you can see in the Results tab.

You agree that if you place in the **top-TBA** at the end of the challenge you must submit your code so that we can check for cheating.
As well as source code, winners are required to submit a short report paper that describes the award methodology in addition to the source code submission.
These instructions will be sent from the organizer via email.
