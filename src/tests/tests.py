from src.core.utils import *

from src.pages.o__general_purpose import *

from src.pages.p__homepage import *
from src.pages.p__authentication import *
from src.pages.p__myaccount import *
from src.pages.p__mywishlist import *
from src.pages.p__women import *


class Tests:
    @staticmethod
    def run__test_login(driverr, homepage, authentication, myaccount, mywishlist, women):
        print("""Executing "login" test""")

        homepage.go_to_homepage(driverr)
        value = driverr.my_driver.current_url
        assert Homepage_.BaseUrl == value, "HOMEPAGE page: URL MISMATCH"

        driverr.click(Homepage_.Buttons.SignIn)
        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, Authentication_.PageName)
        assert "AUTHENTICATION" == value.upper(), "AUTHENTICATION page: NOT AVAILABLE"

        authentication.sign_in(driverr, "user", "password")
        value = driverr.my_driver.current_url
        assert MyAccount_.BaseUrl == value, "MY ACCOUNT page: URL MISMATCH"
        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, MyAccount_.PageName)
        assert "MY ACCOUNT" == value.upper(), "MY ACCOUNT page: NOT AVAILABLE"



    @staticmethod
    def run__test(driverr, homepage, authentication, myaccount, mywishlist, women):
        print("""Executing "a_to_z" test""")

        # -------------------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        # 1. "MY WISHLISTS"
        # 1.1. End-to-End Testing
        # 1.1.1. Scenario: User is logged in
        # 1.1.1.1. Prerequisites

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.1.1

        print("Executing step: 1.1.1.1.1")

        homepage.go_to_homepage(driverr)

        value = driverr.my_driver.current_url
        assert Homepage_.BaseUrl == value, "HOMEPAGE page: URL MISMATCH"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.1.2

        print("Executing step: 1.1.1.1.2")

        driverr.click(Homepage_.Buttons.SignIn)

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, Authentication_.PageName)
        assert "AUTHENTICATION" == value.upper(), "AUTHENTICATION page: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.1.3

        print("Executing step: 1.1.1.1.3")

        authentication.sign_in(driverr, "user", "password")

        value = driverr.my_driver.current_url
        assert MyAccount_.BaseUrl == value, "MY ACCOUNT page: URL MISMATCH"

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, MyAccount_.PageName)
        assert "MY ACCOUNT" == value.upper(), "MY ACCOUNT page: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.1.4

        print("Executing step: 1.1.1.1.4")

        driverr.click(MyAccount_.Subcategory.MyWishlist)

        value = driverr.my_driver.current_url
        assert MyWishlist_.BaseUrl == value, "MY WISHLIST page: URL MISMATCH"

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, MyWishlist_.PageName)
        assert "MY WISHLISTS" == value.upper(), "MY WISHLISTS page: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.1.5

        print("Executing step: 1.1.1.1.5")

        mywishlist.delete_wishlist_table(driverr)

        table = driverr.find_locator_by_xpath(MyWishlist_.Table)
        assert False == bool(table), "Wishlist table: NOT DELETED"

        # -------------------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------
