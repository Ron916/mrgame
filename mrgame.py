import sys
from engine import Engine

paths = [
    '/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python35.zip',
    '/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5',
    '/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/plat-darwin',
    '/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/lib-dynload',
    '/usr/local/lib/python3.5/site-packages',
]

sys.path = paths + sys.path

if __name__ == '__main__':
    engine = Engine()
    engine.game_loop()
