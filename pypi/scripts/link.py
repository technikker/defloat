import os
from pathlib import Path

DIR = Path(__file__).parent
PROJECT = DIR
while PROJECT.name != "unfloat":
	PROJECT = PROJECT.parent

TMP = PROJECT / "pypi/.tmp"

# todo see if this is more dynamic with the DirTree?
LINKS = (
	(PROJECT / "docs", TMP / "docs"),
	(PROJECT / "lib/defloat.py", TMP / "defloat.py"),
	(PROJECT / "meta/LICENSE", TMP / "LICENSE"),
	(PROJECT / "meta/README.rst", TMP / "README.rst"),
	# (PROJECT / "pypi/scripts", TMP / "pypi/scripts"),
	(PROJECT / "pypi/setup.py", TMP / "setup.py"),
	# (PROJECT / "pypi/version.txt", TMP / "version.txt"),
	(PROJECT / "tests", TMP / "tests"),
)

for src, dst in LINKS:
	os.makedirs(dst.parent, exist_ok=True)
	print(f"{src} -> {dst}")
	if dst.exists():
		# make sure a link that exists is the correct one
		assert dst.resolve() == src
	else:
		os.symlink(src, dst)


if __name__ == '__main__':
	pass
