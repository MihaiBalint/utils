import datetime
import logging
import tempfile
import pytest

@pytest.fixture
def mock_datetime():
    return datetime.datetime(year=2019, month=8, day=29)

