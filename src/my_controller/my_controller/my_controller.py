import rclpy
import my_controller.comm as comm

def main(args=None):
	rclpy.init(args=args)
	# my_controller_publisher = comm.ClientPublisher()
	my_controller_subscriber = comm.ClientSubscriber()

	# rclpy.spin(my_controller_publisher)
	rclpy.spin_once(my_controller_subscriber)

	# my_controller_publisher.destry_node()
	my_controller_subscriber.destroy_node()
	rclpy.shutdown

if __name__ == '__main__':
    main()
