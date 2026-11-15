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
