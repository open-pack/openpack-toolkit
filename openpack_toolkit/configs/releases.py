from ._schema import ReleaseConfig, Metadata, DataLocation

RELEASE_CONFIG_V1_0_0 = ReleaseConfig(
    kind="openpack/release",
    name="${.metadata.labels.version}",
    metadata=Metadata(
        labels={
            "version": "v1.0.0",
            "release": "2023-07-14",
        }
    ),
    users={
        "U0101": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['lidar/frames', 'kinect/color-masked/frames'],
        ),
        "U0102": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['lidar/frames', 'kinect/color-masked/frames'],
        ),
        "U0103": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0104": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0105": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0106": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0107": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0108": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0109": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0110": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0111": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0201": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0202": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0203": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0204": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0205": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['kinect/color-masked/frames'],
        ),
        "U0206": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0207": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0208": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0209": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0210": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
    },
    streams={
        "zenodo": [
            "annotation/openpack-actions",
            "annotation/openpack-actions-1hz",
            "annotation/openpack-operations",
            "annotation/openpack-operations-1hz",
            "annotation/openpack-outliers",
            "atr/atr01",
            "atr/atr02",
            "atr/atr03",
            "atr/atr04",
            "e4/e401/acc",
            "e4/e401/bvp",
            "e4/e401/eda",
            "e4/e401/temp",
            "e4/e402/acc",
            "e4/e402/bvp",
            "e4/e402/eda",
            "e4/e402/temp",
            "kinect/2d-kpt/mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2/single",
            "kinect/3d-kpt/none",
            "kinect/3d-kpt/single-ffill-flip-fixed",
            "system/order-sheet",
            "system/ht",
            "system/printer",
        ],
        "googleDrive": [
            "kinect/depth/frames",
            "rs02/depth/frames",
            "lidar/frames",
        ],
        "googleDriveRGB": [
            "kinect/color-masked/frames",
        ],
    },
)
