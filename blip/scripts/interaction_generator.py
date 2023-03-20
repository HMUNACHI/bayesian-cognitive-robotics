#!/usr/bin/env python
import rospy
import random

#include all message types required
from blip.msg import object_info
from blip.msg import human_info
from blip.msg import perceived_info



def interaction_generator():

    #initialise publisher topics
    Pub_object = rospy.Publisher("object_info", object_info, queue_size=10)
    Pub_human = rospy.Publisher("human_info", human_info, queue_size=10)
    Pub_percieved = rospy.Publisher("percieved_info", perceived_info, queue_size=10)

    #initialise node
    rospy.init_node('interaction_generator', anonymous=True)
    rate = rospy.Rate(0.1) # 0.1hz ie 10 seconds
    idnumber = 0   ##initialise interaction ID counter

    #initialise message containers
    obj = object_info()
    human = human_info()
    percieved = perceived_info()


    while not rospy.is_shutdown():

        idnumber+=1

        # generate random object size between 1(small) and 2 (big)
        obj.object_size = random.randint(1,2)
        obj.id = idnumber

        #publish object to topic IntTopicObject
        Pub_object.publish(obj)
        rospy.loginfo(obj)

        human.id = idnumber
        # generate random human expression 1 (happy), 2(sad), 3(neutral)
        human.human_expression = random.randint(1,3)

        # generate random human action 1(looking at robot face), 2(looking at colored toy), 3(looking away)7
        human.human_action = random.randint(1,3)
        Pub_human.publish(human)
        rospy.loginfo(human)


        # assign values and publish
        percieved.id = idnumber
        percieved.object_size = obj.object_size
        percieved.human_action = human.human_action
        percieved.human_expression = human.human_expression

        Pub_percieved.publish(percieved)

        rate.sleep()


if __name__ == '__main__':
    try:
        interaction_generator()
    except rospy.ROSInterruptException:
        pass
