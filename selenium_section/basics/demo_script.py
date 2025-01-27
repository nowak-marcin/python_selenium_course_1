# from selenium import webdriver
# import time

# open chrome driver:
# driver = webdriver.Chrome(executablePath='/user/local/bin/chromedriver')
# driver.implicitly_wait(5)

# go to url:
# driver.get('http://demostore.superqa.com/')
# time.sleep(3)

# click My Account tab:
# my_acct_tab = driver.find_element_by_link_text('My Account')
# my_acc_tab.click()
# time.sleep(3)

# scrole the page:
# driver.execute_script('window.scrollBy(0,300)')

# find username fild and input username:
# u_name_field = driver.find_element_by_id('username')
# u_name_field.send_keys('fakename')

# find password field and input password:
# u_name_field = driver.find_element_by_id('password')
# u_name_field.send_keys('aaaaaaa')

# click login button:
# login_btn = drive.find_element_by_name('login'
# login_btn.click()
# time.sleep(3)

# get dispalyed error:
# errors_list_elm = driver.find_elements_by_css_selector('ul.woocommerce-error li')
# first_error_elm = errors_list_elm[0]
# displayed_error_text = first_error_elm.text

# verify the displayed error is as expected:
# expected_error = 'ERROR: Invalid username. Lost your password?'
# assert expected_error == displayed_error_text, 'Displayed error is not as expected.'
# print('success!!!')

# close the browser:
# driver.quit()




