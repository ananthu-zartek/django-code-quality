# Django code quality example

Install the project's runtime dependencies and the separate quality tools:

```sh
python -m pip install -r requirements.txt
python -m pip install -r quality_requirements.txt
```

In another Django project, keep its own `requirements.txt` and add `quality_requirements.txt` alongside it. Install both files in CI. The quality file contains Ruff, Mypy, and Django typing stubs; it does not replace the project's runtime dependencies.

The example endpoint is `GET /api/health/`. It returns `{"status": "ok"}`.
`GET /api/checks/` returns `{"status": "ok", "checks": 1}`.

## Ruff pull request demonstration

The `Quality` GitHub Actions workflow runs on pull requests to `main` or `master`. `core/views.py` deliberately contains an unused `json` import. In a pull request containing this change, the **Run Ruff** step fails with `F401` and points to that import:

```text
F401 `json` imported but unused
 --> core/views.py:1:8
```

## Mypy pull request demonstration

The `checks` endpoint deliberately declares its response payload as `dict[str, str]` while giving `checks` an integer value. After the Ruff import is fixed, the **Run Mypy** step reports a `dict-item` error in `core/views.py`. The endpoint still returns a valid JSON response, so its test passes.

## Run and fix checks locally

Run the same checks as CI:

```sh
python -m ruff check .
python -m ruff format --check .
python -m mypy .
python manage.py check
python manage.py test
```

Use Ruff's fix commands when a lint or formatting check fails:

```sh
python -m ruff check . --fix
python -m ruff format .
```

Then rerun `python -m ruff check .` and `python -m ruff format --check .` to confirm the fixes. Ruff's autofix removes the unused `json` import in this example. Mypy errors require a code change: change the `checks` payload annotation in `core/views.py` to `dict[str, str | int]`, then rerun `python -m mypy .`. Push the fixes to update the pull request checks.
