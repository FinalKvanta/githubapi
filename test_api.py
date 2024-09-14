import os
import requests
from dotenv import load_dotenv

load_dotenv()

GIT_TOKEN = os.getenv('GIT_TOKEN')

GIT_USER = os.getenv('GIT_USER')

headers = {
    "Authorization": f"token {GIT_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

api_url = "https://api.github.com"

def create_repo(repo_name):

    url = f"{api_url}/user/repos"

    data = {"name": repo_name, "private": False}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:

        print(f"Репозиторий '{repo_name}' успешно создан.")

    else:

        print(f"Ошибка при создании репозитория: {response.json()}")

def check_repo_exists(repo_name):

    url = f"{api_url}/repos/{GIT_USER}/{repo_name}"

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:

        print(f"Репозиторий '{repo_name}' существует.")

        return True
    
    else:

        print(f"Репозиторий '{repo_name}' не найден.")

        return False

def delete_repo(repo_name):

    url = f"{api_url}/repos/{GIT_USER}/{repo_name}"

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:

        print(f"Репозиторий '{repo_name}' успешно удален.")

    else:

        print(f"Ошибка при удалении репозитория: {response.json()}")

if __name__ == "__main__":

    repo_name = os.getenv('REPOS_PATH')

    create_repo(repo_name)

    if check_repo_exists(repo_name):

        delete_repo(repo_name)

