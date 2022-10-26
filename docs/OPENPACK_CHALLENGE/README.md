# OpenPack Challenge 2022 @PerCom2023 WS

This page describes technical details of "OpenPack Challenge 2022".
For motivations, rules and timeline of this challenge, please check [https://open-pack.github.io/challenge2022](https://open-pack.github.io/challenge2022).

## Task

In this competition, you'll develop a time-series segmentation model that recognizes 10 work operations.
The required time resolution of the segmentation is 1 second.
Timeslots are defined based on data collection times. Please refer to the [evaluation/timeslot](#timeslot) section for more details.

If successful, your work will help the ubiquitous research community improve current smart factories and better integration of human factors into the smart-factory optimization process.

## Data

The Dataset for this challenge is [**OpenPack Dataset (v0.3.1)** (Realse Note)](https://open-pack.github.io/release/v0-3-1).
You can use all the modalities listed below as inputs. Please find the best sensor combination that fits your approach.

- ATR (acc, gyro, quaternion)
- E4 (acc, BVP, EDA, temperature)
- Kinect - Front View Camera (2d keypoints, depth)
- LiDAR - Front View (depth)
- RealSense - Top View Camera (depth)
- Meta Data
  - Order Sheet
  - HT Log Data
  - Psuedo Printer Log Data

### Download

```bash
# Step.1: Install a python package (openpack-toolkit).
pip install openpack-toolkit

# Step.2: Download the dataset.
optk-download -d ../data/datasets
```

### Splits

There are two types of data split, `DEBUG_SPLIT` and `OPENPACK_CHALLENGE_2022_SPLIT`.

#### `DEBUG_SPLIT`

This split can be used for checking the usage of the submission site and debugging your model.
This split consists of 1 subjects, 3 sessions for training, 1 session for validation and 1 session for testing.
Official tutorials are, in principle, implemented with this split.

#### `OPENPACK_CHALLENGE_2022_SPLIT`

This split is for a main challenge.
You can use data from 11 subjects for training. Test data consist of 6 subjects [U0104, U0108, U0110, U0203, U0204, and U0207].
Data from non-experienced workers have been excluded from this challenge.
In addition, sessions with recording errors are excluded from test data.
Training data with recording errors are included in the training data. So please consider that when using the data.
Recording errors are listed in [this page](../USER.md).

## Evaluation

The goal of this challenge is time-series classification with a 1s time-resolution.
Performance of your model will be evaluated based on the F1-measure (macro average).
In this section, we will explain the evaluation procedure and submission format in detail.

### Activity Set

Please refer to [`OPENPACK_OPERATIONS`](../ANNOTATION.md#1-openpack_operations).

Notes:

- 10 activity classes + `Null` class
- Samples with the `Null` label are ignored during evaluation.

### Timeslot

Timeslot is necessary to handle multimodal data with different sampling intervals.
The timeslot is defined based on the data collection time, and its size is set to 1 second.
Timeslot of a record is obtained by discarding the symbols under 1 second.
For example, when we got following timestamps (unixtime with milli second precision), you can get the timeslot by discarding the last three digits.

```txt
TIMESTAMP (UNIXTIME), Prediction (Class ID)
1634869193126, ID01 
1634869193225, ID01
1634869193324, ID04
1634869193423, ID04
1634869193522, ID01
1634869193621, ID01
1634869193720, ID01
1634869193819, ID01
1634869193918, ID01 => Timeslot ID = 1634869193 (= 2021-10-22- 11:19:53)
-------------- 
1634869194017, ID01 
1634869194116, ID01
1634869194215, ID01
1634869194314, ID03
1634869194413, ID01
1634869194512, ID01
1634869194611, ID01
...           => Timeslot ID = 1634869194 (= 2021-10-22- 11:19:54)
```

The predictions within the same timeslot will be aggregated into a single record.
The following example is aggregated records by selecting the last record within each timesplot.
This sequence is used to calculate the evaluation metric.

```txt
TIMESTAMP (UNIXTIME), Prediction (Class ID)
1634869193, ID01
1634869194, ID01
```

### Evaluation Metric

The F1-measure (macro-average) is used as the evaluation metric.
A F1-measure is calculated for each class and the average of all of them is used as the score.
Segments corresponding to the "Null" class are excluded before evaluation.
The winner will be selected based on this metric, evaluated on the test data.

In this competition, evaluation scores for each subject are included in the feedback.

### Function to Calculate Your Score

The script to calculate your score is available at [`optk.codalab.eval_operation_segmentation()`](../../openpack_toolkit/codalab/operation_segmentation/eval.py).

### Submission Format

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

Sample submission files for `Development Phase` are available here.

- [submission.json](./submission.json)
- [submission.zip](./submission.zip)

## Rules

### Use of External Dataset

You may use data other than the competition data to develop and test your submission. However, you should ensure that the external data is publicly available to anyone without any cost.

## Relevant links

- [OpenPack Challenge - Main Site](https://open-pack.github.io/)
- [Codalab (Submission Site)](https://codalab.lisn.upsaclay.fr/competitions/7830)
