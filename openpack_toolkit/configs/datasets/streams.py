from .._schema import DataStreamConfig

ATR_ACC_STREAM = DataStreamConfig(
    kind="dataset/stream/imu",
    name="atr-acc",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "IMU/Acc",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/atr",
        "fname": "${device}/${session}.csv",
    },
    frameRate=30,
    devices=['atr01', 'atr02', 'atr03', 'atr04'],
    acc=True,
    gyro=False,
    quat=False,
)


ATR_QAGS_STREAM = DataStreamConfig(
    kind="dataset/stream/imu",
    name="atr-qags",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "IMU",
            "sensorProductName": "ATR TSND151",
            "sensorProdcutReference": "http://www.atr-p.com/products/TSND121_151.html",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/atr",
        "fname": "${device}/${session}.csv",
    },
    frameRate=30,
    devices=['atr01', 'atr02', 'atr03', 'atr04'],
    acc=True,
    gyro=True,
    quat=True,
)


E4_ACC_STREAM = DataStreamConfig(
    kind="dataset/stream/e4",
    name="e4-acc",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensor": "e4",
            "sensorType": "acceleration",
            "sensorProductName": "Empatica E4",
            "sensorProdcutReference": "https://www.empatica.com/en-int/research/e4/",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/e4/${device}/acc",
        "fname": "${session}.csv",
    },
    frameRate=32,
    devices=['e401', 'e402'],
)


E4_BVP_STREAM = DataStreamConfig(
    kind="dataset/stream/e4",
    name="e4-bvp",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensor": "e4",
            "sensorType": "Blood Volume Pulse (BVP)",
            "sensorProductName": "Empatica E4",
            "sensorProdcutReference": "https://www.empatica.com/en-int/research/e4/",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/e4/${device}/bvp",
        "fname": "${session}.csv",
    },
    frameRate=64,
    devices=['e401', 'e402'],
)


E4_EDA_STREAM = DataStreamConfig(
    kind="dataset/stream/e4",
    name="e4-eda",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensor": "e4",
            "sensorType": "EDA",
            "sensorProductName": "Empatica E4",
            "sensorProdcutReference": "https://www.empatica.com/en-int/research/e4/",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/e4/${device}/eda",
        "fname": "${session}.csv",
    },
    frameRate=4,
    devices=['e401', 'e402'],
)


E4_TEMP_STREAM = DataStreamConfig(
    kind="dataset/stream/e4",
    name="e4-temp",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensor": "e4",
            "sensorType": "temperature",
            "sensorProductName": "Empatica E4",
            "sensorProdcutReference": "https://www.empatica.com/en-int/research/e4/",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/e4/${device}/temp",
        "fname": "${session}.csv",
    },
    frameRate=4,
    devices=['e401', 'e402'],
)


KINECT_2D_KPT_STREAM = DataStreamConfig(
    kind="dataset/stream/keypoint",
    name="kinect-2d-kpt",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensorProdcutName": "Azure Kinect DK",
            "sensorProdcutReference": "https://azure.microsoft.com/ja-jp/products/kinect-dk/",
            "keypointType": "2d",
            "poseEstimationModel": "mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2",
            "mmposeUrl": "https://github.com/open-mmlab/mmpose/blob/master/configs/body/2d_kpt_sview_rgb_vid/posewarper/posetrack18/hrnet_w48_posetrack18_384x288_posewarper_stage2.py",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/kinect/2d-kpt/${...metadata.labels.poseEstimationModel}/single",
        "fname": "${session}.json",
    },
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
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensorProdcutName": "Azure Kinect DK",
            "sensorProdcutReference": "https://azure.microsoft.com/ja-jp/products/kinect-dk/",
            "keypointType": "3d",
            "poseEstimationModel": "k4abt",
            "sdkUrl": "https://learn.microsoft.com/ja-jp/azure/kinect-dk/build-first-body-app",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/kinect/3d-kpt/${...metadata.labels.poseEstimationModel}/${preprocessing}",
        "fname": "${session}.json",
    },
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
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensor": "kinect",
            "sensorProdcutName": "Azure Kinect DK",
            "sensorProdcutReference": "https://azure.microsoft.com/ja-jp/products/kinect-dk/",
            "imageType": "depth",
            "preprocessing": "k4a_transformation_depth_image_to_color_camera()",
            "preprocessingReference": "https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/group___functions_gafacffb5f781a9c2df30d4a16241cd514.html",
            "view": "front-view",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/kinect/depth/frames",
        "fname": "${session}",
    },
    frameRate=15,
)


RS02_DEPTH_STREAM = DataStreamConfig(
    kind="dataset/stream/image",
    name="rs02-depth",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensor": "rs02",
            "sensorProdcutName": "Realsense",
            "sensorProdcutReference": "https://www.intel.com/content/www/us/en/products/sku/190004/intel-realsense-depth-camera-d435i/specifications.html",
            "imageType": "depth",
            "preprocessing": "None",
            "view": "top-view",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/rs02/depth/frames",
        "fname": "${session}",
    },
    frameRate=15,
)


SYSTEM_HT_ORIGINAL_STREAM = DataStreamConfig(
    kind="dataset/stream/system/ht",
    name="system-ht-original",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "IoT/handheld-scanner",
            "sensorProductName": "None",
            "sensorProdcutReference": "None",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/system/ht",
        "fname": "${session}.csv",
    },
    frameRate=-1,
)


SYSTEM_ORDER_SHEET_STREAM = DataStreamConfig(
    kind="dataset/stream/system",
    name="system-order-sheet",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "system/order-sheet",
            "sensorProductName": "None",
            "sensorProdcutReference": "None",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/system/order-sheet/",
        "fname": "${session}.csv",
    },
    frameRate=-1,
)


SYSTEM_PRINTER_STREAM = DataStreamConfig(
    kind="dataset/stream/system/printer",
    name="system-printer",
    metadata={
        "labels": {
            "app": "openpack",
            "version": "1.0.0",
            "sensorType": "IoT/printer (pseudo data)",
            "sensorProductName": "None",
            "sensorProdcutReference": "None",
        }
    },
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/system/printer",
        "fname": "${session}.csv",
    },
    frameRate=-1,
)
