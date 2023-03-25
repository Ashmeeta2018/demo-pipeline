from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="ashok",
      author_email="bhatta_ashu@hotmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )
