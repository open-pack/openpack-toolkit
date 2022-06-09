from .._schema import DataStreamConfig, ImuConfig, KeypointConfig

OPENPACK_ATR_ACC_STREAM = ImuConfig(
    schema="ImuConfig",
    name="openpack-atr-acc",
    description="Accelerations from ATR IMU sensors",
    path=DataStreamConfig.Paths(
        template="${datarootdir}/dataset/openpack/{user}/{node}/{session}.csv",
    ),
    frame_rate=30,
    nodes=['atr01', 'atr02', 'atr03', 'atr04'],
    acc=True,
    gyro=False,
    quat=False,
)

OPENPACK_ATR_QAGS_STREAM = ImuConfig(
    schema="ImuConfig",
    name="openpack-atr-qags",
    description="Acceleration, gyro, and quaternion from ATR IMU sensors",
    path=DataStreamConfig.Paths(
        template="${datarootdir}/dataset/openpack/{user}/{node}/{session}.csv",
    ),
    frame_rate=30,
    nodes=['atr01', 'atr02', 'atr03', 'atr04'],
    acc=True,
    gyro=True,
    quat=True,
)

OPENPACK_KINECT_2D_KPT_STREAM = KeypointConfig(
    schema="KeypointConfig",
    name="openpack-kinect-2d-kpt",
    description="2D keypoint extracted by mmpose/hrnet",
    path=DataStreamConfig.Paths(
        template="${datarootdir}/dataset/openpack/{user}/2d-kpt/${model}/{session}.csv",
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
