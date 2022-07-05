# Modality

1. `atr-qags`
1. `kinect-2d-kpt`

## [1] `atr-qags`

Acceleration, gyro, and quaternion data captured by ATR IMU sensors.

- Config File: [atr-qags.yaml](../configs/dataset/stream/atr-qags.yaml)
- Python Module: [`openpack_toolkit.configs.datasets.streams.ATR_QAGS_STREAM`](../openpack_toolkit/configs/datasets/streams.py)
- Frame Rate: 30

### 1-1: Path

```txt
${path.openpack.rootdir}/${user.name}/atr/${device}/${session}.csv
```

### 1-2: File Format (`csv`)



| # | Column Name | Description | Unit | Dtype | Note |
|---|-------------|-------------|------|-------|------|
| 0 | unixtime |  | milli second |  |  |
| 1 | acc_x |  | G |  |  |
| 2 | acc_y |  | G |  |  |
| 3 | acc_z |  | G |  |  |
| 4 | gyro_x |  | dps |  |  |
| 5 | gyro_y |  | dps |  |  |
| 6 | gyro_z |  | dps |  |  |
| 7 | quat_w |  |  |  |  |
| 8 | quat_x |  |  |  |  |
| 9 | quat_y |  |  |  |  |
| 10 | quat_z |  |  |  |  |

### 1-2: Meta Data

#### Device List

We attached 4 IMU sensors to subjects. IMU = [ATR TSND151](http://www.atr-p.com/products/TSND121_151.html).

| # | Device Name | Location | 
|---|---|---| 
| 0 | atr01 | Right Wrist | 
| 1 | atr02 | Left Wrist | 
| 2 | atr03 | Right Upper Arm | 
| 3 | atr04 | Left Upper Arm | 


## [2] `kinect-2d-kpt`

2D keypoint extracted by mmpose/hrnet. The model used to extract keypoints was 2-stage bottom-up model defined in [mmpose/2d_kpt_sview_rgb_vid/posewarper/posetrack18/hrnet_w48_posetrack18_384x288_posewarper_stage2.py](https://github.com/open-mmlab/mmpose/blob/master/configs/body/2d_kpt_sview_rgb_vid/posewarper/posetrack18/hrnet_w48_posetrack18_384x288_posewarper_stage2.py).

- Config File: [kinect-2d-kpt.yaml](../configs/dataset/stream/kinect-2d-kpt.yaml)
- Python Module: [`openpack_toolkit.configs.datasets.streams.KINECT_2D_KPT_STREAM`](../openpack_toolkit/configs/datasets/streams.py)
- Frame Rate: 15

### 2-1: Path

```txt
${path.openpack.rootdir}/${user.name}/kinect/${..category}/${..model}/single/${session}.json
```

### 2-2: File Format (`json`)

MS COCO format

| # | Column Name | Description | Unit | Dtype | Note |
|---|-------------|-------------|------|-------|------|
| 0 | info |  | None | dict |  |
| 1 | licences |  | None | list[dict] |  |
| 2 | annotations |  | None | list[dict] |  |
| 3 | annotations/id |  | None | int |  |
| 4 | annotations/image_id |  | milli seconds | int | UNIXtime with milli seconds precision |
| 5 | annotations/category_id |  | None | int |  |
| 6 | annotations/area |  | None | float |  |
| 7 | annotations/bbox |  | None | Tuple[float, float, float, float] | [x, y, width, height] |
| 8 | annotations/iscrowd |  | None | int | iscrowd = 0 |
| 9 | annotations/keypoints |  | px | list[float] | [x1, y1, v1, ...] (v? = confidence score) |
| 10 | annotations/num_keypoints |  | None | int |  |
| 11 | annotations/bbox_score |  | None | float | confidence score for the bounding box |
| 12 | annotations/track_id |  | None | int |  |
| 13 | category |  | None | list |  |

### 2-2: Meta Data

#### Keypoints

Keypoints are defined in MS COCO style.

| # | ID | Location | 
|---|---|---| 
| 0 | 0 | nose | 
| 1 | 1 | left_eye | 
| 2 | 2 | right_eye | 
| 3 | 3 | left_ear | 
| 4 | 4 | right_ear | 
| 5 | 5 | left_shoulder | 
| 6 | 6 | right_shoulder | 
| 7 | 7 | left_elbow | 
| 8 | 8 | right_elbow | 
| 9 | 9 | left_wrist | 
| 10 | 10 | right_wrist | 
| 11 | 11 | left_hip | 
| 12 | 12 | right_hip | 
| 13 | 13 | left_knee | 
| 14 | 14 | right_knee | 
| 15 | 15 | left_ankle | 
| 16 | 16 | right_ankle | 


