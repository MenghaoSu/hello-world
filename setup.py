from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30830",
      url="",
      author="Menghao Su",
      author_email="menghao.su@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30830_systeminfo=systeminfo.main:main']
          }
      )
      