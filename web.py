import requests
from bs4 import BeautifulSoup

# Function to crawl a webpage and extract its content
def crawl_webpage(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Error:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Function to search for keywords in the content
def search_for_keywords(content, keywords):
    found_keywords = []
    for keyword in keywords:
        if keyword in content.lower():
            found_keywords.append(keyword)
    return found_keywords    
    

# Main function
def main():
    # URL of the website you want to crawl
    target_url = "a"  # Replace with your target website URL

    # Customize this list with specific keywords to search for
    keywords_to_search = ["c++"]

    content = crawl_webpage(target_url)
    if content:
        found_keywords = search_for_keywords(content, keywords_to_search)
        if found_keywords:
            print("Potential gun or weapon-related content found on the webpage. Keywords found:", found_keywords)
        else:
            print("No gun or weapon-related content found on the webpage.")

if __name__ == "__main__":
    main()
