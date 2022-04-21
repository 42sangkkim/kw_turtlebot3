import rclpy
import my_controller.comm as comm

def main(args=None):
	rclpy.init(args=args)
	my_controller_publisher = comm.ClientPublisher()

	rclpy.spin(my_controller_publisher)

	my_controller_publisher.destry_node()
	rclpy.shutdown


if __name__ == '__main__':
    main()
