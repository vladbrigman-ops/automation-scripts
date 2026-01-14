import requests

def main():
    url = "https://httpbin.org/json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print("Успешный запрос!")
    print("Ключи в корне JSON:", list(data.keys()))

if __name__ == "__main__":
    main()
    