from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from ZSB_Automation.ZSB_Mobile.Common_Method import Common_Method
# from ZSB_Automation.ZSB_Mobile.PageObject.APP_Settings_Screen import App_Settings_Screen
from ZSB_Mobile.PageObject.Feed_on_Head_Close.Feed_on_HeadClose import Feed_on_HeadClose
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen


class test_Feed_On_HeadClose():
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
sleep(3.0)




def test_Feed_on_HeadClose_TestcaseID_45790():
    """"Create the object for Login page & Common_Method page to reuse the methods"""""


login_page = Login_Screen(poco)
feed_on_close = Feed_on_HeadClose(poco)

#login_page.click_LoginAllow_Popup()
login_page.click_loginBtn()
sleep(2)
"""""""select the login with google option"""""""""
login_page.click_Loginwith_Google()
sleep(2)

""" Select the existing Google Test Account """
login_page.click_swdvt_account()
time.sleep(10)

""" Click on the Navigation Menu """

login_page.click_Menu_HamburgerICN()
sleep(1)

""" Select the Printer Settings """
feed_on_close.click_Printer_Settings()

""" Select a printer """
feed_on_close.click_selected_printer()
sleep(2)


""" FURTHER CANNOT BE AUTOMATED DUE TO THE BUG ID: SMBM-1684, SMBM-1236"""

""" Click on the icon """

"""Similar methods used"""

feed_on_close.click_icon()
sleep(1)
res = feed_on_close.verify_text()
print(res)

feed_on_close.click_demo_video()
sleep(5)

res = feed_on_close.verify_demo_video()
print(res)


feed_on_close.click_to_exit_demo_video()



# def test_Feed_on_HeadClose_TestcaseID_45791():
#     pass
#
# login_page = Login_Screen(poco)
# feed_on_close = Feed_on_HeadClose(poco)
#
# # login_page.click_LoginAllow_Popup()
# # login_page.click_loginBtn()
# # sleep(2)
# # """""""select the login with google option"""""""""
# # login_page.click_Loginwith_Google()
# # sleep(2)
# #
# # """ Select the existing Google Test Account """
# # login_page.click_swdvt_account()
# # sleep(2)
#
# """ Click on the Navigation Menu """
#
# login_page.click_Menu_HamburgerICN()
# sleep(1)
#
# """ Select the Printer Settings """
# feed_on_close.click_Printer_Settings()
#
# """ Select a printer """
# feed_on_close.click_selected_printer()
# sleep(2)

""" FURTHER CANNOT BE AUTOMATED DUE TO THE BUG ID: SMBM-1684, SMBM-1236"""





# """ check update printer "Feed on Cover Close" value, delete printer but not decomission, restart printer , setting will not set to default"""
#
# def test_Feed_on_HeadClose_TestcaseID_45792():
#     pass


# login_page = Login_Screen(poco)
# feed_on_close = Feed_on_HeadClose(poco)
#
# # login_page.click_LoginAllow_Popup()
# # login_page.click_loginBtn()
# # sleep(2)
# # """""""select the login with google option"""""""""
# # login_page.click_Loginwith_Google()
# # sleep(2)
# #
# # """ Select the existing Google Test Account """
# # login_page.click_swdvt_account()
# # sleep(2)
#
# """ Click on the Navigation Menu """
#
# login_page.click_Menu_HamburgerICN()
# sleep(1)
#
# """ Select the Printer Settings """
# feed_on_close.click_Printer_Settings()
#
# """ Select a printer """
# feed_on_close.click_selected_printer()
# sleep(2)
""" FURTHER CANNOT BE AUTOMATED DUE TO THE BUG ID: SMBM-1684, SMBM-1236"""



