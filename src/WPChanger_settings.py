import os
import sys
import shutil
import string
import platform
import traceback
import configparser
from colorama import init
from colorama import Fore
init()


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def main(message=None):
	clearConsole()
	if message != None:
		print(Fore.YELLOW + message.center(shutil.get_terminal_size().columns) + Fore.WHITE)
	config = configparser.ConfigParser()
	test = config.read("config.ini")
	try:
		_ = config["DEFAULT"]["images"]
		menu()
	except:
		add_wallpapers()


def menu():
	clearConsole()
	print(
		"\nВведите число, соответствующее нужному действию:".center(shutil.get_terminal_size().columns),
		"1 | Добавить обои".center(shutil.get_terminal_size().columns),
		"2 | Удалить все обои".center(shutil.get_terminal_size().columns),
		"3 | Редактировать время смены обоев".center(shutil.get_terminal_size().columns)
		)
	action = input("> ")
	try:
		action = int(action)
	except:
		main("Необходимо ввести число.")
	if action == 1:
		add_wallpapers()
	elif action == 2:
		del_wallpapers()
	elif action == 3:
		edit_time()
	else:
		main("Действия не существует.")


def add_wallpapers():
	clearConsole()
	old_names = None
	config = configparser.ConfigParser()
	config.read("config.ini")
	old_names = config["DEFAULT"]["images"].split(", ")
	print(
		'Добавление обоев (старые при этом сохраняются).'.center(shutil.get_terminal_size().columns),
		'Введите названия файлов добавленных обоев через запятую (с расширением).'.center(shutil.get_terminal_size().columns),
		'Например:'.center(shutil.get_terminal_size().columns),
		'winter.jpg, spring.png и т.д.'.center(shutil.get_terminal_size().columns),
		)
	names = input("> ")
	names = names.split(", ")
	print(
		'Будут добавлены следующие файлы:'.center(shutil.get_terminal_size().columns)
		)
	for name in names:
		print(name.center(shutil.get_terminal_size().columns))
	print('Вы уверены, что хотите продолжить? (y/n)'.center(shutil.get_terminal_size().columns))
	confirm = input("> ")
	if confirm.lower() == "y" or confirm.lower() == "д":
		if old_names != None:
			for old_name in old_names:
				names.append(old_name)
		config['DEFAULT'] = {"images": ", ".join(names)[:-1]}
		with open('config.ini', 'w') as configfile:
			config.write(configfile)
	else:
		main("Добавление отменено.")
	


"""
	scheduler = BaseScheduler()

	scheduler.add_job(id="wallpapers_changer_1", func=set_wallpaper, hour=change_time_1, trigger='cron')
	scheduler.add_job(id="wallpapers_changer_2", func=set_wallpaper, hour=change_time_2, trigger='cron')

	scheduler.run_until_stopped()



def set_wallpaper():
	wallpapers = 
	#Check the operating system
	system_name = platform.system().lower()
	path = os.getcwd()+'\\images\\{wallpaper_name}.jpg'
	ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

"""


try:
	main()
except KeyboardInterrupt:
	sys.exit(0)
except:
	traceback.format_exc()