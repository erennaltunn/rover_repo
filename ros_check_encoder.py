#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from random import randint
from std_msgs.msg import String

class Control:
    check_button = 1

    def __init__(self):
        rospy.init_node("control_node")
        self.random_lis()


    def arm_get_list(self,data):  #24
        s = str(data.data)
        list_of_data = []
        i = 1
        if s[0] == "A" and s[-1] == "B":
            for a in range(6):
                val = s[i:i+4]
                list_of_data.append(val)
                i += 4
        self.control_list(list_of_data)


    def drive_get_list(self,data): #16
        s = str(data.data)
        list_of_data = []
        i = 1
        if s[0] == "A" and s[-1] == "B":
            for a in range(4):
                val = s[i:i+4]
                list_of_data.append(val)
                i += 4
        self.control_list(list_of_data)


    def control_list(self,list):
        edited_list=[]

        for a in range(len(list)):
            str_motor_value = str(list[a][1:])
            int_motor_value = int(list[a][1:])
            if (int_motor_value > 255):
                int_motor_value = 255
                str_motor_value = str(int_motor_value)
            edit = list[a][0] + str_motor_value
            edited_list.append(edit)

        last_message = ' '.join(edited_list)
        rospy.loginfo("%s",last_message)

        if len(last_message)>0:
            self.check_start = 1
            self.talker(last_message)


    def talker(self,pub_message):
        pub_drive = rospy.Publisher('/position/drive', String, queue_size=10)
        pub_arm = rospy.Publisher('/position/robotic_arm',String,queue_size=10)

        while not rospy.is_shutdown() and self.check_start:
            if len(pub_message) == 19: #drive message including spaces
                pub_drive.publish(pub_message)
                self.check_start = 0

            if len(pub_message) == 29: #robotic_arm message including spaces
                pub_arm.publish(pub_message)
                self.check_start = 0


    def random_lis(self):
        rospy.Subscriber('/serial/drive',String,self.drive_get_list)
        rospy.Subscriber('/serial/robotic_arm', String, self.arm_get_list)
        rospy.spin()


if __name__ == '__main__':
    k = Control()
