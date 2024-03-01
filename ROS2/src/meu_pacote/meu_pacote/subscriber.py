import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from math import sqrt

class VelocidadeSubscriber(Node):

    def __init__(self):
        super().__init__('velocidade_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            '/velocidade',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        modulo_linear = sqrt(msg.linear.x**2 + msg.linear.y**2 + msg.linear.z**2)
        modulo_angular = sqrt(msg.angular.x**2 + msg.angular.y**2 + msg.angular.z**2)

        self.get_logger().info(f'Modulos:\nModulo Linear: {modulo_linear:.2f}\nModulo Angular: {modulo_angular:.2f}')
        

def main(args=None):
    rclpy.init(args=args)

    velocidade_subscriber = VelocidadeSubscriber()

    rclpy.spin(velocidade_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    velocidade_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()