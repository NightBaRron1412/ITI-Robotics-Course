from launch import LaunchDescription
from launch_ros.actions import Node
from math import pi


def generate_launch_description():
    ld = LaunchDescription()

    gps_link = Node(

        package="tf2_ros",

        executable="static_transform_publisher",

        arguments=["--x", "0", "--y", "0", "--z", "1.77",
                   "--yaw", "0", "--pitch", "0", "--roll", "0",
                   "--frame-id", "base_footprint", "--child-frame-id", "gps_link"]
    )

    lidar_link = Node(

        package="tf2_ros",

        executable="static_transform_publisher",

        arguments=["--x", "1.92", "--y", "0", "--z", "0.36",
                   "--yaw", "0", "--pitch", "0", "--roll", "0",
                   "--frame-id", "base_footprint", "--child-frame-id", "lidar_link"]
    )

    zed2_link = Node(

        package="tf2_ros",

        executable="static_transform_publisher",

        arguments=["--x", "1.8", "--y", "-0.03", "--z", "1",
                   "--yaw", "0", "--pitch", "0", "--roll", "0",
                   "--frame-id", "base_footprint", "--child-frame-id", "zed2_link"]
    )

    mynt_link = Node(

        package="tf2_ros",

        executable="static_transform_publisher",

        arguments=["--x", "-0.1", "--y", "0", "--z", "0.88",
                   "--yaw", "0", "--pitch", f"{pi}", "--roll", "0",
                   "--frame-id", "base_footprint", "--child-frame-id", "mynt_link"]
    )

    imu_link = Node(

        package="tf2_ros",

        executable="static_transform_publisher",

        arguments=["--x", "1.8", "--y", "-0.5", "--z", "1",
                   "--yaw", f"{pi / 2}", "--pitch", "0", "--roll", "0",
                   "--frame-id", "base_footprint", "--child-frame-id", "imu_link"]
    )

    ld.add_action(gps_link)
    ld.add_action(lidar_link)
    ld.add_action(zed2_link)
    ld.add_action(mynt_link)
    ld.add_action(imu_link)

    return ld
