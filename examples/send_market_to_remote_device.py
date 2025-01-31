# This file is part of Octopus Sensing <https://octopus-sensing.nastaran-saffar.me/>
# Copyright © Nastaran Saffaryazdi 2020
#
# Octopus Sensing is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
#  either version 3 of the License, or (at your option) any later version.
#
# Octopus Sensing is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Foobar.
# If not, see <https://www.gnu.org/licenses/>.

import sys  # nopep8
sys.path.append('../octopus-sensing/')  # nopep8
import time
from octopus_sensing.device_coordinator import DeviceCoordinator
from octopus_sensing.devices.network_devices.socket_device import SocketNetworkDevice
from octopus_sensing.common.message_creators import start_message, stop_message

def server():
    '''
    Starts a server and sends several messages and terminates
    '''
    device_coordinator = DeviceCoordinator()
    socket_device = SocketNetworkDevice("0.0.0.0", 5002)
    device_coordinator.add_devices([socket_device])


    time.sleep(2)
    input("Press enter to start sending marker")
    message = start_message("test", "00")
    device_coordinator.dispatch(message)
    
    time.sleep(2)
    message = stop_message("test", "00")
    device_coordinator.dispatch(message)
    time.sleep(2)
    message = start_message("test", "01")
    device_coordinator.dispatch(message)
    time.sleep(2)
    message = stop_message("test", "01")
    device_coordinator.dispatch(message)
    time.sleep(3)

    device_coordinator.terminate()

if __name__ == "__main__":
    server()
