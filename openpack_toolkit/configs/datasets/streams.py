from .._schema import E4Config, DataStreamConfig, ImuConfig, KeypointConfig

ATR_ACC_STREAM = ImuConfig(
    schema="ImuConfig",
    name="atr-acc",
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

E4_ACC_STREAM = E4Config(
    schema="ImuConfig",
    name="e4-acc",
    sensor="",
    path=DataStreamConfig.Paths(
        dir="${path.openpack.rootdir}/${user.name}/e4/${device}/acc",
        fname="${session}.csv",
    ),
    frame_rate=32,
    devices=['e401', 'e402'],
)

E4_BVP_STREAM = E4Config(
    schema="ImuConfig",
    name="e4-bvp",
    sensor="",
    path=DataStreamConfig.Paths(
        dir="${path.openpack.rootdir}/${user.name}/e4/${device}/bvp",
        fname="${session}.csv",
    ),
    frame_rate=64,
    devices=['e401', 'e402'],
)

E4_EDA_STREAM = E4Config(
    schema="ImuConfig",
    name="e4-eda",
    sensor="",
    path=DataStreamConfig.Paths(
        dir="${path.openpack.rootdir}/${user.name}/e4/${device}/eda",
        fname="${session}.csv",
    ),
    frame_rate=4,
    devices=['e401', 'e402'],
)

E4_TEMP_STREAM = E4Config(
    schema="ImuConfig",
    name="e4-temp",
    sensor="",
    path=DataStreamConfig.Paths(
        dir="${path.openpack.rootdir}/${user.name}/e4/${device}/temp",
        fname="${session}.csv",
    ),
    frame_rate=4,
    devices=['e401', 'e402'],
)

KINECT_2D_KPT_STREAM = KeypointConfig(
    schema="KeypointConfig",
    name="kinect-2d-kpt",
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

SYSTEM_HT_ORIGINAL_STREAM = ImuConfig(
    schema="SystemDataConfig",
    name="system-ht-original",
    super_stream="None",
    path=DataStreamConfig.Paths(
        dir="${path.openpack.rootdir}/${user.name}/system/ht",
        fname="${session}.csv",
    ),
    frame_rate=-1,
)

SYSTEM_ORDER_SHEET_STREAM = ImuConfig(
    schema="SystemDataConfig",
    name="system-order-sheet",
    super_stream="None",
    path=DataStreamConfig.Paths(
        dir="${path.openpack.rootdir}/${user.name}/system/order-sheet/",
        fname="${session}.csv",
    ),
    frame_rate=-1,
)
