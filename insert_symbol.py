

def obtain_parse_wiki_snp500():

# Download and parse the wikipedia list of s&p500 
# constituents using requests and BeautifulSoup.
# Returns a list of tuples for to add to MySQL.

	# Stores the current time ,for the created_at record
	now = datetime.datetime.utcnow()
	# Use requests and BeautifulSoup to download the
	# list of s&p500 companies and obtain the symbol table
	response = requests.get("http://en.wikipedia.org/wiki/List_of_s%26p_500_companies")
	soup = bs4.BeautifulSoup(response.text)
	# This selects the first table,using CSS Selector syntax
	# and then ignores the header row([1:])
	symbolslist = soup.select('table')[0].select('tr')[1:]
	# Obtain the symbol information for each
	# row in the s&p500 constituent table
	symbols = []
	for i, symbol in enumerate(symbolslist):
		tds = symbol.select('td')
		symbols.append(
			(
				tds[0].select('a')[0].text, # Ticker
				'stock',
				tds[1].select('a')[0].text, # Name
				tds[3].text, # Sector
				'USD',now,now
			)
		)
	return symbols
