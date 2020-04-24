# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['StarMapGen.py'],
             pathex=['C:\\Users\\dagor\\source\\repos\\StarMapGen\\StarMapGen\\src'],
             binaries=[('C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python37_64\\Lib\\site-packages\\wx\\libcairo-2.dll', '.')],
             datas=[('..\\images\\BannerMap.svg', '.'), ('C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python37_64\\Lib\\site-packages\\cairocffi\\VERSION', 'cairocffi')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='StarMapGen',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
