import pip._internal as pipint

_all_ = [
    "feedparser>=5.2.1",
    "ObjectListView>=1.3.1",
]

windows = [
    "wxPython>=4.0.3",
    ]

darwin = [
    "wxPython>=4.0.3",
    ]

linux = []

def install(packages):
    for package in packages:
        print("Установка: " + package)
        pipint.main(['install', "-U", package])

if __name__ == '__main__':
    print("Установка зависимостей")
    from sys import platform

    print("Установка общих зависимостей")
    install(_all_)
    if platform == 'windows' or platform == 'win32':
        print("Установка зависимостей для Windows")
        install(windows)
    if platform == 'darwin':
        print("Установка зависимостей для MacOS")
        install(darwin)
    if platform.startswith('linux'):
        print("Установка зависимостей для Linux")
        install(linux)
        pipint.main(['install', '-U' '-f' 'https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04', 'wxPython'])
