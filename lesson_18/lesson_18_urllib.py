import urllib.request
import urllib.parse

def get_method(url:str, data:dict={}):
    """ Getting data from url

    :param url: The URL to send the GET request to.
    :param data: Optional dictionary to be sent as query parameters.
    """
    encode_data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(
            url, 
            method='GET',
            data=encode_data, 
            headers={'Content-Type': 'application/json'}
        )
    with urllib.request.urlopen(request) as f:
            result = f.read()
            return result

def post_method(url:str, data:dict={}):
    """ Getting data from url

    :param url: The URL to send the GET request to.
    :param data: Optional dictionary to be sent as query parameters.
    """
    encode_data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(
            url, 
            method='POST',
            data=encode_data, 
            # headers={'Content-Type': 'application/json'}
        )
    with urllib.request.urlopen(request) as f:
            result = f.read()
            return result


def post_method_1(url:str = "https://www.example.com", data:dict = {}):
    """ Getting data... """
    encode_data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data=encode_data)
    result = response.read()
    return result


def pastebin():
    url = "https://pastebin.com/api/api_post.php"
    post_data = dict(
        api_dev_key = "ulMHuv-FlPEloav7EYTG3u4jRLqizgxJ",
        api_paste_code = "Ми вивчаємо запити у пітон",
        api_option = "paste",
    )
    return post_method(url, post_data)


def get_api_hillel():
    url = "https://qauto.forstudy.space/api-docs/auth/logout"
    return get_method(url)

if __name__ == "__main__":
    

    result = get_api_hillel()
    print(result)