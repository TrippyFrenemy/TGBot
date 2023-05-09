import requests

def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    print(response)


if __name__ == "__main__":
    get_data()