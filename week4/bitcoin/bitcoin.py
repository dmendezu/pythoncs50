import sys
import requests

if len(sys.argv)<2:
    sys.exit('Missing command-line argument')
else:
    try:
        val=float(sys.argv[1])
        bitcoin_request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

        if (bitcoin_request.status_code==200):
            bitcoin_value=bitcoin_request.json()
            value=float(bitcoin_value["bpi"]["USD"]["rate_float"])
            amount=val*value
            print(f"${amount:,.4f}")
        else:
            raise requests.RequestException

    except ValueError:
        sys.exit('Command-line argument is not a number')

    except requests.RequestException:
        sys.exit('fail request')
