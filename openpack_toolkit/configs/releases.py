from ._schema import ReleaseConfig

RELEASE_CONFIG_V0_2_0 = ReleaseConfig(
    version="v0.2.0",
    url="https://zenodo.org/record/6697990",
    users={
        "U0102": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0103": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0105": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0106": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
    },
    streams={
        "atr": {
            "repository": "zenodo",
            "subdirs": "${.devices}",
            "devices": [
                "atr01",
                "atr02",
                "atr03",
                "atr04"
            ]
        },
        "kinect": {
            "2d-kpt": {
                "repository": "zenodo",
                "subdirs": [
                    {
                        "name": "${.model}",
                        "category": "2d-kpt",
                        "model": "mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2",
                        "subdir": "single",
                        "fname": "kinect-2d-kpt"
                    }
                ]
            }
        },
        "annotation": {
            "repository": "zenodo",
            "subdirs": [
                "openpack-operations"
            ]
        }
    },
)


RELEASE_CONFIG_V0_2_1 = ReleaseConfig(
    version="v0.2.1",
    url="None",
    users={
        "U0102": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0103": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0105": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0106": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0107": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
    },
    streams={
        "atr": {
            "repository": "zenodo",
            "subdirs": "${.devices}",
            "devices": [
                "atr01",
                "atr02",
                "atr03",
                "atr04"
            ]
        },
        "kinect": {
            "2d-kpt": {
                "repository": "zenodo",
                "subdirs": [
                    {
                        "name": "${.model}",
                        "category": "2d-kpt",
                        "model": "mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2",
                        "subdir": "single",
                        "fname": "kinect-2d-kpt"
                    }
                ]
            }
        },
        "annotation": {
            "repository": "zenodo",
            "subdirs": [
                "openpack-operations"
            ]
        }
    },
)
