### bevore ROS is started on the robot:
sudo chmod a+rw /dev/ttyACM0 -> the opencrBoard
sudo chmod a+rw /dev/ttyUSB0 -> the Lidar Sensor
### to start ROS on the robot:
ros2 launch turtlebot3_bringup robot.launch.py
### to teleop the robot: 
ros2 run turtlebot3_teleop teleop_keyboard
sudo chmod a+rw /dev/ttyACM0; sudo chmod a+rw /dev/ttyUSB0
