from src.core.utils import *


# ------------------------------------------------------------------------------------------------------------------


@dataclass
class Authentication_Forms_SignIn__EmailAddress_:
    url: str = """"""
    xpath: str = """//*[@id="email"]"""


@dataclass
class Authentication_Forms_SignIn__Password_:
    url: str = """"""
    xpath: str = """//*[@id="passwd"]"""


@dataclass
class Authentication_Forms_SignIn__SignIn_:
    url: str = """"""
    xpath: str = """//*[@id="SubmitLogin"]/span"""


@dataclass
class Authentication_Forms__SignIn_:
    EmailAddress: str = Authentication_Forms_SignIn__EmailAddress_().xpath
    Password: str = Authentication_Forms_SignIn__Password_().xpath
    SignIn: str = Authentication_Forms_SignIn__SignIn_().xpath


@dataclass
class Authentication__Forms_:
    Form_SignIn: Authentication_Forms__SignIn_ = Authentication_Forms__SignIn_()
    Form_Register = None


@dataclass
class Authentication_:
    BaseUrl: str = """http://automationpractice.com/index.php?controller=authentication&back=my-account"""
    Forms: Authentication__Forms_ = Authentication__Forms_()
    PageName = """//h1[contains(text(), "Authentication")]"""


# ------------------------------------------------------------------------------------------------------------------


class Authentication:
    def __init__(self):
        pass

    def sign_in(self, driver: Browser, user: str, password: str):
        locator = Authentication_.Forms.Form_SignIn.EmailAddress
        driver.click(locator)
        keys = user
        elem = WebDriverWait(driver.my_driver, 10).until(ec.visibility_of_element_located((By.XPATH, locator))).send_keys(keys)

        locator = Authentication_.Forms.Form_SignIn.Password
        driver.click(locator)
        keys = password
        elem = WebDriverWait(driver.my_driver, 10).until(ec.visibility_of_element_located((By.XPATH, locator))).send_keys(keys)

        locator = Authentication_.Forms.Form_SignIn.SignIn
        driver.click(locator)


# ------------------------------------------------------------------------------------------------------------------
