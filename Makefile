.PHONY: install test lint run
install:
	python -m pip install -e '.[dev]'
test:
	python -m pytest -q
lint:
	python -m compileall -q apps/api/src
run:
	uvicorn crip_api.main:app --reload
