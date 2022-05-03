import rclpy
import my_controller.comm as comm
import cv2

def main(args=None):
	rclpy.init(args=args)
	my_controller_subscriber = comm.ClientSubscriber()
	my_controller_publisher = comm.ClientPublisher()

	while(1):
		rclpy.spin_once(my_controller_publisher)

		rclpy.spin_once(my_controller_subscriber)
		myImage = my_controller_subscriber.GetImage() # Cv2Image
		cv2.imshow("My Image", myImage)
		keyin = cv2.waitKey(1)
		if (keyin == ord('w')):
			my_controller_publisher.set_velocity(0.1, 0.0) # move forward
		elif (keyin == ord('a')):
			my_controller_publisher.set_velocity(0.0, 0.1) # turn left (counter clock wise)
		elif (keyin == ord('s')):
			my_controller_publisher.set_velocity(-0.1, 0.0) # move backward
		elif (keyin == ord('d')):
			my_controller_publisher.set_velocity(0.0, -0.1) # turn right (clock wise)
		elif (keyin == 32): # space bar
			my_controller_publisher.set_velocity(0.0, 0.0) # stop

		elif (keyin == ord('q')): # quit
			break

	my_controller_publisher.destry_node()
	my_controller_subscriber.destroy_node()
	rclpy.shutdown

if __name__ == '__main__':
    main()
