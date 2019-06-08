#!/bin/bash
#
# execute with --user to make pip install in the user home
#
set -e

python3 -m pip install $USER PyInstaller

echo "# build the program"
echo "For the operating system" $1
if [ $1 == "linux" ];
then
cd /home/travis/build/cunyap/pyIMDT/
sudo apt-get install libgl1-mesa-glx
sudo /usr/lib64/
sudo cp -R /usr/lib/x86_64-linux-gnu/mesa/* /usr/lib64/
echo $(ls /usr/lib/)
echo $(ls /usr/lib64/*)
echo $(ls /usr/lib64/libGL*)
pip install .
python3 -m PyInstaller --noconsole --onefile --icon=/home/travis/build/cunyap/pyIMDT/pyIMD/ui/icons/pyIMD_logo_icon.ico /home/travis/build/cunyap/pyIMDT/pyIMD/build/pyIMD_unix.spec
PYIMD_APP="`pwd`/dist/pyIMD"
echo "The app can be found in \"$PYIMD_APP\"."
mv /home/travis/build/cunyap/pyIMDT/dist/pyIMD /home/travis/build/cunyap/pyIMDT/dist/pyIMD_x64_unix
echo $(ls /home/travis/build/cunyap/pyIMDT/dist/)
else
cd /Users/travis/build/cunyap/pyIMDT/
pip install .
python3 -m PyInstaller --noconsole --onefile /Users/travis/build/cunyap/pyIMDT/pyIMD/build/pyIMD_osx.spec

echo "# create the .dmg file"
# see http://stackoverflow.com/a/367826/1320237
PYIMD_DMG="`pwd`/dist/pyIMD.dmg"
rm -f "$PYIMD_DMG"
hdiutil create -srcfolder dist/pyIMD.app "$PYIMD_DMG"
mv /Users/travis/build/cunyap/pyIMDT/dist/pyIMD.dmg /Users/travis/build/cunyap/pyIMDT/dist/pyIMD_x64_osx.dmg
echo $(ls /Users/travis/build/cunyap/pyIMDT/dist/)
echo "The installer can be found in \"$PYIMD_DMG\"."
fi;

echo "# Done with compiling"
