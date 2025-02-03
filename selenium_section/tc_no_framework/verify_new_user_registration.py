from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random


driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = 'http://demostore.supersqa.com/my-account/'
email_field_id = 'reg_email'
psswd_field_id = 'reg_password'

# go to url:
driver.get(url)
email_field = driver.find_element(By.ID, email_field_id)

# generate random email:
letters = string.ascii_lowercase
rand_string = ''.join(random.choice(letters) for i in range(10))
random_email = rand_string + '@supersqa.com'

# type in the email field:
email_field.send_keys(random_email)

# find passworod field and send password
password_field = driver.find_element(By.ID, psswd_field_id)
password_field.send_keys('abcde098765!')

# button register:
# <button type="submit" class="woocommerce-Button woocommerce-button button woocommerce-form-register__submit"
# name="register" value="Register">Register</button>
register_btn = driver.find_element(By.CSS_SELECTOR, 'button[value="Register"]')
register_btn.click()

# check if logout button is displayed:
log_out_css = ('li.woocommerce-MyAccount-navigation-link--customer-logout a')

try:
    log_out_btn = driver.find_element(By.CSS_SELECTOR, log_out_css)
    if log_out_btn.is_displayed():
        print('test OK')
except:
    raise Exception('error - user not logged in after registration')

driver.quit()
