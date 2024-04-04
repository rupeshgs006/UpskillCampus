import requests

# Replace 'YOUR_BITLY_API_TOKEN' with the provided API token
BITLY_API_TOKEN = f'f17f496959520f654cfe9eee33cbba51e8368c25'

# Define the headers with the Bitly API token
headers = {
    'Authorization': f'Bearer {BITLY_API_TOKEN}',
    'Content-Type': 'application/json',
}

# Prompt the user to enter the long URL
long_url = input("Enter the long URL: ")

# Define the data payload with the long URL provided by the user
data = {
    'long_url': long_url,
}

# Make a POST request to shorten the URL
response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    if 'link' in response_json:
        # Extract the shortened URL from the response
        shortened_url = response_json['link']
        print("Shortened URL:", shortened_url)
    else:
        print("Failed to shorten URL. No shortened URL found in response.")
else:
    # If the request fails, print the error message and the response content
    print("Failed to shorten URL:", response.text)
