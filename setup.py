from setuptools import setup

setup(name='spoilerfy',
      version='0.11',
      description='Put 4 spaces in front of each line, then copy those lines to your clipboard.',
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
