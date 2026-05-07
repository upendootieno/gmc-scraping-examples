import requests
from bs4 import BeautifulSoup # class

# classes have attributes, methods

class Countries:
	def __init__(self, capital: str, population: int, area: float):
		self.capital = capital
		self.population = population
		self.area = area


def get_countries_html():
	print("Fetching page")
	response = requests.get("https://www.scrapethissite.com/pages/simple/") # Returns a response object
	# Request object has .get() method
	# Response objects -> status_code, text attributes

	if response.status_code == 200:
		return response.text
	else:
		print("Getting content failed")


def parse_html(html: str):
	print("Parsing page")
	soup = BeautifulSoup(html, 'html.parser') # object
	countries_html = soup.select('.col-md-4') # method
	# Returns a list of html elements

	country_list = []
	# We initialize an empty list to store the
	# values we will extract from the HTML

	for c in countries_html:
		country_name_html = c.select_one("h3")
		country_dict = {
		"name": country_name_html.get_text()
		}
		country_list.append(country_dict)

	return country_list


print(parse_html(get_countries_html()))

