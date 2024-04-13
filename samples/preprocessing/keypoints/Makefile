OPENPACK_ROOT_DIR := ../../openpack/v1.0.0
OUTPUT_DIR := ./build
USER := U0209
SESSION := S0500

OPERATION_LABEL_PATH := ${OPENPACK_ROOT_DIR}/${USER}/annotation/openpack-operations/${SESSION}.csv
ACTION_LABEL_PATH := ${OPENPACK_ROOT_DIR}/${USER}/annotation/openpack-actions/${SESSION}.csv

.PHONY: build
build: build-2d-kpt build-3d-kpt

# ============================
#  Add Labels to 2D Keypoints
# ============================
KEYPOINTS_KINECT_2D_PATH := ${OPENPACK_ROOT_DIR}/${USER}/kinect/2d-kpt/mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2/single/${SESSION}.json
OUTPUT_KINECT_2D_PATH := ${OUTPUT_DIR}/kinect-2d-kpt/${USER}-${SESSION}.csv

.PHONY: build-2d-kpt
build-2d-kpt:
	mkdir -p ${OUTPUT_DIR}
	poetry run python build_kinect_2d_kpt_with_labels.py \
		--kinect-2d-keypoints-path ${KEYPOINTS_KINECT_2D_PATH} \
		--operation-labels-path ${OPERATION_LABEL_PATH} \
		--action-labels-path ${ACTION_LABEL_PATH} \
		--output-path ${OUTPUT_KINECT_2D_PATH}


# ============================
#  Add Labels to 3D Keypoints
# ============================
KEYPOINTS_KINECT_3D_PATH := ${OPENPACK_ROOT_DIR}/${USER}/kinect/3d-kpt/single-ffill-flip-fixed/${SESSION}.csv
OUTPUT_KINECT_3D_PATH := ${OUTPUT_DIR}/kinect-3d-kpt/${USER}-${SESSION}.csv


.PHONY: build-3d-kpt
build-3d-kpt:
	mkdir -p ${OUTPUT_DIR}
	poetry run python build_kinect_3d_kpt_with_labels.py \
		--kinect-3d-keypoints-path ${KEYPOINTS_KINECT_3D_PATH} \
		--operation-labels-path ${OPERATION_LABEL_PATH} \
		--action-labels-path ${ACTION_LABEL_PATH} \
		--output-path ${OUTPUT_KINECT_3D_PATH}


.PHONY: clean
clean:
	rm -rf ${OUTPUT_DIR}
