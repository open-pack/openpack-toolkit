from .._schema import DataStreamConfig, ImuConfig, KeypointConfig

ATR_ACC_STREAM = ImuConfig(
    schema="ImuConfig",
    name="atr-acc",
    description="Accelerations from ATR IMU sensors",
    super_stream="atr-qags",
    path=DataStreamConfig.Paths(
        dir="${path.openpack.rootdir}/${user.name}/atr/${device}",
        fname="${session}.csv",
    ),
    frame_rate=30,
    devices=['atr01', 'atr02', 'atr03', 'atr04'],
    acc=True,
    gyro=False,
    quat=False,
)

ATR_QAGS_STREAM = ImuConfig(
    schema="ImuConfig",
    name="atr-qags",
    description="Acceleration, gyro, and quaternion data captured by ATR IMU sensors.",
    super_stream="None",
    path=DataStreamConfig.Paths(
        dir="${path.openpack.rootdir}/${user.name}/atr/${device}",
        fname="${session}.csv",
    ),
    frame_rate=30,
    devices=['atr01', 'atr02', 'atr03', 'atr04'],
    acc=True,
    gyro=True,
    quat=True,
)

KINECT_2D_KPT_STREAM = KeypointConfig(
    schema="KeypointConfig",
    name="kinect-2d-kpt",
    description="2D keypoint extracted by mmpose/hrnet. The model used to extract keypoints was 2-stage bottom-up model defined in [mmpose/2d_kpt_sview_rgb_vid/posewarper/posetrack18/hrnet_w48_posetrack18_384x288_posewarper_stage2.py](https://github.com/open-mmlab/mmpose/blob/master/configs/body/2d_kpt_sview_rgb_vid/posewarper/posetrack18/hrnet_w48_posetrack18_384x288_posewarper_stage2.py).",
    super_stream="None",
    path=DataStreamConfig.Paths(
        dir="${path.openpack.rootdir}/${user.name}/kinect/${..category}/${..model}/single",
        fname="${session}.json",
    ),
    frame_rate=15,
    category="2d-kpt",
    model="mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2",
    nodes={
        0: "nose",
        1: "left_eye",
        2: "right_eye",
        3: "left_ear",
        4: "right_ear",
        5: "left_shoulder",
        6: "right_shoulder",
        7: "left_elbow",
        8: "right_elbow",
        9: "left_wrist",
        10: "right_wrist",
        11: "left_hip",
        12: "right_hip",
        13: "left_knee",
        14: "right_knee",
        15: "left_ankle",
        16: "right_ankle",
    },
)
