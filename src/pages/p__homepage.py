from src.core.utils import *


# ------------------------------------------------------------------------------------------------------------------


@dataclass
class Homepage_Buttons__Btn_SignIn_:
    url: str = """http://automationpractice.com/index.php?controller=authentication&back=my-account"""
    xpath: str = """//*[@title="Log in to your customer account"]"""


@dataclass
class Homepage__Buttons_:
    ActionUrl = Homepage_Buttons__Btn_SignIn_().url
    SignIn = Homepage_Buttons__Btn_SignIn_().xpath


@dataclass
class Homepage_:
    BaseUrl: str = """http://automationpractice.com/index.php"""
    Buttons: Homepage__Buttons_ = Homepage__Buttons_()


# ------------------------------------------------------------------------------------------------------------------


class Homepage:
    def __init__(self):
        pass

    def go_to_homepage(self, driver: Browser):
        driver.my_driver.get(Homepage_.BaseUrl)


# ------------------------------------------------------------------------------------------------------------------
