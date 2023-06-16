from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://chat.openai.com/?model=gpt-4-browsing")

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("cheese")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

# the page is ajaxy so the title is originally this:
print driver.title

# we have to wait for the page to refresh, the last thing that seems to be updated is the title
WebDriverWait(driver, 10).until(EC.title_contains("cheese"))

# You should see "cheese - Google Search"
print driver.title
