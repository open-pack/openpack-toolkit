# Preprocessed Dataset - Keypoints

## Build `kinect-2d-kpt-with-operation-action-label`

This preprocessed dataset contains 2d keypoints (`kinect-2d-kpt`), work operation labels, and action labels in a single CSV.
Here is a command to build this dataset with sample data.

```bash
python build_kinect_2d_kpt_with_labels.py \
        --kinect-2d-keypoints-path ../../openpack/v1.0.0/U0209/kinect/2d-kpt/mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2/single/S0500.json \
        --operation-labels-path ../../openpack/v1.0.0/U0209/annotation/openpack-operations/S0500.csv \
        --action-labels-path ../../openpack/v1.0.0/U0209/annotation/openpack-actions/S0500.csv \
        --output-path ./build/U0209-S0500.csv
```

or

```bash
make build-2d-kpt
```

## Build `kinect-3d-kpt-with-operation-action-label`

This preprocessed dataset contains 3d keypoints (`kinect-3d-kpt`), work operation labels, and action labels in a single CSV.
Here is a command to build this dataset with sample data.

```bash
poetry run python build_kinect_3d_kpt_with_labels.py \
        --kinect-3d-keypoints-path ../../openpack/v1.0.0/U0209/kinect/3d-kpt/single-ffill-flip-fixed/S0500.csv \
        --operation-labels-path ../../openpack/v1.0.0/U0209/annotation/openpack-operations/S0500.csv \
        --action-labels-path ../../openpack/v1.0.0/U0209/annotation/openpack-actions/S0500.csv \
        --output-path ./build/kinect-3d-kpt/U0209-S0500.csv
```

or

```bash
make build-3d-kpt
```