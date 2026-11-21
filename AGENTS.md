# Repository notes

- This repository contains course assignments; the root README has no setup or test instructions. CI currently targets only `viikko3/login` (`.github/workflows/main.yml`).
- For the login app, work in `viikko3/login`; its Flask entrypoint is `src/index.py`, and Robot browser suites are in `src/tests/`.
- Use Python 3.14 and `uv` in `viikko3/login` (`pyproject.toml` and `uv.lock` require Python >=3.14). Set up and run the full browser suite with:
  ```sh
  uv sync
  uv run rfbrowser install --with-deps chromium
  bash run_robot_tests.sh
  ```
- `run_robot_tests.sh` starts the Flask app on port 5001, waits for it, runs all Robot suites headlessly, then stops the process listening on that port. Do not run it while another service you need is using port 5001.
- To run one suite, start the app with `uv run python3 src/index.py` from `viikko3/login`, then in another shell run `uv run robot --variable HEADLESS:true src/tests/<suite>.robot`; stop the app afterward. For example, `<suite>` can be `login` or `register`.
- For `viikko4/verkkokauppa`, use Python 3.14 and `uv` (`pyproject.toml`/`uv.lock`); run `uv sync` and `uv run pytest` from that directory. The focused test file is `src/tests/kauppa_test.py`; these are unit tests and need no external service.
- In `viikko4/verkkokauppa`, `src/index.py` is a runnable example flow, while the shop components are separate modules under `src/` and tests import them directly.
- For `viikko4/tdd-ostoskori`, use Python 3.14 and `uv`; from that directory run `uv sync` then `uv run pytest` (or focus with `uv run pytest src/tests/ostoskori_test.py`). Tests are `unittest` cases collected by pytest, and the project modules are in `src/`.
- In `viikko4/tdd-ostoskori`, do not change `src/ostos.py`, `src/tuote.py`, or tests unless explicitly asked; implement only the minimal changes needed to pass the tests.
