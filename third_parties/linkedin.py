import os
import requests

from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape LinkedIn profile using either the LinkedIn API or a mocked response.

    Args:
    - linkedin_profile_url (str): The URL of the LinkedIn profile to scrape.
    - mock (bool, optional): Whether to use a mocked response or the LinkedIn API.

    Returns:
    - response (dict): The scraped data from the LinkedIn profile.
    """

    # If the 'mock' flag is True, use a mocked response.
    if mock:
        # The mocked response is a JSON file hosted on GitHub Gist.
        linkedin_profile_url = (
            "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/"
            "raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        )
        # Make a GET request to the mocked response URL.
        response = requests.get(
            linkedin_profile_url,  # The URL of the mocked response.
            timeout=10,  # The maximum amount of time to wait for the response.
        )
    # If the 'mock' flag is False, use the LinkedIn API.
    else:
        # The LinkedIn API endpoint.
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        # The headers containing the API key for authentication.
        header_dic = {"Authorization": f"Bearer {os.environ.get('PROXYCURL_API_KEY')}"}
        # Make a GET request to the API endpoint with the LinkedIn profile URL as a parameter.
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,  # The maximum amount of time to wait for the response.
        )

    # Parse the JSON response into a dictionary.
    data = response.json()

    # Remove empty values and specific keys from the dictionary.
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    # Remove the 'profile_pic_url' key from each group in the 'groups' list.
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    # Return the scraped data.
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
           linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",
           mock=True
        )
    )

