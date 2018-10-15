# put the dataSet in the same folder 
# run 'pyinstaller mainOneFile.spec'

block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['D:\\Homework\\NeuralNetwork'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))

    return extra_datas

# append the 'data' dir
a.datas += extra_datas('dataSet')

pyz = PYZ(
    a.pure, 
    a.zipped_data,
    cipher = block_cipher
)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='main',
    debug=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False 
)