#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
    data = data.ranges
    rospy.loginfo(rospy.get_caller_id() + f"-{min(data)}")
    
def closest_point():

    rospy.init_node('closest_point', anonymous=True)
    rospy.Subscriber("scan", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    closest_point()