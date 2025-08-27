# ---------------------------------------------------------------------
# Gufo Liftbridge: liftbridge fixture
# ---------------------------------------------------------------------
# Copyright (C) 2023-25, Gufo Labs
# See LICENSE.md for details
# ---------------------------------------------------------------------

# Python modules
import logging
from typing import Iterator

# Third-party modules
import pytest

# Gufo Liftbridge modules
from gufo.liftbridge.liftbridge import Liftbridge


@pytest.fixture(scope="session")
def liftbridge() -> Iterator[Liftbridge]:
    logger = logging.getLogger("gufo.liftbridge.liftbridge")
    logger.setLevel(logging.DEBUG)
    with Liftbridge() as liftbridge:
        yield liftbridge
