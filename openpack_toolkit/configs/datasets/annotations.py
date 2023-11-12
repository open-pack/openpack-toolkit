from .._schema import AnnotConfig, Label, Metadata, DataLocation


OPENPACK_ACTIONS = (
    Label(
        id=101,
        name="Pick Up Sheet",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=103,
        name="Pick Up Item from Box",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=107,
        name="Pick Up Box Sheet",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=108,
        name="Walk to Work Bench",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=109,
        name="Put Packed Box",
        version="v3.3.0",
        is_ignore=False,
    ),
    Label(
        id=201,
        name="Remove Item Label",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=202,
        name="Attach to Order Sheet",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=203,
        name="Hold Pen",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=204,
        name="Write Check Mark",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=205,
        name="Put Item Small Bag",
        version="v3.4.0",
        is_ignore=False,
    ),
    Label(
        id=301,
        name="Pick Cardboard",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=302,
        name="Bend Flap",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=303,
        name="Attach Tape",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=304,
        name="Turn Over Box",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=305,
        name="Pick Up Assembled Box",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=401,
        name="Insert Item into Box",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=402,
        name="Air Cushion",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=403,
        name="Separate Air Cushion",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=404,
        name="Put Item Small Bag",
        version="v3.4.0",
        is_ignore=False,
    ),
    Label(
        id=501,
        name="Bend Flap",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=502,
        name="Attach Tape",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=601,
        name="Attach Box Label",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=701,
        name="Pick Up HT",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=702,
        name="Scan Order Sheet",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=703,
        name="Scan Box",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=704,
        name="Scan Item",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=705,
        name="Hold Scanner",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=706,
        name="Scan Order Sheet",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=707,
        name="Scan Printer",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=801,
        name="Pick Up Shipping Label",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=802,
        name="Attach Shipping Label",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=901,
        name="Pick Up Packed Box",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=902,
        name="Put Packed Box",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=1001,
        name="Pick Up Pen",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=1002,
        name="Write Sign",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=1003,
        name="Push Order Sheet into Tray",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=8101,
        name="Others",
        version="v3.2.2",
        is_ignore=True,
    ),
    Label(
        id=8102,
        name="System Error",
        version="v3.2.2",
        is_ignore=True,
    ),
    Label(
        id=8103,
        name="Ignore",
        version="v3.2.2",
        is_ignore=True,
    ),
    Label(
        id=8104,
        name="Unknown",
        version="v3.2.2",
        is_ignore=True,
    ),
    Label(
        id=8105,
        name="Null",
        version="v3.5.0",
        is_ignore=False,
    ),
    Label(
        id=8106,
        name="Exclude",
        version="v3.5.0",
        is_ignore=True,
    ),
    Label(
        id=8201,
        name="System Error",
        version="v3.2.2",
        is_ignore=True,
    ),
)


OPENPACK_OPERATIONS = (
    Label(
        id=100,
        name="Picking",
        version="v3.0.0",
        is_ignore=False,
    ),
    Label(
        id=200,
        name="Relocate Item Label",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=300,
        name="Assemble Box",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=400,
        name="Insert Items",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=500,
        name="Close Box",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=600,
        name="Attach Box Label",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=700,
        name="Scan Label",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=800,
        name="Attach Shipping Label",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=900,
        name="Put on Back Table",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=1000,
        name="Fill out Order",
        version="v3.2.2",
        is_ignore=False,
    ),
    Label(
        id=8100,
        name="Null",
        version="v3.2.2",
        is_ignore=True,
    ),
)


