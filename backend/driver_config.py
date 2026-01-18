"""
driver_config.py - Anti-fingerprint and browser configuration for Chronos Engine (OP-VERITAS)
"""
from selenium.webdriver import ChromeOptions

def get_anti_fingerprint_options() -> ChromeOptions:
    options = ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1280,1024')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # Patch navigator.webdriver, user-agent, and other JS properties in runtime
    # (see core/antidetect.py for JS injection)
    return options
