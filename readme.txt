# automationpractice


A very tiny test framework (made with Python and Selenium) for "automationpractice.com" as per "MY WISHLISTS" test cases.


About development environment:
* PyCharm Community 2019.3 EAP
* Python 3.7
* ChromeDriver 77.0.3865.40 (or higher)
* macOS 10.14 (or higher)


Install the Python packages from "requirements.txt" file.
Set ChromeDriver path in "src/config.json" file.
Create your "automationpractice.com" account and update some code lines [authentication.sign_in(driverr, "user", "password")] with your current credentials in "src/tests/tests.py" file.
Run "main.py" script.

To run the tests with a visible browser comment the line [self.my_chrome_options.add_argument("--headless")] from "Browser" class ("src/core/utils.py").


In case of any exception fired during the execution of the methods which belongs to Browser class, the "output/screenshots" folder will be populated with a .PNG picture taken from that moment.


The project is less than 100% done.

Have fun! :)
