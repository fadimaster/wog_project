from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys


def test_scores_service(url):
    # Set up Chrome options for headless execution
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Initialize WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the specified URL
    driver.get(url)

    # Attempt to find the score element and retrieve its text
    try:
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)

        # Check if the score is within the expected range
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        # Ensure the driver is closed after the test
        driver.quit()


def main_function(url="http://localhost:5000"):
    # Execute the test function
    if test_scores_service(url):
        exit(0)  # Test passed
    else:
        exit(-1)  # Test failed
    

main_function()