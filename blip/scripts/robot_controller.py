#!/usr/bin/env python
import rospy
from blip.msg import perceived_info
from blip.msg import robot_info
from blip.srv import predict_robot_expression

global Pub_expression

def service_client(p_info):
    print ("Recieved Perception Info")
    print ("Calling service")
    rospy.wait_for_service('RobotExpressionPrediction')
    Pub_expression = rospy.Publisher("Robot_Expression", robot_info, queue_size=10)
    print ("Requesting")
    rospy.loginfo(p_info)
    try:
        Predict = rospy.ServiceProxy('RobotExpressionPrediction', predict_robot_expression)
        resp1 = Predict(p_info)
        # publish object to topic
        Pub_expression.publish(resp1.prediction)
        print("Prediction")
        rospy.loginfo(resp1.prediction)

    except rospy.ServiceException, e:
        print ("Service call failed: %s" % e)


# listen for percieved topics, call service client to get the robot predicted values
def listener():
    Pub_expression = rospy.Publisher("Robot_Expression", robot_info, queue_size=10)
    print ("Waiting for publisher")
    rospy.init_node('Robot_Controller', anonymous=True)
    rospy.Subscriber("Perceived", perceived_info, service_client)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
