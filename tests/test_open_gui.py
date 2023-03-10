# Copyright 2023 IRT Saint Exupéry, https://www.irt-saintexupery.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License version 3 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# Contributors:
#    INITIAL AUTHORS - API and implementation and/or documentation
#        :author: Francois Gallard
#    OTHER AUTHORS   - MACROSCOPIC CHANGES
from __future__ import annotations

from subprocess import call
from subprocess import TimeoutExpired

import pytest


def test_cmd():
    """Tests that the entry point works."""
    with pytest.raises(
        TimeoutExpired,
        match="Command 'gemseo-template-grammar-editor' timed out after 1.0 seconds",
    ):
        # This ensures that the GUI is openned, stays opens 1 second, and then
        # closed by the timeout, otherwise it would raise a FileNotFoundError.
        call("gemseo-template-grammar-editor", timeout=1.0)
