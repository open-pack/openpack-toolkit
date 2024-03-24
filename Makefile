.PHONY: tests
tests:
	poetry run pytest -v \
		tests \
		samples/preprocessing/keypoints/tests
		

