# -*- mode: python -*-
# Main script to bundle pyIMD
# Author Andreas P. Cuny, andreas.cuny@bsse.ethz.ch
# Use the following command to build the executable with pyinstaller
# C:\\Python35-3-3-64\\Scripts pyinstaller.exe --noconsole --onefile C:\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\ui\\pyIMD.spec

block_cipher = None

a = Analysis(['C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\main.py'],
             pathex=['C:\\Python35-3-3-64\\lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Python35-3-3-64\\Scripts'],
             binaries=[],
             datas=[],
             hiddenimports=["tkinter", "tkinter.filedialog", "pandas._libs.tslibs.np_datetime","pandas._libs.tslibs.nattype","pandas._libs.skiplist", 
			 "scipy.optimize", "scipy.optimize.minipack2" "pyIMD", "plotnine", "mizani", "palettable.colorbrewer", "statsmodels.tsa.statespace"],
             hookspath=['C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\ui\\hooks\\'],
             runtime_hooks=[],
             excludes=['jinja2'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
			  
	 
a.datas += [('ui/icons/pyimd_logo2_01_FNf_icon.ico','C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\ui\\icons\\pyimd_logo2_01_FNf_icon.ico','DATA'),
			('ui/main_window.ui','C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\ui\\main_window.ui','DATA'),
			('ui/setting_dialog.ui','C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\ui\\setting_dialog.ui','DATA'),
			('inertialmassdetermination.py','C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\inertialmassdetermination.py','DATA')]
			    			 			 
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pyIMD',
          debug=True,
          strip=False,
          upx=True,
          console=True,
		  icon='C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\ui\\icons\\pyimd_logo2_01_FNf_icon.ico')
