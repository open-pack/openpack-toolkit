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


RELEASE_CONFIG_V0_3_0 = ReleaseConfig(
    version="v0.3.0",
    url="https://zenodo.org/record/7139262",
    users={
        "U0101": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['lidar/frames'],
        ),
        "U0102": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['lidar/frames'],
        ),
        "U0103": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0104": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400'],
            exclude=['annotation'],
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
            exclude=None,
        ),
        "U0108": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
        "U0109": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
        "U0110": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
        "U0111": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0202": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0203": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['e4', 'annotation'],
        ),
        "U0204": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
        "U0205": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0207": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
        "U0210": ReleaseConfig._User(
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
                    "fname": "activity-1s",
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
            },
            "frames": {
                "repository": "gooogle-drive",
                "zip": "{user}/kinect/{img_type}/frames/{session}.zip",
                "subdirs": [
                    {
                        "name": "${.img_type}",
                        "fname": None,
                        "img_type": "depth"
                    }
                ]
            }
        },
        "rs02": {
            "frames": {
                "repository": "gooogle-drive",
                "zip": "{user}/rs02/{img_type}/frames/{session}.zip",
                "subdirs": [
                    {
                        "name": "${.img_type}",
                        "fname": None,
                        "img_type": "depth"
                    }
                ]
            }
        },
        "lidar": {
            "frames": {
                "repository": "gooogle-drive",
                "zip": "{user}/lidar/frames/{session}.zip",
                "subdirs": [
                    {
                        "name": "pcl",
                        "fname": None
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
                },
                {
                    "name": "printer",
                    "fname": "system-printer"
                }
            ]
        },
        "e4": {
            "repository": "zenodo",
            "zip": "{user}__e4.zip",
            "subdirs": [
                {
                    "name": "${.fname}",
                    "fname": "e4-acc",
                    "subdir": "${device}/acc"
                },
                {
                    "name": "${.fname}",
                    "fname": "e4-bvp",
                    "subdir": "${device}/bvp"
                },
                {
                    "name": "${.fname}",
                    "fname": "e4-eda",
                    "subdir": "${device}/eda"
                },
                {
                    "name": "${.fname}",
                    "fname": "e4-temp",
                    "subdir": "${device}/temp"
                }
            ],
            "devices": [
                "e401",
                "e402"
            ]
        }
    },
)


RELEASE_CONFIG_V0_3_1 = ReleaseConfig(
    version="v0.3.1",
    url="https://zenodo.org/record/7213887",
    users={
        "U0101": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['lidar/frames'],
        ),
        "U0102": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['lidar/frames'],
        ),
        "U0103": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0104": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400'],
            exclude=['annotation'],
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
            exclude=None,
        ),
        "U0108": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
        "U0109": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0110": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
        "U0111": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0202": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0203": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
        "U0204": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
        "U0205": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=None,
        ),
        "U0207": ReleaseConfig._User(
            sessions=['S0100', 'S0200', 'S0300', 'S0400', 'S0500'],
            exclude=['annotation'],
        ),
        "U0210": ReleaseConfig._User(
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
                    "fname": "activity-1s",
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
            },
            "frames": {
                "repository": "gooogle-drive",
                "zip": "{user}/kinect/{img_type}/frames/{session}.zip",
                "subdirs": [
                    {
                        "name": "${.img_type}",
                        "fname": None,
                        "img_type": "depth"
                    }
                ]
            }
        },
        "rs02": {
            "frames": {
                "repository": "gooogle-drive",
                "zip": "{user}/rs02/{img_type}/frames/{session}.zip",
                "subdirs": [
                    {
                        "name": "${.img_type}",
                        "fname": None,
                        "img_type": "depth"
                    }
                ]
            }
        },
        "lidar": {
            "frames": {
                "repository": "gooogle-drive",
                "zip": "{user}/lidar/frames/{session}.zip",
                "subdirs": [
                    {
                        "name": "pcl",
                        "fname": None
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
                },
                {
                    "name": "printer",
                    "fname": "system-printer"
                }
            ]
        },
        "e4": {
            "repository": "zenodo",
            "zip": "{user}__e4.zip",
            "subdirs": [
                {
                    "name": "${.fname}",
                    "fname": "e4-acc",
                    "subdir": "${device}/acc"
                },
                {
                    "name": "${.fname}",
                    "fname": "e4-bvp",
                    "subdir": "${device}/bvp"
                },
                {
                    "name": "${.fname}",
                    "fname": "e4-eda",
                    "subdir": "${device}/eda"
                },
                {
                    "name": "${.fname}",
                    "fname": "e4-temp",
                    "subdir": "${device}/temp"
                }
            ],
            "devices": [
                "e401",
                "e402"
            ]
        }
    },
)
