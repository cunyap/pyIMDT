#!/bin/bash
#
# execute with --user to make pip install in the user home
#
set -e

echo "# build the program"
# see https://pythonhosted.org/PyInstaller/usage.html
python3 -m pyinstaller --noconsole --onefile --icon=/home/travis/build/cunyap/pyIMDT/pyIMD/ui/icons/pyIMD_logo_icon.ico /home/travis/build/cunyap/pyIMDT/pyIMD/build/pyIMD_unix.spec

echo "# create the .exe file"
# see http://stackoverflow.com/a/367826/1320237
PYIMD_EXE="`pwd`/dist/KnitEditor.exe"
rm -f "$PYIMD_EXE"
hdiutil create -srcfolder dist/pyIMD_unix_x64.exe "$PYIMD_EXE"

echo "The installer can be found in \"$PYIMD_EXE\"."
