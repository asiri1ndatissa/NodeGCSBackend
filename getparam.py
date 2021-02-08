
# import asyncio
# from mavsdk import System
# from mavsdk.param import (IntParam,FloatParam,AllParams,ParamResult,ParamError,Param)



# async def run():
#     drone = System()
#     await drone.connect(system_address="udp://:14540")

    
#     print("drone to conaaaaaaaaanect...")
#     # params= Param.get_all_params()

#     async for param in drone.param.get_all_params():
#         print(f"health: {param}")
    


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(run())

import asyncio
from mavsdk import System
from mavsdk.param import Param
from operator import attrgetter
async def run():
    # Init the drone
    drone = System()
   
  
    await drone.connect(system_address="udp://:14540")
    
    # Start the tasks
    asyncio.ensure_future(print_battery(drone))
    # asyncio.ensure_future(print_gps_info(drone))
    # asyncio.ensure_future(print_in_air(drone))
    # asyncio.ensure_future(print_position(drone))
   
async def print_battery(drone):
    x = await drone.param.get_all_params()
    gender, username = attrgetter('int_params', 'float_params')(x)

    # y = attrgetter('<mavsdk.param.IntParam object at 0x7febcc219cc0>')(gender)
    for ele in enumerate(gender):
      name , value = attrgetter('name', 'value')(ele[1])
      print(name, value)

        
  
async def print_gps_info(drone):
    async for gps_info in drone.telemetry.gps_info():
        print(f"GPS info: {gps_info}")

        

async def print_in_air(drone):
    async for in_air in drone.telemetry.in_air():
        print(f"In air: {in_air}")


async def print_position(drone):
    async for position in drone.telemetry.position():
        print(position)


if __name__ == "__main__":
    # Start the main function
    asyncio.ensure_future(run())

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()