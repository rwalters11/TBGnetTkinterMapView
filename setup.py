from setuptools import setup

# Update on pypi:
#
# 1. delete old /dist
# 2  increase both version numbers
# 3. python3.10 -m pip install --upgrade build
# 4. python3.10 -m build
# 5. python3.10 -m twine upload dist/*

setup(name="tbgnettkintermapview",
      version="1.29.0.1",
      author="Richard Walters",
      license="Creative Commons Zero v1.0 Universal",
      url="https://github.com/TomSchimansky/TkinterMapView",
      description="Customised version of a python Tkinter widget to display image tile maps like OpenStreetMap or Satellite Images.",
      long_description_content_type="text/markdown",
      long_description="**Detailed Information: https://github.com/TomSchimansky/TkinterMapView**",
      packages=["tbgnettkintermapview"],
      classifiers=["Operating System :: OS Independent",
                   "Programming Language :: Python :: 3",
                   "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"],
      install_requires=["geocoder", "pillow", "requests", "pyperclip", 'pywin32; platform_system=="Windows"', "customtkinter"],
      python_requires=">=3.6")
