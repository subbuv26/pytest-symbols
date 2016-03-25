# Copyright 2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
pytest_symbols.plugin
~~~~~~~~~~~~~~~~~~~~~
This module defines the pytest hooks implemented by pytest_symbols.

"""


import pytest

from . import models


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption(
        "--symbols",
        action="store",
        metavar="path",
        help="path for test environment symbols file"
    )
    parser.addini(
        "symbols",
        type="linelist",
        help="each line specifies the path to a test environment symbols file"
    )


def pytest_configure(config):
    if config.option.symbols:
        config._symbols = models.Symbols(config.option.symbols)


@pytest.fixture(scope="session", autouse=True)
def symbols(request):
    symbols = getattr(request.config, "_symbols", None)

    def teardown():
        symbols = None

    request.addfinalizer(teardown)
    return symbols