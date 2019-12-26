from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pyperclip as pc


def setup ( username, password ):
	dir = r"C:\Users\HP\Desktop\chromedriver_win32"
	chrome_driver_path = dir + "\chromedriver.exe"
	#options = webdriver.ChromeOptions ()
	#options.add_argument ('headless')
	#options.add_argument ('window-size=1200x600')
	#options.add_argument ("disable-gpu")
	driver = webdriver.Chrome (chrome_driver_path)# options=options)
	url = "https://codeforces.com/enter"
	driver.get (url)
	handle = driver.find_element_by_id ("handleOrEmail")
	passw = driver.find_element_by_id ("password")
	handle.send_keys (username)
	passw.send_keys (password)
	checkbox = driver.find_element_by_id ("remember")
	if (checkbox.is_selected ()):
		pass
	else:
		checkbox.click ()
	x = passw.submit ()
	time.sleep (2)
	return driver


language = [ "GNU G++14 6.4.0", "Java 1.8.0_162" ]


def start ( pathi, pathinp, lang ):
	file = open (pathi, "r")
	inp = open (pathinp, "r")
	# print(file.read())

	Username = ""
	Password = ""
	driver = setup (Username, Password)

	url = "https://codeforces.com/problemset/customtest"
	driver.get (url)
	checkbox= driver.find_elements_by_id ("toggleEditorCheckbox") [ 0 ]
	if(not checkbox.is_selected()):
		checkbox.click()
	driver.implicitly_wait(100)
	text_area = driver.find_element_by_id ("sourceCodeTextarea")
	text_area.clear ()
	text_area.click()
	code = file.read ()
	pc.copy(code)
	text_area.send_keys (Keys.CONTROL + 'v')
	test = driver.find_element_by_name ("input")
	input = inp.read ()
	test.clear()
	test.click()
	pc.copy(input)
	test.send_keys (Keys.CONTROL + 'v')

	driver.implicitly_wait (100)
	btn = driver.find_elements_by_name ("submit") [ 0 ]
	select = Select (driver.find_element_by_name ('programTypeId'))
	select.select_by_visible_text ('Haskell GHC 7.8.3 (2014.2.0.0)')

	select.select_by_visible_text (language [ 0 ] if lang == "c++" else language [ 1 ])
	driver.implicitly_wait (100)

	btn.submit ()

	driver.implicitly_wait (1000)

	time.sleep (2)

	textarea = driver.find_element_by_name ('output')
	output = 'Runn'
	driver.save_screenshot("scrn.png")
	while output [ :4 ] == 'Runn':
		try:
			# print the attribute of the textarea
			output = textarea.get_attribute ('value')
			o = output.replace ("\n", " ")
		except:
			pass
	end=output.find("=")
	print (output[:end])
	driver.close()
	driver.quit()


start (r"C:\Users\HP\Desktop\test.txt", r"C:\Users\HP\Desktop\inp.txt", "c++")
