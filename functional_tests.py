#!/usr/bin/env python3

import traceback
import sys
# ######################################################
# ######################################################
# ######################################################
print('# ######################################################')
exit_status = 0
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

try: assert 'Django' in browser.title
except Exception as inst:
    print('### ERROR: ###################################')
    traceback.print_exc()
    exit_status = 1
else:
    print("All Ok.")
finally:
    print('# ######################################################')
    browser.quit()
print('Quit')
import sys
sys.exit(exit_status)
# ######################################################
# ######################################################
# ######################################################


#try:
#except Exception as inst:
    #print(type(inst))    # the exception instance
    #print(inst.args)     # arguments stored in .args
    #print(inst)          # __str__ allows args to be printed directly,
# help(webdriver.Firefox)
# class WebDriver(selenium.webdriver.remote.webdriver.WebDriver)
#    WebDriver( capabilities=None, desired_capabilities=None,
#               log_path=None, service_log_path='geckodriver.log',
#               executable_path='geckodriver',
#               firefox_binary=None, firefox_options=None, firefox_profile=None,
#               keep_alive=True options=None, proxy=None, service_args=None, timeout=30,)

# ######################################################
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
cap['binary'] = '/home/mjb/bin/geckodriver'
browser = webdriver.Firefox(executable_path=r'/home/mjb/bin/geckodriver')
browser.get('http://google.com')                   # browser.get('http://localhost:8000')
assert 'Django' in browser.title

import sys
sys.exit(0)
# ######################################################

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
#cap['binary'] = '/usr/bin/firefox'
#cap['binary'] = '/home/mjb/bin/geckodriver'

cap['handleAlerts'] = True
cap['acceptSslCerts'] = True
cap['acceptInsecureCerts'] = True

browser = webdriver.Firefox()
#browser = webdriver.Firefox(capabilities=cap, timeout=10)

# , executable_path='/home/mjb/bin/geckodriver', firefox_binary='/usr/bin/firefox')
# service_log_path='geckodriver.log',
browser.get('http://google.com')                   # browser.get('http://localhost:8000')
assert 'Django' in browser.title

## from selenium import webdriver
##
## # selenium.common.exceptions.SessionNotCreatedException: Message: Unable to find a matching set of capabilities
## # https://stackoverflow.com/questions/47782650/selenium-common-exceptions-sessionnotcreatedexception-message-unable-to-find-a/47785513
## from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
## browser = webdriver.Firefox(capabilities=cap)
## # selenium.common.exceptions.WebDriverException: Message: Can't load the profile. Possible firefox version mismatch.
## #   You must use GeckoDriver instead for Firefox 48+. Profile Dir: /tmp/tmpny6wa451
## #   If you specified a log_file in the FirefoxBinary constructor, check it for details.
## browser.get('http://google.com')
##
##
## #browser = webdriver.Firefox()
## #browser.get('http://localhost:8000')
##
## assert 'Django' in browser.title
##
