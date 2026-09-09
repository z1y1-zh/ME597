import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'task_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	( os.path.join('share', package_name, 'launch'),
          glob('launch/*.py')
    ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='me597',
    maintainer_email='jenny_zhaozy@hotmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	    'talker = task_2.joint_publisher:main',
	    'listener = task_2.joint_subscriber:main',
	    'service = task_2.joint_service:main',
	    'client = task_2.joint_client:main',
        ],
    },
)
