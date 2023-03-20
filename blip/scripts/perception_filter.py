#!/usr/bin/env python
import rospy
import random
from blip.msg import object_info
from blip.msg import human_info
from blip.msg import perceived_info

# create global file
global Pub_filter

def callback(data):
    randomfilter = random.randint(1,8)
    rospy.loginfo(randomfilter)

    # generate random value and filters
    if randomfilter==1:
        data.object_size = 0
    elif randomfilter==2:
        data.human_action=0
    elif randomfilter==3:
        data.human_expression=0
    elif randomfilter == 4:
        data.object_size = 0
        data.human_action=0
    elif randomfilter==5:
        data.object_size = 0
        data.human_expression=0
    elif randomfilter==6:
        data.human_action=0
        data.human_expression=0
    elif randomfilter==7:
        data.object_size = 0
        data.human_action=0
        data.human_expression=0

    rospy.loginfo(data)

    # publish
    Pub_filter.publish(data)


def callbackobj(data):
    pass
def callbackhuman(data):
    pass

def listener():
    # subscribe to the topiiics published in node 1
    rospy.init_node('Perception_Filter', anonymous=True)
    rospy.Subscriber("percieved_info", perceived_info, callback)
    rospy.Subscriber("object_info", object_info, callbackobj)
    rospy.Subscriber("human_info", human_info, callbackhuman)
    rospy.spin()


if __name__ == '__main__':
    Pub_filter = rospy.Publisher("Perceived", perceived_info, queue_size=10)
    listener()
