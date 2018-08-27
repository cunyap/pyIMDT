# -*- mode: python -*-
# Main script to bundle pyIMD on OSX.
# Author Andreas P. Cuny, andreas.cuny@bsse.ethz.ch
# Use the following command to build the executable with pyinstaller and adjust the file paths first according to your installation.
# PyInstaller --noconsole --onefile /Users/localadmin//pyIMD/pyIMD/ui/pyIMD_osx.spec

block_cipher = None

a = Analysis(['/Users/localadmin/pyIMD/pyIMD/main.py'],
             pathex=['/Users/localadmin/miniconda3/lib/python3.6/site-packages/PyQt5', '/Users/localadmin/miniconda3/lib/python3.6/site-packages/'],
            binaries=[],
             datas=[],
             hiddenimports=["PyQt5", "numpy", "PyQt5.QtWidgets", "PyQt5.sip", "platinfo", "tkinter", "tkinter.filedialog", "pandas._libs.tslibs.np_datetime","pandas._libs.tslibs.nattype","pandas._libs.skiplist",
							"scipy.optimize", "scipy.optimize.minipack2", "pyIMD", "plotnine", "mizani", "palettable.colorbrewer", "statsmodels", "statsmodels.tsa.statespace._filters",
							"statsmodels.tsa.statespace._filters._conventional", "statsmodels.tsa.statespace._filters._inversions",  "statsmodels.tsa.statespace._filters._univariate",
							"statsmodels.tsa.statespace._smoothers", "statsmodels.tsa.statespace._smoothers._alternative", "statsmodels.tsa.statespace._smoothers._classical",
							"statsmodels.tsa.statespace._smoothers._conventional", "statsmodels.tsa.statespace._smoothers._univariate", "scipy._lib.messagestream", "palettable"],
             runtime_hooks=[],
             excludes=['jinja2'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

hookspath=['/Users/localadmin/pyIMD/pyIMD/ui/hooks/']

a.datas += [('ui/icons/pyimd_logo2_01_FNf_icon.ico','/Users/localadmin/pyIMD/pyIMD/ui/icons/pyimd_logo2_01_FNf_icon.ico','DATA'),
         ('ui/main_window.ui','/Users/localadmin/pyIMD/pyIMD/ui/main_window.ui','DATA'),
         ('ui/setting_dialog.ui','/Users/localadmin/pyIMD/pyIMD/ui/setting_dialog.ui','DATA'),
         ('inertialmassdetermination.py','/Users/localadmin/pyIMD/pyIMD/inertialmassdetermination.py','DATA'),
		 ('palettable/colorbrewer/data/colorbrewer_all_schemes.json', '/Users/localadmin/miniconda3/lib/python3.6/site-packages/palettable/colorbrewer/data/colorbrewer_all_schemes.json', 'DATA')]

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
        icon='/Users/localadmin/pyIMD/pyIMD/ui/icons/pyimd_logo2_01_FNf_icon.ico')


app = BUNDLE(exe,
         name='pyIMD.app',
         icon='/Users/localadmin/pyIMD/pyIMD/ui/icons/pyIMS_Logo-01.png',
         bundle_identifier=None,
         info_plist={'NSHighResolutionCapable': 'True'},
         )
