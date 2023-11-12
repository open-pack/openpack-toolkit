from .._schema import DataStreamConfig, Metadata, DataLocation

ATR_QAGS_STREAM = DataStreamConfig(
    kind="dataset/stream/imu",
    name="atr-qags",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "IMU",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/atr",
        fname="${device}/${session}.csv",
    ),
    frameRate=30,
    devices=['atr01', 'atr02', 'atr03', 'atr04'],
    acc=True,
    gyro=True,
    quat=True,
)


ATR_ACC_STREAM = DataStreamConfig(
    kind="dataset/stream/imu",
    name="atr-acc",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "IMU/Acc",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/atr",
        fname="${device}/${session}.csv",
    ),
    frameRate=30,
    devices=['atr01', 'atr02', 'atr03', 'atr04'],
    acc=True,
    gyro=False,
    quat=False,
)


E4_ACC_STREAM = DataStreamConfig(
    kind="dataset/stream/e4",
    name="e4-acc",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "ACC",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/e4/${device}/acc",
        fname="${session}.csv",
    ),
    frameRate=32,
    devices=['e401', 'e402'],
)


E4_BVP_STREAM = DataStreamConfig(
    kind="dataset/stream/e4",
    name="e4-bvp",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "Blood Volume Pulse (BVP)",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/e4/${device}/bvp",
        fname="${session}.csv",
    ),
    frameRate=64,
    devices=['e401', 'e402'],
)


E4_EDA_STREAM = DataStreamConfig(
    kind="dataset/stream/e4",
    name="e4-eda",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "EDA",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/e4/${device}/eda",
        fname="${session}.csv",
    ),
    frameRate=4,
    devices=['e401', 'e402'],
)


E4_TEMP_STREAM = DataStreamConfig(
    kind="dataset/stream/e4",
    name="e4-temp",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "temperature",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/e4/${device}/temp",
        fname="${session}.csv",
    ),
    frameRate=4,
    devices=['e401', 'e402'],
)


KINECT_2D_KPT_STREAM = DataStreamConfig(
    kind="dataset/stream/keypoint",
    name="kinect-2d-kpt",
    metadata=Metadata(
        labels={
            "app": "openpack-benchmarks",
            "version": "1.0.0",
            "sensorType": "keypoint/2d",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/kinect/2d-kpt/mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2/single",
        fname="${session}.json",
    ),
    frameRate=15,
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


KINECT_3D_KPT_STREAM = DataStreamConfig(
    kind="dataset/stream/keypoint",
    name="kinect-3d-kpt",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "keypoint/3d",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/kinect/3d-kpt/k4abt/${preprocessing}",
        fname="${session}.json",
    ),
    frameRate=15,
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


KINECT_DEPTH_STREAM = DataStreamConfig(
    kind="dataset/stream/image",
    name="kinect-depth",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "depth/16bit-png",
            "view": "front-view",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/kinect/depth/frames",
        fname="${session}",
    ),
    frameRate=15,
)


RS02_DEPTH_STREAM = DataStreamConfig(
    kind="dataset/stream/image",
    name="rs02-depth",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "depth/16bit-png",
            "view": "top-view",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/rs02/depth/frames",
        fname="${session}",
    ),
    frameRate=15,
)


LIDAR_DEPTH_STREAM = DataStreamConfig(
    kind="dataset/stream/pointcloud",
    name="lidar-depth",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "lidar/point-cloud",
            "view": "front-view",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/lidar/frames",
        fname="${session}",
    ),
    frameRate=-1,
)


SYSTEM_HT_ORIGINAL_STREAM = DataStreamConfig(
    kind="dataset/stream/system/ht",
    name="system-ht-original",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "IoT/handheld-scanner",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/system/ht",
        fname="${session}.csv",
    ),
    frameRate=-1,
)


SYSTEM_ORDER_SHEET_STREAM = DataStreamConfig(
    kind="dataset/stream/system",
    name="system-order-sheet",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "system/order-sheet",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/system/order-sheet/",
        fname="${session}.csv",
    ),
    frameRate=-1,
)


SYSTEM_PRINTER_STREAM = DataStreamConfig(
    kind="dataset/stream/system/printer",
    name="system-printer",
    metadata=Metadata(
        labels={
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "IoT/printer/pseudo-data",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/system/printer",
        fname="${session}.csv",
    ),
    frameRate=-1,
)
