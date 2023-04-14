from setuptools import setup

package_name = 'pozyx_listener'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='melchior',
    maintainer_email='koroyeldiores@gmail.com',
    description='Simple Package to get position Data from pozyx Access point',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'xyz_publisher = pozyx_listener.xyz_publisher:main'
        ],
    },
)
