def download_contract_from_quanndl(contract,dl_dir):
	# Download an individual futures contract from Quandl and then
	# store it to disk in the 'dl_dir' directory. An auth_token is
	# required,which is obtained from the Quandl upon sign-up.
	# Construct the API call from the contract and auth_token
	api_call = "http://www.quandl.com/api/v1/datasets/"
	api_call += "OFDP/FUTURE_%s.csv" % contract
	# If you wish to add an auth token for more downloads,simply
	# comment the following line and replace MY_AUTH_TOKEN with
	# your auth token in the line below
	params = "?sort_order=asc"
	# params = "?auth_token=MY_AUTH_TOKEN&sort_order=asc"
	full_url = "%s%s" % (api_call,params)
	
	# Download the data from Quandl
	data = requests.get(full_url).text
	
	# Store the data to disk
	fc = open('%s/%s.csv' % (dl_dir,contract),'w')
	fc.write(data)
	fc.close()
