# https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors
# https://www.w3schools.com/cssref/css_selectors.asp

# css selector best selector after ID
# fast for selenium next to ID
# easy to write
# better than xpath (even tho u hear the word so much more)

# go to 'http://demostore.supersqa.com'

# =============================
# Simply use id or class as css locator
# '.' is for class
# '#' is for id

# Example find the nav bar
# css using id = #site-navigation
# css using id = nav#site-navigation
# css using class = .main-navigation
# css using class = nav.main-navigation

# Two ways to test selector on Chrome developer tools
# 1. Simply Search (cmd+f then nav#site-navigation)
# 2. use the console
# $$(nav#site-navigation)  user $$ on console for css ($x) for xpath and just $ for jquery

# Second option is best in my opinion
# Example '.product' to find all products
# $$('li.product')

# =============================
# CHILD ELEMENT
# can chain css with '>' or ' ' (space) to find child elements.
# '>' for direct decendent
# * ' ' for any child/subchild
# next two should give same result
# 'div.storefront-sorting ul.page-numbers'
# 'div.storefront-sorting > nav.woocommerce-pagination > ul.page-numbers'

# MORE CHILD ELEMENT
# locator:nth-child(n)
# locator:nth-of-type(n)
# 'ul.products li:nth-child(2)'
# 'ul.products li:nth-of-type(2)'
# another example
# 'input.input-text:nth-of-type(1)'  >> results with 4 elements
# 'input.input-text:nth-child(1)'  >> results with 2 elements
# so add more properties
# 'form.login input.input-text:nth-child(1)'

# Multiple Classes
# * just connect all classes with '.'
# 'li.product.type-product.instock.product-type-simple'
# 'li.product.type-product.outofstock"
# 'li.product.product-type-variable

# Use any attribute
# * 'a[data-product_id="23"]'
# * 'nav[aria-label="Primary Navigation"]'
# * 'ul[id="site-header-cart"] a[title="View your shopping cart"]'
# * 'a[title="View your shopping cart"]'
# * 'a.footer-cart-contents[title="View your shopping cart"]'
# 'button.woocommerce-button[value="Log in"]'
# attribute must be exactly as it appears. For example can not take just one class
# ul[class="products columns-4"]

# Partialy matching attribute
# * contains word
# ^ start with word
# $ ends with word
# the following 4 css have same result ( the wildcard ones can have more matches)
# 'a[title="View your shopping cart"]'
# 'a[title^="View your"]'
# 'a[title*="shopping"]'
# 'a[title$="cart"]'


# exclude selector
# $$('li.product:not(.product-type-variable)')

# #site-header-cart > li:nth-child(1) > a


