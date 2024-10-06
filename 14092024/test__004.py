# Why use WebDriverWait instead of time.sleep()?
# time.sleep() makes your program wait for a fixed number of seconds,
# whether or not the webpage is ready.

# WebDriverWait is smarter.
# It waits only as long as it needs to until something specific happens
# (like an element appears), and it won't wait longer than needed.
# It prevents the program from waiting too much or not enough.

# Why use EC. (Expected Conditions) instead of driver.?
# EC (Expected Conditions) are pre-made conditions that check if something is true
# (like if an element is clickable, or if the page URL has changed).
# These conditions help you interact with the webpage only when it’s ready.
# driver. directly interacts with the page
# (e.g., finding elements, clicking buttons),
# but it doesn’t wait.
# So, using EC ensures that the page is ready before interacting with it.

# Why use until?
# until tells the program to wait for something specific to happen
# (like an element being present, clickable, or a URL change).
# Once the condition is met, the program continues.
# If the condition isn’t met within the time limit, it raises an error.
# In short, WebDriverWait with EC and until helps your program wait for the right moment
# to interact with the webpage,
# ensuring the page is ready, which makes your test more reliable than using fixed
# wait times like time.sleep().





