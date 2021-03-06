# -*- Mode: Python -*- vi:si:et:sw=4:sts=4:ts=4:syntax=python
#
# Copyright (c) 2015, Thibault Saunier <thibault.saunier@collabora.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
# Boston, MA 02110-1301, USA.


import subprocess
from launcher import utils

SYNC_ASSETS_COMMAND = "git fetch origin && git checkout origin/master && git annex get ."

def update_assets(assets_dir):
    try:
        utils.launch_command("cd %s && %s" % (assets_dir, SYNC_ASSETS_COMMAND),
                             fails=True)

    except subprocess.CalledProcessError as e:
        utils.printc("Could not update assets repository\n\nError: %s"
                     "\n\nMAKE SURE YOU HAVE git-annex INSTALLED!" % (e),
                     utils.Colors.FAIL, True)

        return False

    return True
