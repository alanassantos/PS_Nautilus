import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('sistema'),
        'config',
        'param.yaml'
    )    

    return LaunchDescription([

        Node(
            package="sistema",
            executable="estrela",
            name="estrela",
        ),

        Node(
            package="sistema",
            executable="planeta",
            name="planeta",
        ),

        Node(
            package="sistema",
            executable="satelite",
            name="satelite",
        ),
        
        Node(
            package="sistema",
            executable="parametros",
            name="parametros",
            parameters = [config]
        )

    ])
