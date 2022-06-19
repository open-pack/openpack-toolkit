# Recommended Data Split (Train / Val / Test / Submission)

1. `debug`
1. `pilot-challenge`

## [1] Debug

This split is for debugging. The used sequence for each section is small.

- Config File: [debug.yaml](../configs/dataset/split/debug.yaml)
- Python Class: [`openpack_toolkit.configs.datasets.splits.DEBUG_SPLIT`](../openpack_toolkit/configs/datasets/splits.py)

| # | Usage |User | Session | 
|---|-------|------|---------|
| 1 | TRAIN | U0102 | S0100 |
| 2 | TRAIN | U0102 | S0200 |
| 3 | TRAIN | U0102 | S0300 |
|  |  |  |  |
| 1 | VAL | U0102 | S0400 |
|  |  |  |  |
| 1 | TEST | U0102 | S0500 |
|  |  |  |  |
| 1 | SUBMISSION | U0102 | S0500 |

## [2] Pilot Challenge

This split is for OpenPack Pilot Challenge (private competition).

- Config File: [pilot-challenge.yaml](../configs/dataset/split/pilot-challenge.yaml)
- Python Class: [`openpack_toolkit.configs.datasets.splits.PILOT_CHALLENGE_SPLIT`](../openpack_toolkit/configs/datasets/splits.py)

| # | Usage |User | Session | 
|---|-------|------|---------|
| 1 | TRAIN | U0102 | S0100 |
| 2 | TRAIN | U0102 | S0200 |
| 3 | TRAIN | U0102 | S0300 |
| 4 | TRAIN | U0102 | S0400 |
| 5 | TRAIN | U0102 | S0500 |
| 6 | TRAIN | U0103 | S0100 |
| 7 | TRAIN | U0103 | S0200 |
| 8 | TRAIN | U0103 | S0300 |
| 9 | TRAIN | U0103 | S0400 |
| 10 | TRAIN | U0103 | S0500 |
| 11 | TRAIN | U0105 | S0100 |
| 12 | TRAIN | U0105 | S0200 |
| 13 | TRAIN | U0105 | S0300 |
| 14 | TRAIN | U0105 | S0400 |
| 15 | TRAIN | U0105 | S0500 |
|  |  |  |  |
| 1 | VAL | U0106 | S0200 |
| 2 | VAL | U0106 | S0400 |
|  |  |  |  |
| 1 | TEST | U0106 | S0100 |
| 2 | TEST | U0106 | S0300 |
| 3 | TEST | U0106 | S0500 |
|  |  |  |  |
| 1 | SUBMISSION | U0107 | S0100 |
| 2 | SUBMISSION | U0107 | S0200 |
| 3 | SUBMISSION | U0107 | S0300 |
| 4 | SUBMISSION | U0107 | S0400 |
| 5 | SUBMISSION | U0107 | S0500 |

