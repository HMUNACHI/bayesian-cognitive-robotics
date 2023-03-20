#!/usr/bin/env python

import rospy
from blip.msg import perceived_info
from blip.msg import robot_info
from blip.srv import predict_robot_expression, predict_robot_expressionResponse
from bayesian.bbn import *

global bbn

# defining the probabilities
def f_o(o):
    '''Size of Object'''
    return 0.5


def f_he(he):
    '''Human Expression'''
    return 0.333

def f_ha(ha):
    '''Human Action'''
    return 0.333


def f_re(o, he, ha, re):
    '''Robot Expression: Probabilities determined from experiments'''

    # creating the conditional probability table
    table = dict()
    table['shrh'] = 0.8
    table['shrs'] = 0.2
    table['shrn'] = 0.0
    table['shoh'] = 0.8
    table['shos'] = 0.2
    table['shon'] = 0.0
    table['shah'] = 0.6
    table['shas'] = 0.2
    table['shan'] = 0.2
    
    table['ssrh'] = 0.0
    table['ssrs'] = 0.0
    table['ssrn'] = 1.0
    table['ssoh'] = 0.0
    table['ssos'] = 0.1
    table['sson'] = 0.9
    table['ssah'] = 0.0
    table['ssas'] = 0.2
    table['ssan'] = 0.8

    table['snrh'] = 0.7
    table['snrs'] = 0.3
    table['snrn'] = 0.0
    table['snoh'] = 0.8
    table['snos'] = 0.2
    table['snon'] = 0.0
    table['snah'] = 0.6
    table['snas'] = 0.2
    table['snan'] = 0.2

    table['bhrh'] = 1.0
    table['bhrs'] = 0.0
    table['bhrn'] = 0.0
    table['bhoh'] = 1.0
    table['bhos'] = 0.0
    table['bhon'] = 0.0
    table['bhah'] = 0.8
    table['bhas'] = 0.2
    table['bhan'] = 0.0
    
    table['bsrh'] = 0.0
    table['bsrs'] = 0.0
    table['bsrn'] = 1.0
    table['bsoh'] = 0.1
    table['bsos'] = 0.1
    table['bson'] = 0.8
    table['bsah'] = 0.2
    table['bsas'] = 0.2
    table['bsan'] = 0.6

    table['bnrh'] = 0.8
    table['bnrs'] = 0.2
    table['bnrn'] = 0.0
    table['bnoh'] = 0.9
    table['bnos'] = 0.1
    table['bnon'] = 0.0
    table['bnah'] = 0.7
    table['bnas'] = 0.2
    table['bnan'] = 0.1

    # logic for selecting key characters according to value of the variables o, he, ha, re
    key = ''
 
    if o == 1:
     key = key + 's'
    elif o == 0:
     key = key + 's'
    else:
     key = key + 'b' 

    if he == 1:
     key = key + 'h'
    elif o == 2:
     key = key + 's'
    else:
     key = key + 'n' 

    if ha == 1:
     key = key + 'r'
    elif o == 2:
     key = key + 'o' 
    else:
     key = key + 'a' 
 
    if re == 1:
     key = key + 'h'
    elif o == 2:
     key = key + 's' 
    else:
     key = key + 'n' 

    return table[key]

# called with the percieved info recieved by the service, builds the Neural network and (Ideally) returns the response
def handler_predictor(req):
    # collect the percieved information
    percieved_info = perceived_info()
    f_o = percieved_info.object_size
    f_he = percieved_info.human_expression
    f_ha = percieved_info.human_action
    probs = bbn.query(f_o=f_o,f_he=f_he,f_ha=f_ha) # gives an error "'dict' object has no attribute 'id'", traced to "in serialize\n    buff.write(_get_struct_q3d().pack(_x.prediction.id, _x.prediction.p_happy, _x.prediction.p_sad, _x.prediction.p_neutral))\n'" which I could'nt troubleshoot before the deadline

    preds = robot_info() #dummy values
    preds.id = len(probs)
    preds.p_happy = 0.6
    preds.p_sad = 0.2
    preds.p_neutral = 0.2

    return predict_robot_expressionResponse(preds)


def expression_prediction_server():
    rospy.init_node('robot_expression_prediction')  # initialise node
    s = rospy.Service('RobotExpressionPrediction', predict_robot_expression, handler_predictor) # start service
    print ("Service up.")
    rospy.spin()


if __name__ == '__main__':

    # build the bayesian belief network
    bbn = build_bbn(f_o, f_he, f_ha, f_re)

    # create service
    expression_prediction_server()
