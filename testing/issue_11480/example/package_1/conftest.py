# package_1/conftest.py

import pytest

@pytest.fixture(autouse=True, scope="package")
def some_fixture1():
    print("\n------------Setup package 1")

    yield

    print("\n------------ Teardown package 1")