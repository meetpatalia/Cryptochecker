from django.shortcuts import render

def home(request):
	import requests
	import json

	#Crypto Price Data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,ADA,USDT,MIOTA,XRT,TFUEL&tsyms=USD")
	price = json.loads(price_request.content)

	#Crypto News
	# api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	# api = json.loads(api_request.content)
	return render(request, 'home.html', {'price': price})


def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		quote = quote.upper()
		#Get info for the searched currency
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

	else:
		return render(request, 'prices.html', {'notfound': True})
