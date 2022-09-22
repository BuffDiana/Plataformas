#!/usr/bin/env python
import rospy
import random
from geometry_msgs.msg import Twist

rospy.init_node('Ejercicio3')
pub = rospy.Publisher('aleatorio', Twist,queue_size = 10)

aleatorio = Twist()
frecuencia = rospy.Rate(0.5)

while not rospy.is_shutdown() :
	aleatorio.linear.x = random.randint(1,200)
	aleatorio.linear.y = random.randint(1,200)
	aleatorio.linear.z = random.randint(1,200)
	aleatorio.angular.x = random.randint(1,200)
	aleatorio.angular.y = random.randint(1,200)
	aleatorio.angular.z = random.randint(1,200)
	pub.publish(aleatorio)
	frecuencia.sleep()


	