#
#
        # -------------------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.
        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.1

        print("Executing step: 1.1.1.2.1")

        driverr.click(PageElements_.TopMenu.Women)

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, PageElements_.CategoryName)
        assert "WOMEN" == value.upper(), "WOMEN category: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.2

        print("Executing step: 1.1.1.2.2")

        driverr.scroll_to_element_by_xpath(View.Label, 2)

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, View.Label)
        assert "View" == value, "View label: NOT AVAILABLE"

        value = driverr.get_attribute_from(HtmlDomElement.title, View.Mode.Grid)
        assert "Grid" == value, "Grid mode: NOT AVAILABLE"

        value = driverr.get_attribute_from(HtmlDomElement.title, View.Mode.List)
        assert "List" == value, "List mode: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.3

        print("Executing step: 1.1.1.2.3")

        driverr.click(View.Mode.Grid)

        value = driverr.get_attribute_from(HtmlDomElement.className, str(View.Mode.Grid).replace('/a', ''))
        assert "selected" == value, "Grid mode: NOT SELECTED"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.4

        print("Executing step: 1.1.1.2.4")

        article = "Blouse"
        driverr.scroll_to_element_by_xpath(Article.article_from_category(Article, article), 2)

        # "is_element_in_viewport" method should be fixed; js error
        # !!!!! value = driverr.is_element_in_viewport(Article.by_name(Article, article) + '/ancestor::li')
        # assert True == bool(value), "Article: NOT VISIBLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.5

        print("Executing step: 1.1.1.2.5")

        article = "Blouse"
        driverr.mouseover_element_by_xpath(Article.article_from_category(Article, article))

        value = driverr.get_attribute_from(HtmlDomElement.className, Card_Style_2.Add_to_Wishlist)
        assert -1 != value.find('addToWishlist'), "Card_Style_2: NOT VISIBLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.6

        print("Executing step: 1.1.1.2.6")

        driverr.click(Card_Style_2.Add_to_Wishlist)

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, ModalWindow.Message)
        assert "Added to your wishlist." == value, "Modal window, \"Added to your wishlist.\": NOT PRESENT"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.7

        print("Executing step: 1.1.1.2.7")

        driverr.click(ModalWindow.Close)

        value = driverr.find_locator_by_xpath(ModalWindow.Close)
        assert False == bool(value), "Modal window: NOT CLOSED"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.8

        print("Executing step: 1.1.1.2.8")

        driverr.click(CustomerAccount.Account)

        value = driverr.my_driver.current_url
        assert MyAccount_.BaseUrl == value, "MY ACCOUNT page: URL MISMATCH"

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, MyAccount_.PageName)
        assert "MY ACCOUNT" == value.upper(), "MY ACCOUNT page: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.9

        print("Executing step: 1.1.1.2.9")

        driverr.click(MyAccount_.Subcategory.MyWishlist)

        value = driverr.my_driver.current_url
        assert MyWishlist_.BaseUrl == value, "MY WISHLIST page: URL MISMATCH"

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, MyWishlist_.PageName)
        assert "MY WISHLISTS" == value.upper(), "MY WISHLISTS page: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.10

        print("Executing step: 1.1.1.2.10")

        mywishlist.wishlist_table = Table.get_table_by_xpath(driverr, MyWishlist_.Table)
        driverr.click(mywishlist.click_wishlist(driverr, "My wishlist"))

        value = driverr.find_locator_by_xpath(MyWishlist_.WishlistContent)
        assert True == bool(value), "Wishlist content: NOT VISIBLE"

        value = driverr.my_driver.find_elements_by_xpath(MyWishlist_.WishlistArticle)
        assert 1 == len(value), "Wishlist content: WRONG NUMBER OF ARTICLES"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.11

        print("Executing step: 1.1.1.2.11")

        article = "Blouse"

        num_of_articles = mywishlist.get_articles_from_wishlist(driverr)
        assert 1 == num_of_articles, "Wishlist content: WRONG NUMBER OF ARTICLES"

        article = mywishlist.get_article_info(article)
        assert "Blouse" == article["name"], "Wishlist content: ARTICLE DOES NOT EXIST"
        assert "1" == article["quantity"], "Wishlist content: WRONG QUANTITY"
        assert "Medium" == article["priority"], "Wishlist content: WRONG PRIORITY"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.12

        print("Executing step: 1.1.1.2.12")

        article = "Blouse"

        value_to_set = "5"
        web_element = mywishlist.get_webelement_by_article_name(driverr, article)
        driverr.send_keys_by_webelement(web_element, MyWishlist_.WishlistArticle_Quantity, value_to_set, "-")

        elemm = driverr.my_driver.find_element_by_xpath(MyWishlist_.WishlistArticle_Quantity)
        paste_value = elemm.get_attribute('value')

        num_of_articles = mywishlist.get_articles_from_wishlist(driverr)
        assert 1 == num_of_articles, "Wishlist content: WRONG NUMBER OF ARTICLES"

        article = mywishlist.get_article_info(article)
        assert "Blouse" == article["name"], "Wishlist content: ARTICLE DOES NOT EXIST"
        assert value_to_set == paste_value, "Wishlist content: WRONG PARTIAL QUANTITY"
        assert "Medium" == article["priority"], "Wishlist content: WRONG PRIORITY"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.13

        print("Executing step: 1.1.1.2.13")

        article = "Blouse"

        web_element = mywishlist.get_webelement_by_article_name(driverr, article)
        driverr.click_by_webelement(web_element, MyWishlist_.WishlistArticle_Save)

        mywishlist.get_articles_from_wishlist(driverr)
        article = mywishlist.get_article_info(article)
        assert "Blouse" == article["name"], "Wishlist content: ARTICLE DOES NOT EXIST"
        assert "5" == article["quantity"], "Wishlist content: WRONG QUANTITY"
        assert "Medium" == article["priority"], "Wishlist content: WRONG PRIORITY"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.14

        print("Executing step: 1.1.1.2.14")

        driverr.click(CustomerAccount.Account)

        value = driverr.my_driver.current_url
        assert MyAccount_.BaseUrl == value, "MY ACCOUNT page: URL MISMATCH"

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, MyAccount_.PageName)
        assert "MY ACCOUNT" == value.upper(), "MY ACCOUNT page: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.15

        print("Executing step: 1.1.1.2.15")

        driverr.click(MyAccount_.Subcategory.MyWishlist)

        value = driverr.my_driver.current_url
        assert MyWishlist_.BaseUrl == value, "MY WISHLIST page: URL MISMATCH"

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, MyWishlist_.PageName)
        assert "MY WISHLISTS" == value.upper(), "MY WISHLISTS page: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.16

        print("Executing step: 1.1.1.2.16")

        mywishlist.wishlist_table = Table.get_table_by_xpath(driverr, MyWishlist_.Table)
        driverr.click(mywishlist.click_wishlist(driverr, "My wishlist"))

        value = driverr.find_locator_by_xpath(MyWishlist_.WishlistContent)
        assert True == bool(value), "Wishlist content: NOT VISIBLE"

        value = driverr.my_driver.find_elements_by_xpath(MyWishlist_.WishlistArticle)
        assert 1 == len(value), "Wishlist content: WRONG NUMBER OF ARTICLES"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.17

        print("Executing step: 1.1.1.2.17")

        article = "Blouse"

        mywishlist.get_articles_from_wishlist(driverr)
        article = mywishlist.get_article_info(article)
        assert "Blouse" == article["name"], "Wishlist content: ARTICLE DOES NOT EXIST"
        assert "5" == article["quantity"], "Wishlist content: WRONG QUANTITY"
        assert "Medium" == article["priority"], "Wishlist content: WRONG PRIORITY"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.18

        print("Executing step: 1.1.1.2.18")

        article = "Blouse"
        value_to_select = "Low"

        web_element = mywishlist.get_webelement_by_article_name(driverr, article)
        driverr.click_by_webelement(web_element, MyWishlist_.WishlistArticle_Priority)
        select = Select(web_element.find_element_by_xpath("." + MyWishlist_.WishlistArticle_Priority))
        select.select_by_visible_text(value_to_select)

        mywishlist.get_articles_from_wishlist(driverr)
        article = mywishlist.get_article_info(article)
        assert "Blouse" == article["name"], "Wishlist content: ARTICLE DOES NOT EXIST"
        assert "5" == article["quantity"], "Wishlist content: WRONG QUANTITY"
        assert "Low" == article["priority"], "Wishlist content: WRONG PRIORITY"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.19

        print("Executing step: 1.1.1.2.19")

        article = "Blouse"

        web_element = mywishlist.get_webelement_by_article_name(driverr, article)
        driverr.click_by_webelement(web_element, MyWishlist_.WishlistArticle_Save)

        mywishlist.get_articles_from_wishlist(driverr)
        article = mywishlist.get_article_info(article)
        assert "Blouse" == article["name"], "Wishlist content: ARTICLE DOES NOT EXIST"
        assert "5" == article["quantity"], "Wishlist content: WRONG QUANTITY"
        assert "Low" == article["priority"], "Wishlist content: WRONG PRIORITY"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.20

        print("Executing step: 1.1.1.2.20")

        driverr.click(PageElements_.UserMenu.SignOut)

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, Authentication_.PageName)
        assert "AUTHENTICATION" == value.upper(), "AUTHENTICATION page: NOT AVAILABLE"

        value = driverr.find_locator_by_xpath(PageElements_.UserMenu.Account)
        assert False == value, "Account button: IS PRESENT"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.21

        print("Executing step: 1.1.1.2.21")

        driverr.click(PageElements_.LogoImage)

        value = driverr.my_driver.current_url
        assert Homepage_.BaseUrl == value, "HOMEPAGE page: URL MISMATCH"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.22

        print("Executing step: 1.1.1.2.22")

        driverr.click(Homepage_.Buttons.SignIn)

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, Authentication_.PageName)
        assert "AUTHENTICATION" == value.upper(), "AUTHENTICATION page: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.23

        print("Executing step: 1.1.1.2.23")

        authentication.sign_in(driverr, "user", "password")

        value = driverr.my_driver.current_url
        assert MyAccount_.BaseUrl == value, "MY ACCOUNT page: URL MISMATCH"

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, MyAccount_.PageName)
        assert "MY ACCOUNT" == value.upper(), "MY ACCOUNT page: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.24

        print("Executing step: 1.1.1.2.24")

        driverr.click(MyAccount_.Subcategory.MyWishlist)

        value = driverr.my_driver.current_url
        assert MyWishlist_.BaseUrl == value, "MY WISHLIST page: URL MISMATCH"

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, MyWishlist_.PageName)
        assert "MY WISHLISTS" == value.upper(), "MY WISHLISTS page: NOT AVAILABLE"


        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.25

        print("Executing step: 1.1.1.2.25")

        mywishlist.wishlist_table = Table.get_table_by_xpath(driverr, MyWishlist_.Table)
        driverr.click(mywishlist.click_wishlist(driverr, "My wishlist"))

        value = driverr.find_locator_by_xpath(MyWishlist_.WishlistContent)
        assert True == bool(value), "Wishlist content: NOT VISIBLE"

        value = driverr.my_driver.find_elements_by_xpath(MyWishlist_.WishlistArticle)
        assert 1 == len(value), "Wishlist content: WRONG NUMBER OF ARTICLES"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.26

        print("Executing step: 1.1.1.2.26")

        article = "Blouse"

        mywishlist.get_articles_from_wishlist(driverr)
        article = mywishlist.get_article_info(article)
        assert "Blouse" == article["name"], "Wishlist content: ARTICLE DOES NOT EXIST"
        assert "5" == article["quantity"], "Wishlist content: WRONG QUANTITY"
        assert "Low" == article["priority"], "Wishlist content: WRONG PRIORITY"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.27

        print("Executing step: 1.1.1.2.27")

        driverr.click(PageElements_.TopMenu.Women)

        value = driverr.get_attribute_from(HtmlDomElement.innerHTML, PageElements_.CategoryName)
        assert "WOMEN" == value.upper(), "WOMEN category: NOT AVAILABLE"

        # -------------------------------------------------------------------------------------------------------------
        # 1.1.1.2.28

        # 1.1.1.2.29

        # 1.1.1.2.30

        # 1.1.1.2.31

        # 1.1.1.2.32

        # 1.1.1.2.33

        # 1.1.1.2.34

        # 1.1.1.2.35

        # 1.1.1.2.36

        # 1.1.1.2.37

        # 1.1.1.2.38

        # 1.1.1.2.39

        # 1.1.1.2.40

        # 1.1.1.2.41

        # 1.1.1.2.42

        # 1.1.1.2.43

        # 1.1.1.2.44

        # 1.1.1.2.45

        # 1.1.1.2.46

        # 1.1.1.2.47

        # 1.1.1.2.48

        # 1.1.1.2.49

        # 1.1.1.2.50

        # 1.1.1.2.51

        # 1.1.1.2.52

        # 1.1.1.2.53

        # 1.1.1.2.54

        # 1.1.1.2.55

        # 1.1.1.2.56

#
        # -------------------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------
