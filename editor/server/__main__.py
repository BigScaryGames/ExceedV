"""Run the editor server: python -m editor.server (from the repo root)."""
import uvicorn

from .main import app


def main() -> None:
    uvicorn.run(app, host="127.0.0.1", port=8787, log_level="warning")


if __name__ == "__main__":
    main()
