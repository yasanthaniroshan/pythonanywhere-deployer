import requests,sys

def send_command_to_console(url:str,data:dict):
    try:
        response = requests.post(url, headers=headers, data=data)
        print(response.status_code, response.text)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(e)
        sys.exit(1)
    

def reload_web_app():
    try:
        response = requests.post(URL_FOR_RELOAD_WEB_APP, headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    USERNAME, API_TOKEN,BRANCH,HOST,CONSOLE_ID,BRANCH = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5],sys.argv[6]
    DOMAIN_NAME = f'{USERNAME}.pythonanywhere.com'
    headers={'Authorization': 'Token {token}'.format(token=API_TOKEN)}
    URL_FOR_CONSOLE = f'https://www.{HOST}/api/v0/user/{USERNAME}/consoles/'
    URL_FOR_RELOAD_WEB_APP = f'https://www.{HOST}/api/v0/user/{USERNAME}/webapps/{DOMAIN_NAME}/reload/'
    URL_TO_SEND_INPUT = URL_FOR_CONSOLE+str(CONSOLE_ID)+'/send_input/'
    data = {'input':f'git pull origin {BRANCH}\n'}
    send_command_to_console(URL_TO_SEND_INPUT, data)
    reload_web_app()
    

