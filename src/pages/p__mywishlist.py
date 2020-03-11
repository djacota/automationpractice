from src.core.utils import *


# ------------------------------------------------------------------------------------------------------------------


@dataclass
class MyWishlist_:
    BaseUrl: str = """http://automationpractice.com/index.php?fc=module&module=blockwishlist&controller=mywishlist"""
    PageName = """//*[@id="mywishlist"]/h1"""
    Table: str = """//*[@id="block-history"]/table"""
    WishlistContent = """//div[contains(@class, 'wlp_bought')]"""
    WishlistArticle: str = """//*[contains(@class, 'wlp_bought')]//li"""
    WishlistArticle_Article: str = """//*[@id="s_title"]"""
    WishlistArticle_Quantity: str = """//*[@class="product_infos"]//*[contains(@id, 'quantity')]"""
    WishlistArticle_Priority: str = """//*[@class="product_infos"]//*[@class="form-control grey"][contains(@id, "priority")]"""
    WishlistArticle_Save: str = """//*[contains(@class, "btn")]/a"""


# ------------------------------------------------------------------------------------------------------------------


class MyWishlist:
    wishlist_table: Table
    wishlist_content = {}

    def __init__(self):
        self.wishlist_table = Table()

    def delete_wishlist_table(self, driver: Browser):
        # driver = driver.my_driver
        # get the table
        self.wishlist_table = Table.get_table_by_xpath(driver, MyWishlist_.Table)
        # get the number of rows and cols from the table
        table_cols = len(self.wishlist_table['head'])
        try:
            table_rows = int(len(self.wishlist_table['row']) / table_cols)
        except ZeroDivisionError:
            table_rows = 0
        # delete rows
        while table_rows > 0:
            driver.click(self.wishlist_table['row'][('row_0', 'col_5')]['xpath'])
            import time
            time.sleep(1)
            driver.my_driver.switch_to_alert().accept()
            time.sleep(1)
            # WebDriverWait(driver.my_driver, 10).until(driver.my_driver.switch_to_alert().accept())  # fara accept()
            # driver.my_driver.switch_to_alert().accept()
            self.wishlist_table = Table.get_table_by_xpath(driver, MyWishlist_.Table)
            table_cols = len(self.wishlist_table['head'])
            try:
                table_rows = int(len(self.wishlist_table['row']) / table_cols)
            except ZeroDivisionError:
                table_rows = 0

    def click_wishlist(self, driver: Browser, wishlist_name: str):
        table = Table.get_table_by_xpath(driver, self.wishlist_table["xpath"])
        table = table['row']
        xpath = ''
        i_row_ = 0
        # i_col_ = 0
        for col in range(len(table)):
            row_ = 'row_' + str(i_row_)
            col_ = 'col_' + str(col % len(self.wishlist_table['head']))
            index = (row_, col_)
            if table[index]['data'] == wishlist_name:
                xpath = table[index]['xpath']
                break
            col = col + 1
            if (col % len(self.wishlist_table['head'])) == 0:
                i_row_ = i_row_ + 1
        return xpath

    def get_articles_from_wishlist(self, driver: Browser):
        mywishlist = driver.my_driver.find_elements_by_xpath(MyWishlist_.WishlistArticle)
        article_info = {}
        key_name = 'art_'
        a_name = ''
        a_quantity = ''
        a_priority = ''
        num_of_articles = 0
        for i in range(len(mywishlist)):
            # article name
            try:
                elem = mywishlist[i].find_element_by_xpath("." + MyWishlist_.WishlistArticle_Article).text.split("\n", 1)
                a_name = elem[0]
            except:
                a_name = ''
            # article quantity
            try:
                elem = mywishlist[i].find_element_by_xpath("." + MyWishlist_.WishlistArticle_Quantity)
                a_quantity = elem.get_attribute("value")
            except:
                a_quantity = ''
            # article priority
            try:
                elem = mywishlist[i].find_element_by_xpath("." + MyWishlist_.WishlistArticle_Priority)
                options = [x for x in elem.find_elements_by_tag_name("option")]
                for option_ in options:
                    selected = option_.get_attribute("selected")
                    if selected == "true":
                        a_priority = option_.get_attribute("text")
                        break
            except:
                a_priority = ''
            # article dictionary
            try:
                article_info[key_name + str(i)] = {"name": a_name, "quantity": str(a_quantity), "priority": a_priority}
                num_of_articles = i
            except:
                num_of_articles = i
        self.wishlist_content = article_info
        return num_of_articles + 1

    def get_article_info(self, article_name: str):
        for i in range(len(self.wishlist_content)):
            if self.wishlist_content["art_" + str(i)]["name"] == article_name:
                a_quantity = self.wishlist_content["art_" + str(i)]["quantity"]
                a_priority = self.wishlist_content["art_" + str(i)]["priority"]
                return {"name": article_name, "quantity": a_quantity, "priority": a_priority}
        return None

    def get_webelement_by_article_name(self, driver: Browser, article_name: str):
        mywishlist = driver.my_driver.find_elements_by_xpath(MyWishlist_.WishlistArticle)
        for i in range(len(mywishlist)):
            # article name
            try:
                elem = mywishlist[i].find_element_by_xpath("." + MyWishlist_.WishlistArticle_Article).text.split("\n", 1)
                a_name = elem[0]
                if a_name == article_name:
                    return mywishlist[i]
            except:
                a_name = ''
        return None


# ------------------------------------------------------------------------------------------------------------------
