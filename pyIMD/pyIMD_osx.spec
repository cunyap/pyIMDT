# -*- mode: python -*-
# Main script to bundle pyIMD on OSX.
# Author Andreas P. Cuny, andreas.cuny@bsse.ethz.ch
# Use the following command to build the executable with pyinstaller and adjust the file paths first according to your installation.
# PyInstaller --noconsole --onefile /Users/localadmin//pyIMD/pyIMD/ui/pyIMD_osx.spec

block_cipher = None

a = Analysis(['/Users/gflaesch/PycharmProjects/test/pyIMD/pyIMD/main.py'],
            pathex=['/Users/gflaesch/PycharmProjects/PyIMDWithMiniConda/lib/python3.6/site-packages/PyQt5', '/Users/gflaesch/PycharmProjects/PyIMDWithMiniConda/lib/python3.6/site-packages'],
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

hookspath=['/Users/gflaesch/PycharmProjects/test/pyIMD/pyIMD/ui/hooks/']

a.datas += [('ui/icons/pyimd_logo2_01_FNf_icon.ico','/Users/gflaesch/PycharmProjects/test/pyIMD/pyIMD/ui/icons/pyimd_logo2_01_FNf_icon.ico','DATA'),
            ('ui/icons/pyIMD_Logo2-01.png','C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\ui\\icons\\pyIMD_Logo2-01.png','DATA'),
            ('ui/icons/pyIMD_Logo-01.svg','C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\ui\\icons\\pyIMD_Logo-01.svg','DATA'),
            ('ui/main_window.ui','/Users/gflaesch/PycharmProjects/test/pyIMD/pyIMD/ui/main_window.ui','DATA'),
            ('ui/setting_dialog.ui','/Users/gflaesch/PycharmProjects/test/pyIMD/pyIMD/ui/setting_dialog.ui','DATA'),
            ('imd.py','/Users/gflaesch/PycharmProjects/test/pyIMD/pyIMD/imd.py','DATA'),
            ('change_log.txt','C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\change_log.txt','DATA'),
		    ('palettable/colorbrewer/data/colorbrewer_all_schemes.json', '/Users/gflaesch/anaconda3/lib/python3.6/site-packages/palettable/colorbrewer/data/colorbrewer_all_schemes.json', 'DATA')]

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
          icon='/Users/gflaesch/PycharmProjects/test/pyIMD/pyIMD/ui/icons/pyimd_logo2_01_FNf_icon.ico')

app = BUNDLE(exe,
         name='pyIMD.app',
         icon='/Users/gflaesch/PycharmProjects/test/pyIMD/pyIMD/ui/icons/pyIMD_Logo-01.png',
         bundle_identifier=None,
         info_plist={'NSHighResolutionCapable': 'True'},
         )
