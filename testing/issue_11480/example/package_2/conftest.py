# package_2/conftest.py

import pytest

@pytest.fixture(autouse=True, scope="package")
def some_fixture2():
    print("\n------------Setup package 2")

    yield

    print("\n------------Teardown package 2")