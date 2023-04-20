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
    maintainer='Guelakais',
    maintainer_email='koroyeldiores@gmail.com',
    description='TODO: Package description',
    license='MIT_License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'position_publisher = pozyx_listener.position_publisher:main'
        ],
    },
)
