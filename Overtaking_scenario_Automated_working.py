import glob
import os
import sys
from agents.navigation import controller
from agents.navigation import local_planner
from agents.navigation import basic_agent11
import Overtaking_function 
from enum import Enum
#import threading
import csv
import datetime

try:
    sys.path.append(glob.glob('D:/Carla_windows_built_04_10_19/carla/PythonAPI/carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import random
import time
#import change_lane

_args_lateral_dict = {'K_P': 1.0, 'K_D': 0.01, 'K_I': 0.0, 'dt': 0.05}
_target_speed = 20
vehicle1_x,vehicle1_y,vehicle1_z=[],[],[]
vehicle2_x,vehicle2_y,vehicle2_z=[],[],[]
time_sec=[]
vehicle1_Lane_Type=[]
vehicle1_Possible_Lane_Change=[]
vehicle2_Lane_Type=[]
vehicle2_Possible_Lane_Change=[]
vehicle_1=[]
vehicle_2=[]

def Autopilot_vehicle(world,vehicle2):
    agent_overtaking_vehicle2= Overtaking_function.Over_taking(vehicle2)
    agent4=local_planner.LocalPlanner(vehicle2)
    waypoint3 = world.get_map().get_waypoint(vehicle2.get_location())
    plan4=agent_overtaking_vehicle2.Waypoint_straight(waypoint3)
    while True:
        agent4.set_global_plan(plan4)
        agent4.set_speed(5)
        control_1=agent4.run_step()
        vehicle2.apply_control(control_1)
#def CSV_write(speed_Straight,
 #       speed_lane_change,
  #      speed_orgin_lane,way,time_sec,vehicle1_x,vehicle1_y,vehicle1_z,vehicle1_Lane_Type,vehicle1_Possible_Lane_Change,vehicle2_x,vehicle2_y,vehicle2_z,vehicle2_Lane_Type,vehicle2_Possible_Lane_Change):
def CSV_write(limit,speed_Straight,
        speed_lane_change,
        speed_orgin_lane,way,time_sec,vehicle_1,vehicle1_Lane_Type,vehicle1_Possible_Lane_Change,vehicle_2,vehicle2_Lane_Type,vehicle2_Possible_Lane_Change):   
    with open('Over_Taking_{}_{}_{}_way_{}.csv'.format(speed_Straight, speed_lane_change, speed_orgin_lane, way), 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "vehicle1_x","vehicle1_y","vehicle1_z","vehicle1_Lane_Type", "vehicle1_Possible_Lane_Change","vehicle2_x","vehicle2_y","vehicle2_z","vehicle2_Lane_Type", "vehicle2_Possible_Lane_Change"])
        #print(t)
        #counter+=1
        writer = csv.writer(file)
        for i in range (0,limit):
            #writer.writerow([str(time_sec[i]), str(vehicle1_x[i]), str(vehicle1_y[i]), str(vehicle1_z[i]),str(vehicle1_Lane_Type[i]), str(vehicle1_Possible_Lane_Change[i]),str(vehicle2_x[i]), str(vehicle2_y[i]), str(vehicle2_z[i]),str(vehicle2_Lane_Type[i]), str(vehicle2_Possible_Lane_Change[i])])
            writer.writerow([str(time_sec[i]), str(vehicle_1[i].x),str(vehicle_1[i].y),str(vehicle_1[i].z),str(vehicle1_Lane_Type[i]), str(vehicle1_Possible_Lane_Change[i]),str(vehicle_2[i].x),str(vehicle_2[i].y),str(vehicle_2[i].z),str(vehicle2_Lane_Type[i]), str(vehicle2_Possible_Lane_Change[i])])
def List_location(world,vehicle1,vehicle2):
    waypoint_vehicle1 = world.get_map().get_waypoint(vehicle1.get_location(), project_to_road=True, lane_type=(carla.LaneType.Driving))
    waypoint_vehicle2 = world.get_map().get_waypoint(vehicle2.get_location(), project_to_road=True, lane_type=(carla.LaneType.Driving))
    loc_vehicle1=vehicle1.get_location()
    loc_vehicle2=vehicle2.get_location()
    t = time.clock()
    #print(t)
    '''vehicle1_x.append(loc_vehicle1.x)
    vehicle1_y.append(loc_vehicle1.y)
    vehicle1_z.append(loc_vehicle1.z)
    vehicle2_x.append(loc_vehicle2.x)
    vehicle2_y.append(loc_vehicle2.y)
    vehicle2_z.append(loc_vehicle2.z)'''
    vehicle_1.append(loc_vehicle1)
    vehicle_2.append(loc_vehicle2)
    time_sec.append(t)
    vehicle1_Lane_Type.append(waypoint_vehicle1.lane_type)
    vehicle1_Possible_Lane_Change.append(waypoint_vehicle1.lane_change)
    vehicle2_Lane_Type.append(waypoint_vehicle2.lane_type)
    vehicle2_Possible_Lane_Change.append(waypoint_vehicle2.lane_change)
    #return time_sec,vehicle1_x,vehicle1_y,vehicle1_z,vehicle1_Lane_Type,vehicle1_Possible_Lane_Change,vehicle2_x,vehicle2_y,vehicle2_z,vehicle2_Lane_Type,vehicle2_Possible_Lane_Change
    return time_sec,vehicle_1,vehicle1_Lane_Type,vehicle1_Possible_Lane_Change,vehicle_2,vehicle2_Lane_Type,vehicle2_Possible_Lane_Change

def main():
    actor_list = []
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(2.0)
        world = client.get_world()
        spwan_points=world.get_map().get_spawn_points()
        #counter=0
        #for i in spwan_points:
            #print(counter,i)
            #counter=counter+1
        blueprint_library = world.get_blueprint_library()
        bp = random.choice(blueprint_library.filter('vehicle'))
        car = random.choice(blueprint_library.filter('vehicle.tesla.model3'))
        counter=0
        vehicle1 = world.spawn_actor(car,spwan_points[54])#18
        vehicle2= world.spawn_actor(car,spwan_points[145])#338
        #vehicle2.set_autopilot(True)
        actor_list.append(vehicle1) 
        actor_list.append(vehicle2)
        speed_Straight=70
        speed_lane_change=50
        speed_orgin_lane=20
        way=2
        limit=305
        #car=vehicle2.get_control()
        #car.throttle=0.2
        #Autopilot_vehicle(world,vehicle2)
        #t1 = threading.Thread(target=Autopilot_vehicle, args=(world,vehicle2,))
        #t1.start()        

        # agent_overtaking= Overtaking_function.Over_taking(vehicle1)
        # agent1=basic_agent11.BasicAgent(vehicle1)
        #agent2=local_planner.LocalPlanner(vehicle1)
        #vehicle2.apply_control(car)
        #print(waypoint)
        agent_overtaking_vehicle3= Overtaking_function.Over_taking(vehicle1)
        agent5=local_planner.LocalPlanner(vehicle1)
        waypoint4 = world.get_map().get_waypoint(vehicle1.get_location())
        plan5=agent_overtaking_vehicle3.Waypoint_straight(waypoint4) 
        while True:
            loc1=vehicle1.get_location()
            loc2=vehicle2.get_location()
            calc=loc2-loc1
            #print(calc.x)
            #CSV_write(world,vehicle1,vehicle2)
            agent5.set_global_plan(plan5)
            agent5.set_speed(speed_Straight)
            control_2=agent5.run_step()
            vehicle1.apply_control(control_2)
            vehicle2.set_autopilot(True)
            #print('time12---',time.clock())
            List_location(world,vehicle1,vehicle2)
            #CSV_write(world,vehicle1,vehicle2)
            #Autopilot_vehicle(world,vehicle2)
            if round(calc.x,0)<=16:
                #print('123')
                #time.sleep(20)
                #control.brake=1.0
                #control.throttle=0.0
                #vehicle1.apply_control(control)
                waypoint1 = world.get_map().get_waypoint(vehicle1.get_location())
                plan2=agent_overtaking_vehicle3.Waypoint_Plan(waypoint1)
                #print(len(plan))
                #print(len(plan))
                #time.sleep(10)
                break
        agent2=local_planner.LocalPlanner(vehicle1)
        while True:
                loc1=vehicle1.get_location()
                loc2=vehicle2.get_location()
                calc=loc2-loc1
                print(calc.x)
                agent2.set_global_plan(plan2)
                agent2.set_speed(speed_lane_change)
                control1=agent2.run_step()
                vehicle1.apply_control(control1)
                #vehicle2.set_autopilot(True)
                #Autopilot_vehicle(world,vehicle2)
                List_location(world,vehicle1,vehicle2)
                if round(calc.x,4)<=-9.2375:
                    #agent2.reset_vehicle()
                    plan2.clear()
                    #print(len(plan2))
                    #print('success')
                    #time.sleep(20)
                    waypoint2 = world.get_map().get_waypoint(vehicle1.get_location())
                    plan3=agent_overtaking_vehicle3.Waypoint_Plan(waypoint2)
                    #print(len(plan3))
                    #print(len(plan))
                    #time.sleep(10)
                    break
        agent3=local_planner.LocalPlanner(vehicle1)
        while True:
                #print('Success1')
                agent3.set_global_plan(plan3)
                agent3.set_speed(speed_orgin_lane)
                control2=agent3.run_step()
                vehicle1.apply_control(control2)
                #time_sec,vehicle1_x,vehicle1_y,vehicle1_z,vehicle1_Lane_Type,vehicle1_Possible_Lane_Change,vehicle2_x,vehicle2_y,vehicle2_z,vehicle2_Lane_Type,vehicle2_Possible_Lane_Change=List_location(world,vehicle1,vehicle2)
                time_sec,vehicle_1,vehicle1_Lane_Type,vehicle1_Possible_Lane_Change,vehicle_2,vehicle2_Lane_Type,vehicle2_Possible_Lane_Change=List_location(world,vehicle1,vehicle2)
                #vehicle2.set_autopilot(True)
                #Autopilot_vehicle(world,vehicle2)
                print(len(vehicle2_x),len(time_sec))
                if len(time_sec)==limit:
                    break
        #CSV_write(speed_Straight,
        #speed_lane_change,
        #speed_orgin_lane,way,time_sec,vehicle1_x,vehicle1_y,vehicle1_z,vehicle1_Lane_Type,vehicle1_Possible_Lane_Change,vehicle2_x,vehicle2_y,vehicle2_z,vehicle2_Lane_Type,vehicle2_Possible_Lane_Change)
        CSV_write(limit,speed_Straight,
        speed_lane_change,
        speed_orgin_lane,way,time_sec,vehicle_1,vehicle1_Lane_Type,vehicle1_Possible_Lane_Change,vehicle_2,vehicle2_Lane_Type,vehicle2_Possible_Lane_Change)
    finally:

        print('destroying actors')
        for actor in actor_list:
         actor.destroy()
        print('done.')

if __name__ == '__main__':

    main()
