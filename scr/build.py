from os import system, remove, rmdir
from shutil import rmtree, move
name = 'gui4.py'
newName = name[:name.rfind('.')] + '.exe'
icon = 'D:\\Sicily\\lib\\icon.ico'
com = 'pyinstaller {} --noconsole --onefile --icon={}'.format(name, icon)
system(com)
rmtree('__pycache__')
rmtree('build')
remove(name[:name.rfind('.')] + '.spec')
move('dist\\{}'.format(newName), newName)
rmdir('dist')
print('OK')