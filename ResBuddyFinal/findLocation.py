from selenium import webdriver

def scrapper(url):
	url=url.lower()
	googlemapUrl="https://www.google.com/maps/search/"

	option = webdriver.ChromeOptions()
	prefs = {'profile.default_content_setting_values': {'images':2, 'javascript':2}} # for faster loading of webpages
	option.add_experimental_option('prefs', prefs)

	driver = webdriver.Chrome("C:\\Users\\Abhinaba\\Downloads\\chromedriver.exe", options=option)
	driver.get(googlemapUrl+url)
	string=driver.find_element_by_css_selector('meta[itemprop=image]').get_attribute('content')
	driver.close()

	if string.find('&zoom=')==False:
		return "Invalid"
	else:
		x=string.split('?center=')[1].split('&zoom=')[0].split('%2C')[0]
		y=string.split('?center=')[1].split('&zoom=')[0].split('%2C')[1]

		return x,y


"""for debug purposes
if __name__=="__main__":
	x,y=scrapper("parkstreet")
	print(x," ",y)
"""