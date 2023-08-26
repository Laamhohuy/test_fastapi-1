```shell
$ mkdir -p ~/projects/test_fastapi
$ cd projects/test_fastapi
$ python -m venv venv
$ venv/bin/python -m pip install fastapi[all]
$ venv/bin/uvicorn src.main:app --reload
```
