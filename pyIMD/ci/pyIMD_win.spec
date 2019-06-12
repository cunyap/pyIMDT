# -*- mode: python -*-
# Main script to bundle pyIMD
# Author Andreas P. Cuny, andreas.cuny@bsse.ethz.ch
# Use the following command to build the executable with pyinstaller
# C:\\python35-x64\\Scripts pyinstaller.exe --noconsole --onefile C:\\projects\\pyimd\\pyIMD\pyIMD_win.spec

block_cipher = None

a = Analysis(['C:\\projects\\pyimd\\pyIMD\\main.py'],
             pathex=['C:\\python35-x64\\lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\python35-x64\\Scripts'],
             binaries=[],
             datas=[],
             hiddenimports=["tkinter", "tkinter.filedialog", "pandas._libs.tslibs.np_datetime","pandas._libs.tslibs.nattype","pandas._libs.skiplist",
			 "scipy.optimize", "scipy.optimize.minipack2", "pyIMD", "plotnine", "mizani", "palettable.colorbrewer", "statsmodels.tsa.statespace"],
             hookspath=['C:\\projects\\pyimd\\pyIMD\\ui\\hooks\\'],
             runtime_hooks=[],
             excludes=['jinja2'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)


a.datas += [('ui/icons/pyIMD_logo_icon.ico','C:\\projects\\pyimd\\pyIMD\\ui\\icons\\pyIMD_logo_icon.ico','DATA'),
            ('ui/icons/pyIMD_logo.png','C:\\projects\\pyimd\\pyIMD\\ui\\icons\\pyIMD_logo.png','DATA'),
            ('ui/icons/pyIMD_logo_vect.svg','C:\\projects\\pyimd\\pyIMD\\ui\\icons\\pyIMD_logo_vect.svg','DATA'),
			('ui/main_window.ui','C:\\projects\\pyimd\\pyIMD\\ui\\main_window.ui','DATA'),
			('ui/setting_dialog.ui','C:\\projects\\pyimd\\pyIMD\\ui\\setting_dialog.ui','DATA'),
			('imd.py','C:\\projects\\pyimd\\pyIMD\\imd.py','DATA'),
			('change_log.txt','C:\\projects\\pyimd\\pyIMD\\change_log.txt','DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pyIMD',
          debug=False,
          strip=False,
          upx=True,
          console=False,
		  icon='C:\\projects\\pyimd\\pyIMD\\ui\\icons\\pyIMD_logo_icon.ico')
