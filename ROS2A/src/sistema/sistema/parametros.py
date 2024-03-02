import rclpy
from rclpy.node import Node

class Parametro(Node):
    def __init__(self):
        super().__init__('parametro_node')

        self.declare_parameter('Terra', {})
        terra_params = self.get_parameter('Terra').value
        self.Terra_RaioOrbita = terra_params.get('RaioOrbita', 0)
        self.Terra_SateliteRaioOrbita = terra_params.get('SateliteTerra', 0)

        self.get_logger().info(f'Raio da Terra: {self.Terra_RaioOrbita}')
        self.get_logger().info(f'Raio do Satélite da Terra: {self.Terra_SateliteRaioOrbita}')
         
def main(args=None):
    rclpy.init(args=args)
    parametro = Parametro()
    rclpy.spin(parametro)
    parametro.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
