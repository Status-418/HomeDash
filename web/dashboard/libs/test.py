import requests


def check_pihole():
    try:
        response = requests.get('http://172.16.10.5/admin/')
        if response.ok:
            if '<title>Pi-hole' in response.text:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        return False
    
def check_cups():
    try:
        response = requests.get('https://172.16.10.5:631/', verify=False)
        if response.ok:
            if '<title>Home' in response.text:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        return False