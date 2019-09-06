#import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_button_should_be_present(browser):
	browser.get(link)
	add_button = 0
	#time.sleep(10)
	try:
		add_button = browser.find_element_by_css_selector(".btn-add-to-basket")
	
	finally:
		assert add_button, "Add button shoul be present"