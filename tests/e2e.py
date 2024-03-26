from selenium import web rowser

# URL to be opened in Chrome
url_chrome = 'http://www.walla.co.il'

# URL to be opened in Firefox
url_firefox = 'http://www.ynet.co.il'

# Path to the Chrome browser's executable file
# Note: You need to replace this with the actual path of Chrome on your system
chrome_path = '`C:\Program Files\Google\Chrome\Application\chrome.exe %s'

# Path to the Firefox browser's executable file
# Note: You need to replace this with the actual path of Firefox on your system
firefox_path = 'C:\Program Files\Mozilla Firefox\firefox.exe %s'

# Register the browsers
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

# Open URL in Chrome
webbrowser.get('chrome').open(url_chrome)

# Open URL in Firefox
webbrowser.get('firefox').open(url_firefox)
