from setuptools import setup
from pathlib import Path

DIR = Path(__file__).parent

NAME = "DeFloat"
DESC = 'Portable Floating Point Decomposition'
SRC_URL = "https://github.com/technikker/defloat"


# VER = open(DIR / "version.txt").read().strip()
# ^^ not allowed to do this apparently (thanks setuptools)
VER = "0.0.1"
README = open(DIR / "README.rst").read()


# Setting up
setup(
	name=NAME,
	version=VER,
	author="techniker",
	author_email="<mail@xxxxxxxx.com>",
	description=DESC,
	# text/plain
	# text/x-rst
	# text/markdown
	long_description_content_type="text/x-rst",
	long_description=README,
	url=SRC_URL,
	project_urls={
		"Source": SRC_URL,
	},
	license='MPL',
	license_files=["LICENSE", ],
	# packages=[find_packages(), ],  # doesn't work for single file modules
	py_modules=["defloat", ],
	install_requires=[],  # ['opencv-python', 'pyautogui', 'pyaudio'],
	keywords=[
		'python', NAME, 'float', 'floating', 'point', 'decompose',
		"decomposition", "portable"],
	classifiers=[
		# 1 - Planning
		# 2 - Pre-Alpha
		# 3 - Alpha
		# 4 - Beta
		# 5 - Production/Stable
		# 6 - Mature
		# 6 - Inactive
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
		"Programming Language :: Python :: 3",
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
		'Programming Language :: Python :: 3.12',
		'Operating System :: OS Independent',
		# "Operating System :: Unix",
		# "Operating System :: MacOS :: MacOS X",
		# "Operating System :: Microsoft :: Windows",
		'Topic :: Software Development :: Embedded Systems',
		"Topic :: Scientific/Engineering",
		"Topic :: Utilities",
	]
)
