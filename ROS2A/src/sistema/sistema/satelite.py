import math
import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

class SateliteNode(Node):
    def __init__(self):
        super().__init__('Satelite')
        self.broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.transform_broadcast)

    def transform_broadcast(self):
        parameters = self.get_parameters(['Terra_SateliteRaioOrbita'])
        raiosatelite = parameters['Terra_SateliteRaioOrbita'].value
        angulo = self.get_clock().now().to_msg().sec * 2 * math.pi
        x = raiosatelite * math.cos(angulo)
        y = raiosatelite * math.sin(angulo)

        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'Terra' 
        t.child_frame_id = 'Satelite' 
        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        self.broadcaster.sendTransform(t)

def main():
    rclpy.init()
    node = SateliteNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()
