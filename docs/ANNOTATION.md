# Activity Class Definitions

1. `OPENPACK_OPERATIONS`
1. `OPENPACK_ACTIONS`

## [1] `OPENPACK_OPERATIONS`

- Class Name: `openpack_toolkit.OPENPACK_OPERATIONS`
- Config (YAML): [configs/dataset/annotation/openpack-operations.yaml](../configs/dataset/annotation/openpack-operations.yaml)

### 1-1: Activity Classes

| ID | Name | Description | ignore |
|----|------|-------------|--------|
| 100 | Picking | item picking |  |
| 200 | RelocateItemLabel | relocate label |  |
| 300 | AssembleBox | assemble box |  |
| 400 | InsertItems | insert item |  |
| 500 | CloseBox | close box |  |
| 600 | AttachBoxLabel | attach label |  |
| 700 | ScanLabel | scan label |  |
| 800 | AttachShippingLabel | attach label |  |
| 900 | PutOnRack | put on rack  |  |
| 1000 | Fill-outOrder | fill-out ordersheet |  |
| 8100 | Null |  | True |

### 1-2: File Format

Format: CSV

| # | Column Name | Description |
|---|-------------|-------------|
| 1 | unixtime |  |
| 2 | user |  |
| 3 | session |  |
| 4 | box |  |
| 5 | operation |  |

---

## [2] `OPENPACK_ACTIONS`

- Class Name: `openpack_toolkit.configs.dataset.annotation.OPENPACK_ACTIONS`
- Config (YAML): [configs/dataset/annotation/openpack-actions.yaml](../configs/dataset/annotation/openpack-actions.yaml)

### 2-1: Activity Classes

| ID | Operation | Name | Description | ignore |
|----|-----------|------|-------------|--------|
| 101 | Picking | PickUp-OrderSheet |  |  |
| 102 | Picking | Walk-ToRack |  |  |
| 103 | Picking | PickUp-Item-FromBox |  |  |
| 104 | Picking | Pick-UpOrderSheet&Walk-ToRack-v2 |  |  |
| 105 | Picking | Walk-ToWorkBench-v2 |  |  |
| 106 | Picking | Pick-UpOrderSheet&Walk-ToRack-with-PrevPackedBox-v2 |  |  |
| 201 | RelocateItemLabel | Remove-ItemLabel |  |  |
| 202 | RelocateItemLabel | AttachTo-OrderSheet |  |  |
| 203 | RelocateItemLabel | Hold-Pen |  |  |
| 204 | RelocateItemLabel | Write-CheckMark |  |  |
| 205 | RelocateItemLabel | Put-Item-SmallBack |  |  |
| 206 | RelocateItemLabel | Relocate-ItemLabel-v2 |  |  |
| 207 | RelocateItemLabel | Write-v2 |  |  |
| 301 | AssembleBox | Pick-Cardboard |  |  |
| 302 | AssembleBox | Bend-Flap |  |  |
| 303 | AssembleBox | Attach-Tape |  |  |
| 304 | AssembleBox | TurnOver-Box |  |  |
| 305 | AssembleBox | PickUp-AssembledBox |  |  |
| 306 | AssembleBox | AssembleBox-v2 |  |  |
| 401 | InsertItems | Insert-Item-into-Box |  |  |
| 402 | InsertItems | AirCushion |  |  |
| 403 | InsertItems | Separate-AirCushion |  |  |
| 404 | InsertItems | Put-Item-SmallBack |  |  |
| 405 | InsertItems | Insert-Items-v2 |  |  |
| 501 | CloseBox | Bend-Flap |  |  |
| 502 | CloseBox | Attach-Tape |  |  |
| 503 | CloseBox | CloseBox-v2 |  |  |
| 601 | AttachBoxLabel | Attach-BoxLabel |  |  |
| 602 | AttachBoxLabel | Attach-BoxLabel-v2 |  |  |
| 701 | ScanLabel | PickUp-HT |  |  |
| 702 | ScanLabel | Scan-OrderSheet |  |  |
| 703 | ScanLabel | Scan-Box |  |  |
| 704 | ScanLabel | Scan-Item |  |  |
| 705 | ScanLabel | Hold-Scanner |  |  |
| 704 | ScanLabel | Scan-OrderSheet |  |  |
| 706 | ScanLabel | Scan-Printer |  |  |
| 707 | ScanLabel | HT-v2 |  |  |
| 708 | ScanLabel | Printer-v2 |  |  |
| 801 | AttachShippingLabel | PickUp-ShippingLabel |  |  |
| 802 | AttachShippingLabel | Attach-ShippingLabel |  |  |
| 802 | AttachShippingLabel | Attach-ShippingLabel-v2 |  |  |
| 901 | PutOnRack | PickUp-PackedBox |  |  |
| 902 | PutOnRack | Put-PackedBox |  |  |
| 903 | PutOnRack | Put-OnPack-v2 |  |  |
| 1001 | Fill-outOrder | PickUp-Pen |  |  |
| 1002 | Fill-outOrder | Write-Sign |  |  |
| 1003 | Fill-outOrder | Push-OrderSheet-IntoTray |  |  |
| 1004 | Fill-outOrder | FillOut-v2 |  |  |
| 1005 | Fill-outOrder | Write-v2 |  |  |
| 1006 | Fill-outOrder | Insert-v2 |  |  |
| 8101 | Null | Others |  | True |
| 8102 | Null | SystemError |  | True |
| 8103 | Null | Ignore |  | True |
| 8104 | Null | Unknown |  | True |
| 8201 | SystemError | SystemError |  | True |

### 2-2: File Format

Format: CSV

| # | Column Name | Description |
|---|-------------|-------------|
| 1 | unixtime |  |
| 2 | user |  |
| 3 | session |  |
| 4 | box |  |
| 5 | operation |  |
| 6 | action |  |
