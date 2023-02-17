from selenium import webdriver
import random

# Create a new instance of the Edge driver
driver = webdriver.Edge()

# Set the loop counter to 0
counter = 0

# Set the maximum number of loops
max_loops = 5

# Start the loop
while counter < max_loops:
    # Generate a random search term
    search_term = f'Random Search {random.randint(1, 100)}'

    # Navigate to Google's homepage
    driver.get('https://www.google.com')

    # Find the search box element and enter the search term
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(search_term)

    # Submit the search
    search_box.submit()

    # Wait for the search results to load
    driver.implicitly_wait(10)

    # Close the browser
    driver.quit()

    # Increment the counter
    counter += 1
