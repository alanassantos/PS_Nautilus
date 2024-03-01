import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class VelocidadePublisher(Node):

    def __init__(self):
        super().__init__('velocidade_publisher')
        self.publisher_ = self.create_publisher(Twist, '/velocidade', 10)
        timer_period = 0.5 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
    

    def timer_callback(self):
        msg = Twist()
        # Velocidades lineares e angulares aleatórias (-1.0 e 1.0)
        msg.linear.x= random.uniform(-1.0,1.0)
        msg.linear.y = random.uniform(-1.0,1.0)
        msg.linear.z= random.uniform(-1.0,1.0)
        msg.angular.x = random.uniform(-1.0,1.0)
        msg.angular.y = random.uniform(-1.0,1.0)
        msg.angular.z = random.uniform(-1.0,1.0)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "linear: ({ msg.linear.x:.2f}, { msg.linear.y:.2f}, { msg.linear.z:.2f}), angular: ({msg.angular.x:.2f}, {msg.angular.y:.2f}, {msg.angular.z:.2f})"')        

def main(args=None):
    rclpy.init(args=args)

    velocidade_publisher  = VelocidadePublisher()

    rclpy.spin(velocidade_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    velocidade_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()