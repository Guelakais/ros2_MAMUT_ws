command to create a package:
ros2 pkg create <package_name> --build-type ament_python
additional flags:
--build-type: For example:
	--build-type ament_python
	--build-type ament_cmake
--node-name: all nodes you want inside the package
--dependencies: all dependencies, you want.
