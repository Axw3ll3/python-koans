import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))


def pytest_collection_modifyitems(items):
    items.sort(key=lambda item: (str(item.fspath), item.location[1] or 0))
