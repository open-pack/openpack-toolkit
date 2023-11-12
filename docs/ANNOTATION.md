# Activity Class Definitions

1. `OPENPACK_OPERATIONS`
1. `OPENPACK_ACTIONS`
1. `OPENPACK_OUTLIERS`

## [1] `OPENPACK_OPERATIONS`

- Class Name: `openpack_toolkit.OPENPACK_OPERATIONS`
- Config (YAML): [configs/dataset/annotation/openpack-operations.yaml](../configs/dataset/annotation/openpack-operations.yaml)

### 1-1: Activity Classes

| ID | Operation | Description | ignore |
|----|------|-------------|--------|
| 100 | Picking | Check the order-sheet and go to the back table to pick up the items. |  |
| 200 | Relocate Item Label | Peel off the label from the items and place it on the bottom margin of the order sheet. Check the item names and quantity on the list and label with a ballpoint pen. (When picking is done in one round trip, this action is set as the beginning of the box.) |  |
| 300 | Assemble Box | Assemble cardboard boxes that match the size of the items. |  |
| 400 | Insert Items | Put the goods into the box. Fill the box with air cushion. |  |
| 500 | Close Box | Close the box with craft tape. |  |
| 600 | Attach Box Label | Attach the box number label to the side of the box. |  |
| 700 | Scan Label | Scan barcodes with the handy scanner in the following order: (1) order sheet, (2) box number sticker, (3) item label. Then press the "ESC" button on the handy scanner twice. Next, scan barcodes with the scanner of the label printer in the following order: (1) order sheet, (2) code on the label printer. |  |
| 800 | Attach Shipping Label | Attach the shipping label printed out from the label printer to the box. |  |
| 900 | Put on Back Table | Move the completed packing box under the back table. |  |
| 1000 | Fill out Order | Write their signatures in the confirmation column of the order sheet and insert it into the tray for completed order sheets. |  |
| 8100 | Null | For the operation label, ID8200 is translated into this label (ID8100). | True |

---

## [2] `OPENPACK_ACTIONS`

- Class Name: `openpack_toolkit.configs.dataset.annotation.OPENPACK_ACTIONS`
- Config (YAML): [configs/dataset/annotation/openpack-actions.yaml](../configs/dataset/annotation/openpack-actions.yaml)

### 2-1: Activity Classes

| ID | Operation | Action | Description | ignore |
|----|-----------|------|-------------|--------|
| 101 | Picking | Pick Up Sheet | Pick up order sheet from the workbench. |  |
| 103 | Picking | Pick Up Item from Box | Pick items out of a box that contains items picked in batches. |  |
| 107 | Picking | Pick Up Box Sheet | Pick up an order sheet and packed boxes at the same time. (This label is used for moving packed boxes and picking items for the next box at the same time.) |  |
| 108 | Picking | Walk to Work Bench | Lift the item and turn back toward the workbench. (When picking is done in one round trip, this action is set as the beginning of the box.) |  |
| 109 | Picking | Put Packed Box | Go to the back table and place the packed box under the table. |  |
| 201 | Relocate Item Label | Remove Item Label | Remove the sticker with the barcode from the each item. |  |
| 202 | Relocate Item Label | Attach to Order Sheet | Attach the label on the bottom margin of the order sheet. |  |
| 203 | Relocate Item Label | Hold Pen |  |  |
| 204 | Relocate Item Label | Write Check Mark | The subject's checkes items name and quantity.  |  |
| 205 | Relocate Item Label | Put Item Small Bag | Insert small items (<10cm) into the small paper bag and close it with tape. The action is almost the same as ID0404 but the timing is different. |  |
| 301 | Assemble Box | Pick Cardboard | Select and pick up boxes that match the size of the items. |  |
| 302 | Assemble Box | Bend Flap | Bend "bottom" 4 flaps of the box. |  |
| 303 | Assemble Box | Attach Tape | Apply craft tape to close the "bottom" of the box. |  |
| 304 | Assemble Box | Turn Over Box | Turn the box upside down so that the side with the craft tape is on the bottom. |  |
| 305 | Assemble Box | Pick Up Assembled Box | Pick up a pre-assembled box. (Used in Scenario.3-5) |  |
| 401 | Insert Items | Insert Item into Box | Subject grabs individual items and inserts them in the assembled box |  |
| 402 | Insert Items | Air Cushion | Insert air cushion to the box. |  |
| 403 | Insert Items | Separate Air Cushion | Tear off the connected cushioning. |  |
| 404 | Insert Items | Put Item Small Bag | Insert small items (<10cm) into the small paper bag and close it with tape. The action is almost the same as ID0205 but the timing is different. |  |
| 501 | Close Box | Bend Flap | Bend 4 flaps in the upper side of the box. |  |
| 502 | Close Box | Attach Tape | Close the box with craft tape. |  |
| 601 | Attach Box Label | Attach Box Label | Place the box number label on the side of the box. |  |
| 701 | Scan Label | Pick Up HT | Pick up handy scanner (HT). |  |
| 702 | Scan Label | Scan Order Sheet | Scan the order ID code in the upper left corner of the order sheet. |  |
| 703 | Scan Label | Scan Box | Scan  the box number label. |  |
| 704 | Scan Label | Scan Item | Scan each item number on the label on the order sheet one by one. |  |
| 705 | Scan Label | Hold Scanner | Pick up white scanner (for label printer). |  |
| 706 | Scan Label | Scan Order Sheet | Scan the order ID code in the upper left corner of the order sheet with the white scanner. |  |
| 707 | Scan Label | Scan Printer | Scan the code on the label printer to print out sheiiping labels. |  |
| 801 | Attach Shipping Label | Pick Up Shipping Label | Pick up shipping label from the label printer. |  |
| 802 | Attach Shipping Label | Attach Shipping Label | Attach the printed shipping label to the upper side of the box. |  |
| 901 | Put on Back Table | Pick Up Packed Box | Pick up prepared box from the workbench. |  |
| 902 | Put on Back Table | Put Packed Box | Go to the back table and place the packed box under the table. |  |
| 1001 | Fill out Order | Pick Up Pen | The subject's hand touches the pen. |  |
| 1002 | Fill out Order | Write Sign | Sign each field in the column next to the item list on the order sheet. |  |
| 1003 | Fill out Order | Push Order Sheet into Tray | Insert order sheet into the tray for completed order sheets. |  |
| 8101 | Null | Others |  | True |
| 8102 | Null | System Error |  | True |
| 8103 | Null | Ignore |  | True |
| 8104 | Null | Unknown |  | True |
| 8105 | Null | Null | Segment without any specific actions. This class is prepared for action detection. |  |
| 8106 | Null | Exclude | Segments with this label should be excluded from evaluation. This class is prepared for action detection. | True |
| 8201 | System Error | System Error |  | True |

