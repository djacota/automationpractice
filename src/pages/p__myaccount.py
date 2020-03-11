from src.core.utils import *


# ------------------------------------------------------------------------------------------------------------------


@dataclass
class MyAccount_Subcategory__MyWishlist_:
    url: str = """"""
    xpath: str = """//*[@class="icon-heart"]"""


@dataclass
class MyAccount__Subcategory_:
    Subcategory_1 = None
    Subcategory_2 = None
    Subcategory_n = None
    MyWishlist: str = MyAccount_Subcategory__MyWishlist_().xpath


@dataclass
class MyAccount_:
    BaseUrl: str = """http://automationpractice.com/index.php?controller=my-account"""
    Subcategory: MyAccount__Subcategory_ = MyAccount__Subcategory_()
    PageName = """//*[@id="center_column"]/h1"""


# ------------------------------------------------------------------------------------------------------------------


class MyAccount:
    def __init__(self):
        pass


# ------------------------------------------------------------------------------------------------------------------
