## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['strands_admin_web_ui'],
    scripts=['scripts/strands_admin_web_ui_node.py'],
    package_dir={'': 'src'})

setup(**setup_args)
