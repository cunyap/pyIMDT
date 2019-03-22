# -*- mode: python -*-
# Main script to bundle pyIMD
# Author Andreas P. Cuny, andreas.cuny@bsse.ethz.ch
# Use the following command to build the executable with pyinstaller
# pyinstaller --noconsole --onefile /home/andreascuny/Documents/pyimd/pyIMD/pyIMD_unix.spec

block_cipher = None

a = Analysis(['/home/andreascuny/Documents/pyimd/pyIMD/main.py'],
             pathex=['/home/andreascuny/Documents/miniconda/lib/python3.6/site-packages/PyQt5/Qt/bin'],
             binaries=[],
             datas=[],
             hiddenimports=["tkinter", "tkinter.filedialog", "pandas._libs.tslibs.np_datetime","pandas._libs.tslibs.nattype","pandas._libs.skiplist", 
			 "scipy.optimize", "scipy.optimize.minipack2" "pyIMD", "plotnine", "mizani", "palettable.colorbrewer", "statsmodels.tsa.statespace"],
             hookspath=['/home/andreascuny/Documents/pyimd/pyIMD/ui/hooks/'],
             runtime_hooks=[],
             excludes=['jinja2'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
			  
	 
a.datas += [('ui/icons/pyimd_logo_icon.ico','/home/andreascuny/Documents/pyimd/pyIMD/ui/icons/pyimd_logo_icon.ico','DATA'),
            ('ui/icons/pyIMD_logo.png','/home/andreascuny/Documents/pyimd/pyIMD/ui/icons/pyIMD_logo.png','DATA'),
            ('ui/icons/pyIMD_logo_vect.svg','/home/andreascuny/Documents/pyimd/pyIMD/ui/icons/pyIMD_logo_vect.svg','DATA'),
			('ui/main_window.ui','/home/andreascuny/Documents/pyimd/pyIMD/ui/main_window.ui','DATA'),
			('ui/setting_dialog.ui','/home/andreascuny/Documents/pyimd/pyIMD/ui/setting_dialog.ui','DATA'),
			('imd.py','/home/andreascuny/Documents/pyimd/pyIMD/imd.py','DATA'),
			('change_log.txt','/home/andreascuny/Documents/pyimd/pyIMD/change_log.txt','DATA')]
			    			 			 
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
		  icon='/home/andreascuny/Documents/pyimd/pyIMD/ui/icons/pyimd_logo_icon.ico')
