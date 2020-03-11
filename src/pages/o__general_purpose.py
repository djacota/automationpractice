from dataclasses import dataclass


# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Article Class

class Article:
    xpath: str = ''

    def __init__(self):
        pass

    @staticmethod
    def article_from_category(self, article_name):
        self.xpath = """//*[@id='center_column']/ul//a[contains(text(), '""" + article_name + """')]"""
        return self.xpath
    
    @staticmethod
    def article_from_wishlist(self, article_name):
        self.xpath = """//*[@id="s_title"][contains(text(), '""" + article_name + """')]"""
        return self.xpath


# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# PageElements_


@dataclass
class PageElements_UserMenu__Account:
    xpath__sign_out: str = """//*[@id="header"]//*[contains(@class, 'logout')]"""
    xpath__account: str ="""//*[@id="header"]//*[contains(@class, 'account')]"""


@dataclass
class PageElements__UserMenu:
    ContactUs = None
    SignOut = PageElements_UserMenu__Account().xpath__sign_out
    Account = PageElements_UserMenu__Account().xpath__account


@dataclass
class PageElements_TopMenu__Women:
    xpath: str = """//*[@id="block_top_menu"]//a[contains(text(),'Women')]"""


@dataclass
class PageElements__TopMenu:
    Dresses = None
    T_Shirts = None
    Women: str = PageElements_TopMenu__Women().xpath


@dataclass
class PageElements_:
    UserMenu: PageElements__UserMenu = PageElements__UserMenu()
    TopMenu: PageElements__TopMenu = PageElements__TopMenu()
    CategoryName: str = """//*[@class="cat-name"]"""
    LogoImage: str = """//*[@id="header_logo"]/a"""


# ------------------------------------------------------------------------------------------------------------------


@dataclass
class ViewOption_Grid:
    xpath = """//*[@id="grid"]/a"""


@dataclass
class ViewOption_List:
    xpath = """//*[@id="list"]/a"""


@dataclass
class ViewMode:
    Grid = ViewOption_Grid().xpath
    List = ViewOption_List().xpath


@dataclass
class View:
    Label: str = """//*[@class="display-title"]"""
    Mode = ViewMode()


# ------------------------------------------------------------------------------------------------------------------


@dataclass
class Card_Style_2:
    Add_to_Wishlist: str = """//*[@id="center_column"]//li[contains(@class, "hovered")]//a[contains(text(), "Add to Wishlist")]"""


# ------------------------------------------------------------------------------------------------------------------


@dataclass
class ModalWindow:
    Close: str = """//*[@id="category"]//a[contains(@title, "Close")]"""
    Message: str = """//*[contains(@class, 'fancybox-error')]"""


# ------------------------------------------------------------------------------------------------------------------


@dataclass
class CustomerAccount:
    Account: str ="""//*[@id="header"]//a[contains(@class, "account")]"""

# ------------------------------------------------------------------------------------------------------------------


@dataclass
class HtmlDomElement:
    id: str = 'id'
    className: str = 'class'
    innerHTML: str = 'innerHTML'
    outerHTML: str = 'outerHTML'
    title: str = 'title'

# ------------------------------------------------------------------------------------------------------------------
