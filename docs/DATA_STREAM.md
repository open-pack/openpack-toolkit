# Modality

1. `atr-qags`
1. `kinect-2d-kpt`
1. `e4-acc`
1. `e4-bvp`
1. `e4-eda`
1. `e4-temp`
1. `system-ht-original`
1. `system-order-sheet`

## [1] `atr-qags`

Acceleration, gyro, and quaternion data captured by ATR IMU sensors.

- Config File: [atr-qags.yaml](../configs/dataset/stream/atr-qags.yaml)
- Python Module: [`openpack_toolkit.configs.datasets.streams.ATR_QAGS_STREAM`](../openpack_toolkit/configs/datasets/streams.py)
- Frame Rate: 30 Hz

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
- Frame Rate: 15 Hz

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


## [3] `e4-acc`

Acc data from Empatica E4 sensors

- Config File: [e4-acc.yaml](../configs/dataset/stream/e4-acc.yaml)
- Python Module: [`openpack_toolkit.configs.datasets.streams.E4_ACC_STREAM`](../openpack_toolkit/configs/datasets/streams.py)
- Frame Rate: 32 Hz

### 3-1: Path

```txt
${path.openpack.rootdir}/${user.name}/e4/${device}/acc/${session}.csv
```

### 3-2: File Format (`csv`)



| # | Column Name | Description | Unit | Dtype | Note |
|---|-------------|-------------|------|-------|------|
| 0 | time |  | milli second |  |  |
| 1 | acc_x |  | G |  |  |
| 2 | acc_y |  | G |  |  |
| 3 | acc_z |  | G |  |  |

### 3-2: Meta Data

#### Device List

