OPENPACK_ROOT_DIR := ../../openpack/v1.0.0
OUTPUT_DIR := ./build
USER := U0209
SESSION := S0500

KEYPOINTS_PATH := ${OPENPACK_ROOT_DIR}/${USER}/kinect/2d-kpt/mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2/single/${SESSION}.json
OPERATION_LABEL_PATH := ${OPENPACK_ROOT_DIR}/${USER}/annotation/openpack-operations/${SESSION}.csv
ACTION_LABEL_PATH := ${OPENPACK_ROOT_DIR}/${USER}/annotation/openpack-actions/${SESSION}.csv
OUTPUT_PATH := ${OUTPUT_DIR}/${USER}-${SESSION}.csv


.PHONY: build
build:
	mkdir -p ${OUTPUT_DIR}
	poetry run python build_kinect_2d_kpt_with_labels.py \
		--kinect-2d-keypoints-path ${KEYPOINTS_PATH} \
		--operation-labels-path ${OPERATION_LABEL_PATH} \
		--action-labels-path ${ACTION_LABEL_PATH} \
		--output-path ${OUTPUT_PATH}

.PHONY: clean
clean:
	rm -rf ${OUTPUT_DIR}
