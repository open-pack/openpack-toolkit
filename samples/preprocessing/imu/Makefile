OPENPACK_ROOT_DIR := ../../openpack/v1.0.0
OUTPUT_DIR := ./build
USER := U0209
SESSION := S0500

# ========
#  Common
# ========
OPERATION_LABEL_PATH := ${OPENPACK_ROOT_DIR}/${USER}/annotation/openpack-operations/${SESSION}.csv
ACTION_LABEL_PATH := ${OPENPACK_ROOT_DIR}/${USER}/annotation/openpack-actions/${SESSION}.csv

.PHONY: build
build: build-imu

.PHONY: clean
clean:
	rm -rf ${OUTPUT_DIR}


# ============================
#  Add Labels to IMU dataset
# ============================
ATR_QAGS_PREPROC_DATASET_NAME := imu-with-operation-action-labels
ATR_QAGS_PATH := ${OPENPACK_ROOT_DIR}/${USER}/atr/
OUTPUT_ATR_QAGS_PATH := ${OUTPUT_DIR}/${ATR_QAGS_PREPROC_DATASET_NAME}/${USER}-${SESSION}.csv

.PHONY: build-imu
build-imu:
	poetry run python build_imu_with_labels.py \
		--atr-root-dir ${ATR_QAGS_PATH} \
		--session ${SESSION} \
		--operation-labels-path ${OPERATION_LABEL_PATH} \
		--action-labels-path ${ACTION_LABEL_PATH} \
		--output-path ${OUTPUT_ATR_QAGS_PATH}


.PHONY: zip-imu
zip-imu:
	poetry run python ../keypoints/create_zip.py \
		--dataset-dir ${OUTPUT_DIR}/${ATR_QAGS_PREPROC_DATASET_NAME}
