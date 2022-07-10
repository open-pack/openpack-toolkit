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
        "annotation": {
            "repository": "zenodo",
            "zip": "{user}__annotation.zip",
            "subdirs": [
                {
                    "name": "${.fname}",
                    "fname": "openpack-operations",
                    "is_annotation": True
                }
            ]
        },
        "atr": {
            "repository": "zenodo",
            "zip": "{user}__atr.zip",
            "subdirs": [
                {
                    "name": "${.fname}",
                    "fname": "atr-qags",
                    "subdir": "${device}"
                }
            ],
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
                "zip": "{user}__kinect__2d-kpt.zip",
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
        }
    },
)


RELEASE_CONFIG_V0_2_1 = ReleaseConfig(
    version="v0.2.1",
    url="https://zenodo.org/record/6811369",
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
        "annotation": {
            "repository": "zenodo",
            "zip": "{user}__annotation.zip",
            "subdirs": [
                {
                    "name": "${.fname}",
                    "fname": "openpack-operations",
                    "is_annotation": True
                }
            ]
        },
        "atr": {
            "repository": "zenodo",
            "zip": "{user}__atr.zip",
            "subdirs": [
                {
                    "name": "${.fname}",
                    "fname": "atr-qags",
                    "subdir": "${device}"
                }
            ],
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
                "zip": "{user}__kinect__2d-kpt.zip",
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
        "system": {
            "repository": "zenodo",
            "zip": "{user}__system.zip",
            "subdirs": [
                {
                    "name": "order-sheet",
                    "fname": "system-order-sheet"
                },
                {
                    "name": "ht-original",
                    "fname": "system-ht-original"
                }
            ]
        },
        "e4": {
            "repository": "zenodo",
            "zip": "{user}__e4.zip",
            "subdirs": [
                {
                    "name": "${.fname}",
                    "fname": "e4-all",
                    "subdir": "${device}/${sensor}"
                }
            ],
            "devices": [
                "e401",
                "e402"
            ],
            "sensors": [
                "acc",
                "bvp",
                "eda",
                "temp"
            ]
        }
    },
)
