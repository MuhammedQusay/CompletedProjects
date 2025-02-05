import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict


def check_url(url: str):
    try:
        response: Response = requests.get(url)

        status_code = response.status_code
        headers: CaseInsensitiveDict[str] = response.headers
        content_type = headers.get("Content-Type", "Unknown")
        server = headers.get("Server", "Unknown")
        response_time = response.elapsed.total_seconds()

        print(f"{status_code=}")
        print(f"{headers=}")
        print(f"{content_type=}")
        print(f"{server=}")
        print(f"{response_time=}")
        # print(list(response))


    except RequestException as e:
        print(f"Error: {e}")


def main():
    url_to_check = input("url you want to check: ")
    check_url(url_to_check)


if __name__ == '__main__':
    main()
