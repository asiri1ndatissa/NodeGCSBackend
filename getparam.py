import asyncio
from mavsdk import System
from mavsdk.param import Param
from operator import attrgetter

async def run():
    # Init the drone
    drone = System()
     
    await drone.connect(system_address="udp://:14540")
        # Start the tasks
    asyncio.ensure_future(print_params(drone))

   
async def print_params(drone):
    x = await drone.param.get_all_params()
    intparams, float_params = attrgetter('int_params', 'float_params')(x)

    for ele in enumerate(intparams):
      name , value = attrgetter('name', 'value')(ele[1])
      print(name, value)
    for ele in enumerate(float_params):
      name , value = attrgetter('name', 'value')(ele[1])
      print(name, value)

          
if __name__ == "__main__":
    # Start the main function
    asyncio.ensure_future(run())

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()