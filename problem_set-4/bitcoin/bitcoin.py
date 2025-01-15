
import requests
import sys

def btc():
    try:
        REQs = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        content = REQs.json()
        Currency = content["bpi"]

        usd = Currency["USD"]
        usd_rate = float(usd["rate"].replace(",", ""))

                                                        # for usd_rate in usd["rate"]:
                                                        #     print(usd_rate, end="")
        amount = float(sys.argv[1])

        
        if sys.argv[1] in sys.argv:
            if amount is not str:
                calc = amount * usd_rate
                print(f"${calc:,.4f}")
            else:
                raise notNum
        else:
            raise missing

    except ValueError as missing:
        print("Missing command-line argument")
        sys.exit(1)

    except ValueError as notNum:
        print("Command-line argument is not a number")
        sys.exit(1)

    except requests.RequestException:
        pass
btc()