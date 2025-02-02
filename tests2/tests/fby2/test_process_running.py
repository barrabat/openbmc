#!/usr/bin/env python
#
# Copyright 2018-present Facebook. All Rights Reserved.
#
# This program file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program in a file named COPYING; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#

from common.base_process_running_test import BaseProcessRunningTest


class ProcessRunningTest(BaseProcessRunningTest):
    def set_processes(self):
        self.expected_process = [
            "fscd",
            "sshd",
            "dhclient -6 -d -D LL -pf /var/run/dhclient6.eth0.pid eth0",
            "/usr/local/bin/mTerm_server slot1 /dev/ttyS1",
            "/usr/local/bin/mTerm_server slot2 /dev/ttyS2",
            "/usr/local/bin/mTerm_server slot3 /dev/ttyS3",
            "/usr/local/bin/mTerm_server slot4 /dev/ttyS4",
            "/usr/local/bin/sensord slot1 slot2 slot3 slot4 spb nic",
            "healthd",
            "gpiointrd",
            "/usr/local/bin/gpiod slot1 slot2 slot3 slot4",
            "ntpd",
            "ipmid",
            "ncsid",
            "front-paneld",
            "rest.py",
            "/usr/local/bin/ipmbd 3 2",
            "/usr/local/bin/ipmbd 1 1",
            "/usr/local/bin/ipmbd 5 3",
            "/usr/local/bin/ipmbd 7 4",
        ]
