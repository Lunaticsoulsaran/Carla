import glob
import os
import sys
from agents.navigation import controller
from agents.navigation import local_planner
from agents.navigation import basic_agent11
from enum import Enum

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

class RoadOption(Enum):
    """
    RoadOption represents the possible topological configurations when moving from a segment of lane to other.
    """
    VOID = -1
    LEFT = 1
    RIGHT = 2
    STRAIGHT = 3
    LANEFOLLOW = 4
    CHANGELANELEFT = 5
    CHANGELANERIGHT = 6


class Over_taking():
    def __init__(self, vehicle):
        self._vehicle = vehicle
        self._map = self._vehicle.get_world().get_map()

        self._dt = None
        self._target_speed = None
        self._sampling_radius = None
        self._min_distance = None
        self._current_waypoint = None
        self._target_road_option = None
        self._next_waypoints = None
        self.target_waypoint = None
        self._vehicle_controller = None
        self._global_plan = None
        #self.Initial_waypoint=None
        self.point=4

    def Waypoint_Plan(self,Initial_waypoint):
        print(Initial_waypoint.lane_change)
        if str(Initial_waypoint.lane_change) == 'Right':
            self.plan1=[]
            self.plan1.append((Initial_waypoint,RoadOption.LANEFOLLOW))
            J=Initial_waypoint.get_right_lane().next(self.point)
            #print(J.transform.location)
            #world.get_map().get_waypoint(J.transform.location)
            #print(len(J))
            h=0
            while h<=40:
                #print(J)
                for i in J:
                    #print('Waypoin1--',i)
                    #time.sleep(10)
                    self.plan1.append((i,RoadOption.LANEFOLLOW))
                    #k=world.get_map().get_waypoint(i)
                    #print(k)<
                    l=i.next(self.point)
                    for o in l:
                        #print('Waypoin2--',o)
                        #time.sleep(10)
                        self.plan1.append((o,RoadOption.LANEFOLLOW))
                        J=o.next(self.point)
                #print(J)
                h=h+1
                if h==42:
                    #print(len(self.plan1))
                    time.sleep(60)
            return self.plan1
        else:
            self.plan2=[]
            self.plan2.append((Initial_waypoint,RoadOption.LANEFOLLOW))
            print(Initial_waypoint.lane_change)
            if str(Initial_waypoint.lane_change) == 'Left':
                J=Initial_waypoint.get_left_lane().next(self.point)
                #print(J.transform.location)
                #world.get_map().get_waypoint(J.transform.location)
                #print(len(J))
                h=0
                while h<=40:
                    #print(J)
                    for i in J:
                        #print('Waypoin1--',i)
                        #time.sleep(10)
                        self.plan2.append((i,RoadOption.LANEFOLLOW))
                        #k=world.get_map().get_waypoint(i)
                        #print(k)<
                        l=i.next(self.point)
                        for o in l:
                            #print('Waypoin2--',o)
                            #time.sleep(10)
                            self.plan2.append((o,RoadOption.LANEFOLLOW))
                            J=o.next(self.point)
                    #print(J)
                    h=h+1
                    if h==42:
                        #print(len(self.plan2))
                        time.sleep(60)
                return self.plan2

    def Waypoint_straight(self,Initial_waypoint):
            self.plan_straight=[]
            self.plan_straight.append((Initial_waypoint,RoadOption.LANEFOLLOW))
            J=Initial_waypoint.next(self.point)
            h=0
            while h<=40:
                #print(J)
                for i in J:
                    #print('Waypoin1--',i)
                    #time.sleep(10)
                    self.plan_straight.append((i,RoadOption.LANEFOLLOW))
                    #k=world.get_map().get_waypoint(i)
                    #print(k)<
                    l=i.next(self.point)
                    for o in l:
                        #print('Waypoin2--',o)
                        #time.sleep(10)
                        self.plan_straight.append((o,RoadOption.LANEFOLLOW))
                        J=o.next(self.point)
                #print(J)
                h=h+1
                if h==42:
                    #print(len(self.plan_straight))
                    time.sleep(60)
            return self.plan_straight

