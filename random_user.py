import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    responce = requests.get(url)
    data = responce.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        user_country = user_data["location"]["country"]
        return user_name , user_country
    else:
        raise Exception("Fetch failed API data")
    
def main():
    
    try:
        user_name,user_country = fetch_random_user()
        print(f"user_name : {user_name} \nuser_country : {user_country}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()