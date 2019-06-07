#!/bin/bash
#
# execute with --user to make pip install in the user home
#
set -e

python3 -m pip install $USER PyInstaller==3.3.1
cd /home/travis/build/cunyap/pyIMDT/
pip install .

echo "# build the program"
# see https://pythonhosted.org/PyInstaller/usage.html
if [ "$1" == "linux"]
then
python3 -m PyInstaller --noconsole --onefile --icon=/home/travis/build/cunyap/pyIMDT/pyIMD/ui/icons/pyIMD_logo_icon.ico /home/travis/build/cunyap/pyIMDT/pyIMD/build/pyIMD_unix.spec
else
python3 -m PyInstaller --noconsole --onefile /home/travis/build/cunyap/pyIMDT/pyIMD/build/pyIMD_osx.spec
fi

echo "# create the .exe file"
# see http://stackoverflow.com/a/367826/1320237
echo $(ls -la /home/travis/build/cunyap/pyIMDT/dist/)
PYIMD_EXE="`pwd`/dist/pyIMD.exe"
rm -f "$PYIMD_EXE"
#hdiutil create -srcfolder dist/pyIMD_unix_x64.exe "$PYIMD_EXE"
#mkdir dist/pyIMD_unix_x64.exe "$PYIMD_EXE"

echo "The installer can be found in \"$PYIMD_EXE\"."
