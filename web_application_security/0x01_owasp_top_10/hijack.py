import requests

def generate_hijack_cookies(target_url, num_cookies, output_file):
    """
    Generate a specified number of `hijack_session` cookies from the target URL and save them to a file.

    Args:
        target_url (str): The target URL to visit.
        num_cookies (int): The number of cookies to generate.
        output_file (str): The file to save the cookies.

    Returns:
        None
    """
    cookies = []

    with open(output_file, "w") as file:
        for i in range(num_cookies):
            response = requests.get(target_url)
            if 'hijack_session' in response.cookies:
                cookie = response.cookies['hijack_session']
                cookies.append(cookie)
                file.write(f"{cookie}\n")
                print(f"[{i + 1}] Cookie: {cookie}")
            else:
                print(f"[{i + 1}] No hijack_session cookie found.")

if __name__ == "__main__":
    # Target URL
    target_url = "http://web0x01.hbtn/a1/hijack_session"

    # Number of cookies to generate
    num_cookies = 100

    # Output file to save cookies
    output_file = "hijack_cookies.txt"

    # Generate cookies
    print("Generating hijack_session cookies...")
    generate_hijack_cookies(target_url, num_cookies, output_file)

    print(f"\nCookies saved to {output_file}")
