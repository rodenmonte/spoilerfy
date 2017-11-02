from setuptools import setup

setup(name='spoilerfy',
      version='1.0',
      description='Format your code for /r/dailyprogrammer',
      url='https://www.github.com/rodenmonte/spoilerfy',
      author='Monte Roden',
      author_email='rodenmonte@gmail.com',
      license='MIT',
      packages=['spoilerfy'],
      install_requires=[
        'pyperclip'
      ],
      zip_safe=False,
      entry_points = {
        'console_scripts': ['spoilerfy=spoilerfy.command_line:main']
      })
