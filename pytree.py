import glob
#"python.linting.pylintArgs": []
#"python.linting.pylintArgs": ["--generate-members"]
import os
import sys
import py_trees 
import csv

#from .behaviour import Behaviour
#from .common import Status
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
import random
import time
import cv2
#--extension-pkg-whitelist=cv2
import numpy as np
actor_list=[]
vehicle_list=[]


def main():
    


    
    client = carla.Client('localhost', 2000)
    client.set_timeout(2.0) 
    world = client.get_world()
    map=world.get_map()
    spawnpoints = map.get_spawn_points()
    #print(len(spawnpoints))
    for a in world.get_actors().filter("vehicle*"):
        if a.is_alive:
            a.destroy()
    a = len(spawnpoints)
    count = 0
    spawn_point = carla.Transform(carla.Location(x=339.70, y=-90.20))
    blueprint_library = world.get_blueprint_library()
    car = random.choice(blueprint_library.filter('vehicle.tesla.model3'))
    vehicle1 = world.spawn_actor(car, spawn_point)
    control = vehicle1.get_control()
    #vehicle1.set_autopilot(True)
    counter=0
    waypoint = world.get_map().get_waypoint(vehicle1.get_location(), project_to_road=True, lane_type=(carla.LaneType.Driving))

    with open('Both_vehicle_Dynamic.csv', 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["No", "Time", "X","Y","Z", "Lane_Type", "Possible_Lane_Change","Type Of Scenario"])
    #f= open("guru99.txt","w+")
        while (control.throttle>0.0) and spawn_point.location.x > 0.0000000:
            v_loc=vehicle1.get_location()
            #print(v_loc)
            t = carla.Timestamp()
            #print(t)
            counter+=1
            #print(time.clock())
            #writer = csv.writer(file)
            
            #print("hi")
            writer.writerow([counter, str(time.clock()), str(v_loc.x),str(v_loc.y),str(v_loc.z), str(waypoint.lane_type), str(waypoint.lane_change),str("Autopilot_stationary_with_wait_time")])
    #lidar = world.get_blueprint_library().find('sensor.lidar.ray_cast')
    #transform1 = carla.Transform(carla.Location(x=0.2, z=1.0))
    #sensor1 = world.spawn_actor(lidar, transform1, attach_to=vehicle2)

    '''
    blueprint = world.get_blueprint_library().find('sensor.camera.rgb')
    blueprint.set_attribute('image_size_x', '800')
    blueprint.set_attribute('image_size_y', '600')
    blueprint.set_attribute('fov', '90')
    blueprint.set_attribute('sensor_tick', '0.0')
    transform2 = carla.Transform(carla.Location(x=0.5, z=1.5))
    camera = world.spawn_actor(blueprint, transform2, attach_to=vehicle2)'''


    '''obs = world.get_blueprint_library().find('sensor.other.obstacle')
    obs.set_attribute('debug_linetrace', 'True')
    obs.set_attribute('distance', '5')
    obs.set_attribute('sensor_tick', '0.0')
    transform3 = carla.Transform(carla.Location(x=0.1, z=0.9))
    sensor2 = world.spawn_actor(obs, transform3, attach_to=vehicle2)
    sensor2.listen(lambda data: print(data))
    #measurements, sensor_data = vehicle2.read_data()
    
    #py_trees.composites.Composite.add_child(car)
    world.tick()
    #vehicle2.set_autopilot_(True)

    vehicle2.apply_control(carla.VehicleControl(throttle=1, steer=0.0))
    time.sleep(4)'''

    #print("Current lane type: " + str(waypoint.lane_type))
    #Check current lane change allowed
    #print("Current Lane change:  " + str(waypoint.lane_change))
    #Left and Right lane markings
    #print("L lane marking type: " + str(waypoint.left_lane_marking.type))
    #print("R lane marking type: " + str(waypoint.right_lane_marking.type))
    #print("R lane marking change: " + str(waypoint.right_lane_marking.lane_change))
    #print(str(control.throttle))
    #veh = carla.ObstacleDetectionSensorEvent(distance)
    #print(obs.get_attribute('distance'))


if __name__ == '__main__':

    main()
    #waypoint_tuple_list = main().spawn_point.get_topology()
    #print(waypoint_tuple_list)
    