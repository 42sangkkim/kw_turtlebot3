import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from sensor_msgs.msg import Imu
from cv_bridge import CvBridge

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
		self.subscribtionImg = self.create_subscription(Image, '/camera/image_raw', self.listener_Img_callback, 10)
		self.subscribtionImu = self.create_subscription(Imu, '/imu', self.listener_Imu_callback, 10)
		self.Cv2Image = None
		self.CvBridge = CvBridge()

	def listener_Img_callback(self, msg):
		self.get_logger().info('[Image]Subscribed: width %s' % msg.width)
		self.get_logger().info('[Image]Subscribed: height %s' % msg.height)
		# self.get_logger().info('[Image]Subscribed: data %s' % msg.data)
		self.Cv2Image = self.CvBridge.imgmsg_to_cv2(msg)

	def listener_Imu_callback(self, msg):
		self.get_logger().info('[IMU]Subscribed: linear %s' % msg.linear_acceleration)
		self.get_logger().info('[IMU]Subscribed: Angular %s' % msg.angular_velocity)

	def GetImage(self):
		return self.Cv2Image