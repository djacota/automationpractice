from src.core.utils import *

from src.pages.p__homepage import Homepage
from src.pages.p__authentication import Authentication
from src.pages.p__myaccount import MyAccount
from src.pages.p__mywishlist import MyWishlist
from src.pages.p__women import Women

from src.tests.tests import Tests


homepage = Homepage()
authentication = Authentication()
myaccount = MyAccount()
mywishlist = MyWishlist()
women = Women()

driverr = Browser()
print("\nPID: " + str(driverr.get_pid()))
Tests.run__test_login(driverr, homepage, authentication, myaccount, mywishlist, women)
driverr.close_driver()

driverr = Browser()
print("\nPID: " + str(driverr.get_pid()))
Tests.run__test(driverr, homepage, authentication, myaccount, mywishlist, women)
driverr.close_driver()

print("\nTest done.")
