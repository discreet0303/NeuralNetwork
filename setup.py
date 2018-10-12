import sys, os
from cx_Freeze import setup, Executable
# os.environ['TCL_LIBRARY'] = r'C:\Users\Hsuan\Anaconda3\envs\p35\tcl\tcl8.6'
# os.environ['TK_LIBRARY'] = r'C:\Users\Hsuan\Anaconda3\envs\p35\tcl\tk8.6'

# packages = ['tkinter']
packages = []
includes = []
include_files = [r"C:\Users\Hsuan\Anaconda3\envs\p35\DLLs\tcl86t.dll", \
                 r"C:\Users\Hsuan\Anaconda3\envs\p35\DLLs\tk86t.dll"]

options = {
    'build_exe': {
        "packages": packages, 
        "includes": includes,
        'include_files': include_files, 
    }
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('main.py', base = None)
]

setup(
    name = 'NeuralNetwork',
    version = '0.1',
    description = 'NeuralNetwork hw1',
    options = options,
    executables = executables
)
