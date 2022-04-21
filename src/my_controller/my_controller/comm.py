import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

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
		super().__init__('client_subscriber')
		self.subscriber = self.create_subscription(String, 'server2client', self.listener_callback, 10)

	def listener_callback(self, msg):
		self.get_logger().info('Subscribed: %s' % msg.data)