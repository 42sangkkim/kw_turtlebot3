import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image

class ClientPublisher(Node):
	def __init__(self):
		super().__init__('my_controller_pub')
		self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.timer_callback)

	def timer_callback(self):
		msg = Twist()
		msg.linear.x = 1.0
		msg.angular.z = 1.0
		self.publisher.publish(msg)
		self.get_logger().info("Publishing: %s" % msg)

class ClientSubscriber(Node):
	def __init__(self):
		super().__init__('my_comtroller_sub')
		self.subscriber = self.create_subscription(Image, '/camera/image_raw', self.listener_callback, 10)

	def listener_callback(self, msg):
		self.get_logger().info('Subscribed: width %s' % msg.width)
		self.get_logger().info('Subscribed: height %s' % msg.height)
		self.get_logger().info('Subscribed: data %s' % msg.data)