---

## [3] `OPENPACK_OUTLIERS` (Outlier Event Definition)

- Class Name: `openpack_toolkit.configs.dataset.annotation.OPENPACK_OUTLIERS`
- Config (YAML): [configs/dataset/annotation/openpack-outliers.yaml](../configs/dataset/annotation/openpack-outliers.yaml)

### 3-1: Activity Classes

| ID | Category | Event | Tags | ignore | Note |
|----|----------|-------|------|--------|------|
| Aa01 | Incident | Others | LOW, HIGH, Single,  |  | |
| Aa02 | Incident | Miss | LOW, HIGH, Single,  |  | |
| Aa03 | Incident | Accident | LOW, HIGH, Single,  |  | |
| Aa04 | Incident | System Error |  |  | |
| Aa05 | Incident | Talk to Staff |  |  | |
| Aa06 | Incident | Break Label |  |  | |
| Aa07 | Incident | Wrong Choice of Box Size | S, M, L, LL,  |  | |
| Ab01 | Investigation | Others | LOW, HIGH,  |  | |
| Ab02 | Investigation | System Error |  |  | |
| Ab03 | Investigation | Check Box Size | Item, Box-Close, Box-Open, Box-In,  |  | |
| Ab04 | Investigation | Check Item Size |  |  | |
| Ab05 | Investigation | Talk to Staff |  |  | |
| Ac01 | Recovery | Others | LOW, HIGH,  |  | |
| Ac02 | Recovery | System Error |  |  | |
| Ac03 | Recovery | Take out Inserted Items from Box |  |  | |
| Ac04 | Recovery | Put Away Box for Resizing | S, M, L, LL,  |  | |
| Ac05 | Recovery | Disassemble Box for Resizing | S, M, L, LL,  |  | |
| Ac06 | Recovery | Fold Box to Clean Up |  |  | |
| Ac07 | Recovery | Return Box |  |  | |
| Ac08 | Recovery | Talk to Staff |  |  | |
| Ac09 | Recovery | Item Label |  |  | |
| Bx01 | Struggling | Others | LOW, HIGH,  |  | |
| Bx02 | Struggling | Look for Items |  |  | |
| Bx03 | Struggling | Label | Item, Box, Shipping,  |  | |
| Bx04 | Struggling | Scan | HT, LP,  |  | |
| Bx05 | Struggling | Air Cushion |  |  | |
| Bx06 | Struggling | Insert Items |  |  | |
| Bx07 | Struggling | Tape |  |  | |
| Cx01 | Confused | Others | LOW, HIGH,  |  | |
| Cx02 | Confused | Box Size |  |  | |
| Cx03 | Confused | Air Cushion |  |  | |
| Cx04 | Confused | Process |  |  | |
| Cx05 | Confused | Double Check |  |  | |
| Dx01 | Parallel | Others | LOW, HIGH,  |  | |
| Dx02 | Parallel | Action&Action | 0101*1003, 0108*0201, 0302*0303, 0303*0304, 0303*0401, 0303*0501, 0401*0403, 0706*1001, 0707*1001, 0801*1003, 1002*1003,  |  | |
| Dx03 | Parallel | Left&Right |  |  | |
| Dx04 | Parallel | Holding |  |  | |
| Dx03 | Parallel | Action&Additional | 0101*G06, 0108*G06, 0301*B03, 0301*G05, 0301*G06, 0303*0304*G07, 0303*G06, 0304*G07, 0401*G07, 0401*G08, 0502*G07, 0502*G08, 0601*G03, 0601*G08, 0701*G06, 0701*G08, 0702*G06, 0703*G08, 0704*G08, 0707*G06, 0707*G08, 0801*G03, 0801*G06, 0801*G08, 0901*G06, 1001*G06, 1003*G06,  |  | |
| Dx04 | Parallel | Action&Others | 107, 030, 109, 011, 001,  |  | |
| Dx05 | Parallel | Additional&Additional | B01*G07, C03*C04, G06*G08, G03*G06,  |  | |
| Dx06 | Parallel | Additional&Others |  |  | |
| Ex01 | Additional | Others | LOW, HIGH,  |  | |
| Ex02 | Additional | Talk to Staff |  |  | |
| Ex03 | Additional | Dispose |  |  | |
| Ex04 | Additional | Operation |  |  | |
| Ex05 | Additional | Refill Boxe Stock | S-D, S, M, L, LL,  |  | |
| Ex06 | Additional | Clean Up the Workbench |  |  | |
| Ex07 | Additional | Lift Up Box |  |  | |
| Ex08 | Additional | Move Box |  |  | |
| Fx01 | Fraction | Others | LOW, MID, HIGH,  |  | |
