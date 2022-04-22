import rclpy
import my_controller.comm as comm
import cv2

def main(args=None):
	rclpy.init(args=args)
	# my_controller_publisher = comm.ClientPublisher()
	my_controller_subscriber = comm.ClientSubscriber()

	# rclpy.spin(my_controller_publisher)
	rclpy.spin_once(my_controller_subscriber)

	myImage = my_controller_subscriber.GetImage() # Cv2Image
	cv2.namedWindow("My Image", flags=cv2.WINDOW_NORMAL)
	cv2.resizeWindow(winname="My Image", width=320, height=180)
	cv2.imshow("My Image", myImage)
	cv2.waitKey(0)

	# my_controller_publisher.destry_node()
	my_controller_subscriber.destroy_node()
	rclpy.shutdown

if __name__ == '__main__':
    main()