OPENPACK_OUTLIERS = (
    Label(
        id="Aa01",
        name="Incident / Others",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Aa02",
        name="Incident / Miss",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Aa03",
        name="Incident / Accident",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Aa04",
        name="Incident / System Error",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Aa05",
        name="Incident / Talk to Staff",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Aa06",
        name="Incident / Break Label",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Aa07",
        name="Incident / Wrong Choice of Box Size",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ab01",
        name="Investigation / Others",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ab02",
        name="Investigation / System Error",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ab03",
        name="Investigation / Check Box Size",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ab04",
        name="Investigation / Check Item Size",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ab05",
        name="Investigation / Talk to Staff",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ac01",
        name="Recovery / Others",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ac02",
        name="Recovery / System Error",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ac03",
        name="Recovery / Take out Inserted Items from Box",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ac04",
        name="Recovery / Put Away Box for Resizing",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ac05",
        name="Recovery / Disassemble Box for Resizing",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ac06",
        name="Recovery / Fold Box to Clean Up",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ac07",
        name="Recovery / Return Box",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ac08",
        name="Recovery / Talk to Staff",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ac09",
        name="Recovery / Item Label",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Bx01",
        name="Struggling / Others",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Bx02",
        name="Struggling / Look for Items",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Bx03",
        name="Struggling / Label",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Bx04",
        name="Struggling / Scan",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Bx05",
        name="Struggling / Air Cushion",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Bx06",
        name="Struggling / Insert Items",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Bx07",
        name="Struggling / Tape",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Cx01",
        name="Confused / Others",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Cx02",
        name="Confused / Box Size",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Cx04",
        name="Confused / Process",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Cx05",
        name="Confused / Double Check",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Dx01",
        name="Parallel / Others",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Dx02",
        name="Parallel / Action&Action",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Dx03",
        name="Parallel / Action&Additional",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Dx04",
        name="Parallel / Action&Others",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Dx05",
        name="Parallel / Additional&Additional",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Dx06",
        name="Parallel / Additional&Others",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ex01",
        name="Additional / Others",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ex02",
        name="Additional / Talk to Staff",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ex03",
        name="Additional / Dispose",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ex05",
        name="Additional / Refill Boxe Stock",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ex06",
        name="Additional / Clean Up the Workbench",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ex07",
        name="Additional / Lift Up Box",
        version="v1.4.0",
        is_ignore=False,
    ),
    Label(
        id="Ex08",
        name="Additional / Move Box",
        version="v1.4.0",
        is_ignore=False,
    ),
)


OPENPACK_ACTIONS_ANNOTATION = AnnotConfig(
    kind="dataset/annotation/csv",
    name="openpack-actions",
    metadata=Metadata(
        labels={
            "type": "annotation/action",
            "version": "v3.5.0",
            "dependency": "None",
            "resolution": "original",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/annotation/openpack-actions",
        fname="${session}.csv",
    ),
    classes=OPENPACK_ACTIONS,
)

OPENPACK_ACTIONS_1HZ_ANNOTATION = AnnotConfig(
    kind="dataset/annotation/csv/sequence",
    name="openpack-actions-1hz",
    metadata=Metadata(
        labels={
            "type": "annotation/action",
            "version": "v3.5.0",
            "dependency": "openpack-actions",
            "resolution": "1Hz",
            "label_format": "soft-target",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/annotation/openpack-actions-1hz",
        fname="${session}.csv",
    ),
    classes=OPENPACK_ACTIONS,
)

OPENPACK_OPERATIONS_ANNOTATION = AnnotConfig(
    kind="dataset/annotation/csv",
    name="openpack-operations",
    metadata=Metadata(
        labels={
            "type": "annotation/operation",
            "version": "v3.5.0",
            "dependency": "openpack-actions",
            "resolution": "original",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/annotation/openpack-operations",
        fname="${session}.csv",
    ),
    classes=OPENPACK_OPERATIONS,
)

OPENPACK_OPERATIONS_1HZ_ANNOTATION = AnnotConfig(
    kind="dataset/annotation/csv/sequence",
    name="openpack-operations-1hz",
    metadata=Metadata(
        labels={
            "type": "annotation/operation",
            "version": "v3.5.0",
            "dependency": "openpack-operations",
            "resolution": "1Hz",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/annotation/openpack-operations-1hz",
        fname="${session}.csv",
    ),
    classes=OPENPACK_OPERATIONS,
)

OPENPACK_OUTLIERS_ANNOTATION = AnnotConfig(
    kind="dataset/annotation/csv",
    name="openpack-outliers",
    metadata=Metadata(
        labels={
            "type": "annotation/outlier",
            "version": "v1.4.0",
            "dependency": "None",
            "resolution": "original",
        }
    ),
    path=DataLocation(
        dir="${path.openpack.rootdir}/${user.name}/annotation/openpack-outliers",
        fname="${session}.csv",
    ),
    classes=OPENPACK_OUTLIERS,
)
