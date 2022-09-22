#!/usr/bin/env python
import rospy
import std_msgs.msg import Int32

rospy.init_node('ej2')
pub = rospy.Publisher('contador',Int32,queue_size = 10)

contador = Int32()
contador.data = 0
frecuencia = rospy.Rate(0.5)

while not rospy.is_shutdown() :
	contador.data = contador.data+1
	pub.publish(contador)
	frecuencia.sleep()


