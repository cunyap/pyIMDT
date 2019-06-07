# -*- mode: python -*-
# Main script to bundle pyIMD on OSX.
# Author Andreas P. Cuny, andreas.cuny@bsse.ethz.ch
# Use the following command to build the executable with pyinstaller and adjust the file paths first according to your installation.
# PyInstaller --noconsole --onefile /home/travis/build/cunyap/pyIMDT/pyIMD/build/pyIMD_osx.spec

block_cipher = None

a = Analysis(['/home/travis/build/cunyap/pyIMDT/pyIMD/main.py'],
            pathex=['/home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/PyQt5', '/home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages'],
            binaries=[],
             datas=[],
             hiddenimports=["PyQt5", "numpy", "PyQt5.QtWidgets", "PyQt5.sip", "platinfo", "tkinter", "tkinter.filedialog", "pandas._libs.tslibs.np_datetime","pandas._libs.tslibs.nattype","pandas._libs.skiplist",
							"scipy.optimize", "scipy.optimize.minipack", "pyIMD", "plotnine", "mizani", "palettable.colorbrewer", "statsmodels", "statsmodels.tools", "statsmodels.tsa.statespace._filters",
							"statsmodels.tsa.statespace._filters._conventional", "statsmodels.tsa.statespace._filters._inversions",  "statsmodels.tsa.statespace._filters._univariate",
							"statsmodels.tsa.statespace._smoothers", "statsmodels.tsa.statespace._smoothers._alternative", "statsmodels.tsa.statespace._smoothers._classical",
							"statsmodels.tsa.statespace._smoothers._conventional", "statsmodels.tsa.statespace._smoothers._univariate", "scipy._lib.messagestream", "palettable","statsmodels.__init__"],
             runtime_hooks=[],
             excludes=['jinja2'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

hookspath=['/home/travis/build/cunyap/pyIMDT/pyIMD/ui/hooks/']

a.datas += [('ui/icons/pyIMD_logo_icon.ico','/home/travis/build/cunyap/pyIMDT/pyIMD/ui/icons/pyIMD_logo_icon.ico','DATA'),
            ('ui/icons/pyIMD_logo.png','/home/travis/build/cunyap/pyIMDT/pyIMD/ui/icons/pyIMD_logo.png','DATA'),
            ('ui/icons/pyIMD_logo.svg','/home/travis/build/cunyap/pyIMDT/pyIMD/ui/icons/pyIMD_logo.svg','DATA'),
            ('ui/main_window.ui','/home/travis/build/cunyap/pyIMDT/pyIMD/ui/main_window.ui','DATA'),
            ('ui/setting_dialog.ui','/home/travis/build/cunyap/pyIMDT/pyIMD/ui/setting_dialog.ui','DATA'),
            ('imd.py','/home/travis/build/cunyap/pyIMDT/pyIMD/imd.py','DATA'),
            ('change_log.txt','/home/travis/build/cunyap/pyIMDT/pyIMD/ui/icons/change_log.txt','DATA'),
		    ('palettable/colorbrewer/data/colorbrewer_all_schemes.json', '/home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/palettable/colorbrewer/data/colorbrewer_all_schemes.json', 'DATA')]

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
          console=True,
          icon='/home/travis/build/cunyap/pyIMDT/pyIMD/ui/icons/pyIMD_logo_icon.ico')

app = BUNDLE(exe,
         name='pyIMD.app',
         icon='/home/travis/build/cunyap/pyIMDT/pyIMD/ui/icons/pyIMD_logo-01.png',
         bundle_identifier=None,
         info_plist={'NSHighResolutionCapable': 'True'},
         )
