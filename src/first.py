from seleniumwire import webdriver

# creating webdriver.
driver = webdriver.Chrome()

# Navigate to google home page. While navigate it wll track requests make by browser.
driver.get('https://google.com')

# Iterate over all POST requests made by browser and print request body.
for request in driver.requests:
    if request.method == 'POST':
        print(request.body)

# quitting browser session
driver.quit()