We attached 2 [Empatica E4](https://www.empatica.com/en-int/research/e4/) sensors to subjects.

| # | Device Name | Location | 
|---|---|---| 
| 0 | e401 | Right Wrist | 
| 1 | e402 | Left Wrist | 


## [4] `e4-bvp`

BVP (Blood Volume Pulse) data from Empatica E4 sensors

- Config File: [e4-bvp.yaml](../configs/dataset/stream/e4-bvp.yaml)
- Python Module: [`openpack_toolkit.configs.datasets.streams.E4_BVP_STREAM`](../openpack_toolkit/configs/datasets/streams.py)
- Frame Rate: 64 Hz

### 4-1: Path

```txt
${path.openpack.rootdir}/${user.name}/e4/${device}/bvp/${session}.csv
```

### 4-2: File Format (`csv`)



| # | Column Name | Description | Unit | Dtype | Note |
|---|-------------|-------------|------|-------|------|
| 0 | time |  | milli second |  |  |
| 1 | bvp |  | mmHg |  |  |

### 4-2: Meta Data

#### Device List

We attached 2 [Empatica E4](https://www.empatica.com/en-int/research/e4/) sensors to subjects.

| # | Device Name | Location | 
|---|---|---| 
| 0 | e401 | Right Wrist | 
| 1 | e402 | Left Wrist | 


## [5] `e4-eda`

EDA data from Empatica E4 sensors

- Config File: [e4-eda.yaml](../configs/dataset/stream/e4-eda.yaml)
- Python Module: [`openpack_toolkit.configs.datasets.streams.E4_EDA_STREAM`](../openpack_toolkit/configs/datasets/streams.py)
- Frame Rate: 4 Hz

### 5-1: Path

```txt
${path.openpack.rootdir}/${user.name}/e4/${device}/eda/${session}.csv
```

### 5-2: File Format (`csv`)



| # | Column Name | Description | Unit | Dtype | Note |
|---|-------------|-------------|------|-------|------|
| 0 | time |  | milli second |  |  |
| 1 | eda |  | microsiemens |  |  |

### 5-2: Meta Data

#### Device List

We attached 2 [Empatica E4](https://www.empatica.com/en-int/research/e4/) sensors to subjects.

| # | Device Name | Location | 
|---|---|---| 
| 0 | e401 | Right Wrist | 
| 1 | e402 | Left Wrist | 


## [6] `e4-temp`

Temp (temperature) data from Empatica E4 sensors

- Config File: [e4-temp.yaml](../configs/dataset/stream/e4-temp.yaml)
- Python Module: [`openpack_toolkit.configs.datasets.streams.E4_TEMP_STREAM`](../openpack_toolkit/configs/datasets/streams.py)
- Frame Rate: 4 Hz

### 6-1: Path

```txt
${path.openpack.rootdir}/${user.name}/e4/${device}/temp/${session}.csv
```

### 6-2: File Format (`csv`)



| # | Column Name | Description | Unit | Dtype | Note |
|---|-------------|-------------|------|-------|------|
| 0 | time |  | milli second |  |  |
| 1 | temp |  | microsiemens |  |  |

### 6-2: Meta Data

#### Device List

We attached 2 [Empatica E4](https://www.empatica.com/en-int/research/e4/) sensors to subjects.

| # | Device Name | Location | 
|---|---|---| 
| 0 | e401 | Right Wrist | 
| 1 | e402 | Left Wrist | 


## [7] `system-ht-original`

Scan log data from a handy terminal.

- Config File: [system-ht-original.yaml](../configs/dataset/stream/system-ht-original.yaml)
- Python Module: [`openpack_toolkit.configs.datasets.streams.SYSTEM_HT_ORIGINAL_STREAM`](../openpack_toolkit/configs/datasets/streams.py)
- Frame Rate: 30 Hz

### 7-1: Path

```txt
${path.openpack.rootdir}/${user.name}/system/ht/${session}.csv
```

### 7-2: File Format (`csv`)



| # | Column Name | Description | Unit | Dtype | Note |
|---|-------------|-------------|------|-------|------|
| 0 | unixtime |  | milli second | int |  |
| 1 | datetime |  | None | str (ISO format) |  |
| 2 | order_sheet |  | None | str |  |
| 3 | box |  | None | str |  |
| 4 | item |  | None | str |  |

### 7-2: Meta Data

No DATA

## [8] `system-order-sheet`

Master data of order sheets.

- Config File: [system-order-sheet.yaml](../configs/dataset/stream/system-order-sheet.yaml)
- Python Module: [`openpack_toolkit.configs.datasets.streams.SYSTEM_ORDER_SHEET_STREAM`](../openpack_toolkit/configs/datasets/streams.py)
- Frame Rate: 30 Hz

### 8-1: Path

```txt
${path.openpack.rootdir}/${user.name}/system/order-sheet//${session}.csv
```

### 8-2: File Format (`csv`)



| # | Column Name | Description | Unit | Dtype | Note |
|---|-------------|-------------|------|-------|------|
| 0 | sheet_no |  | None | str | format = DEN{session_no:0=4}{box_no:0=2} |
| 1 | session |  | None | str |  |
| 2 | box |  | None | str |  |
| 3 | pattern |  | None | str |  |
| 4 | total_amount |  | None | str |  |
| 5 | item1 |  | None | str |  |
| 6 | item2 |  | None | str |  |
| 7 | item3 |  | None | str |  |
| 8 | item4 |  | None | str |  |
| 9 | item5 |  | None | str |  |
| 10 | amount1 |  | None | str |  |
| 11 | amount2 |  | None | str |  |
| 12 | amount3 |  | None | str |  |
| 13 | amount4 |  | None | str |  |
| 14 | amount5 |  | None | str |  |

### 8-2: Meta Data

#### Combination Patterns of Items

-

| # | Key | Amount | Size Category | 
|---|---|---|---| 
| 0 | S1 |  |  | 
| 1 | S2 |  |  | 
| 2 | S3 |  |  | 
| 3 | S4 |  |  | 
| 4 | S5 |  |  | 
| 5 | M1 |  |  | 
| 6 | M2 |  |  | 
| 7 | M3 |  |  | 
| 8 | M4 |  |  | 
| 9 | M5 |  |  | 
| 10 | L1 |  |  | 
| 11 | L2 |  |  | 
| 12 | L3 |  |  | 
| 13 | L4 |  |  | 
| 14 | L5 |  |  | 
| 15 | MIX2 |  |  | 
| 16 | MIX3 |  |  | 
| 17 | MIX4 |  |  | 


