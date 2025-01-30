from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')


# placeholder:
# <input type="search" id="woocommerce-product-search-field-0" class="search-field"
# placeholder="Search products…" value="" name="s">

search_field = driver.find_element('id', 'woocommerce-product-search-field-0')
place_holder = search_field.get_attribute('placeholder')
if place_holder != 'Search products…':
    raise Exception(f'niewlasciwy placeholder, aktualny to: {place_holder}')
else:
    print(f'placeholder wlasciwy - {place_holder}')


# get link url:

product_link = driver.find_element('css selector', 'li.product a')
product_url = product_link.get_attribute('href')
print(f'link do produktu to {product_url}')


# which tab is selected:
# <li class="page_item page-item-9 current_page_item focus">
# <a href="http://demostore.supersqa.com/my-account/" aria-current="page">My account</a></li>

my_acc = driver.find_element('css selector', 'li.page-item-9')
my_acc.click()

nav_items = driver.find_elements('css selector', 'ul.nav-menu li')
for x in nav_items:
    item_class = x.get_attribute('class')
    if 'current_page_item' in item_class:
        print(f'wybrany tab to {x.text}')

driver.quit()