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
tests.demo
~~~~~~~~~~
This module contains tests for the pytest-symbols plugin demo.

"""


import pytest

from pytest import symbols as foo


class TestDemo(object):

    def test_dont_use_symbols_fixture(self):
        print pytest.symbols
        assert pytest.symbols.client_ip == "1.1.1.1"
        assert pytest.symbols.server_ip == "2.2.2.2"
        print foo
        assert foo.client_ip == "1.1.1.1"
        assert foo.server_ip == "2.2.2.2"

    def test_do_use_symbols_fixture(self, symbols):
        print symbols
        assert symbols.client_ip == "1.1.1.1"
        assert symbols.server_ip == "2.2.2.2"
