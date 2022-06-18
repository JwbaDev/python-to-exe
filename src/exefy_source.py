import os, shutil, time, sys

os.system('pip install -q pyinstaller')

os.system('cls' if os.name == 'nt' else 'clear')
name = input('Name > ')

os.system('cls' if os.name == 'nt' else 'clear')
os.system(f'pyinstaller --noconfirm --onefile --console --icon "./icon.ico" --name "{name}"  "./main.py"')


shutil.rmtree('build')
for file in next(os.walk(os.getcwd()), (None, None, []))[2]:
	if file[-1] == "c":
		os.remove(file)
try:
	os.replace(f"dist/{name}.exe", f"./{name}.exe")
	shutil.rmtree('dist')
except:
	pass

os.system('cls')
print('exefyied successfully')
time.sleep(2)
sys.exit()
