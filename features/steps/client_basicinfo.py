# from behave import *
# from features.pages.BasicinfoPage import BasicinfoPage
#
#
# @given(u'user is on the login page')
# def step_impl(context):
#     login_page = BasicinfoPage(context.driver)
#     login_page.login_page_nav()
#
#
# @when(u'user enters the credentials')
# def step_impl(context):
#     login_page = BasicinfoPage(context.driver)
#     login_page.enter_credentials("","")
#     allure.attach(context.driver.get_screenshot_as_png(), name="Login details",
#                   attachment_type=allure.attachment_type.PNG)
#
#
# @when(u'click on the login')
# def step_impl(context):
#     login_page = BasicinfoPage(context.driver)
#     login_page.login_button()
#
#
# @then(u'user is logged to dashboard page')
# def step_impl(context):
#     dashboard_page = BasicinfoPage(context.driver)
#     dashboard_page.redirect_to_dashboard()
#     allure.attach(context.driver.get_screenshot_as_png(), name="Redirect to dashboard",
#                   attachment_type=allure.attachment_type.PNG)
#
# @when(u'user clicks on the client module menu in side nav bar')
# def step_impl(context):
#     dashboard_page = BasicinfoPage(context.driver)
#     dashboard_page.click_clientmodule()
#
# @then(u'user will be directed to client module page')
# def step_impl(context):
#     client_page = BasicinfoPage(context.driver)
#     client_page.clientpage_nav()
#     allure.attach(context.driver.get_screenshot_as_png(), name="Redirect to clientpage",
#                   attachment_type=allure.attachment_type.PNG)
#
# @given(u'user is on the client list page')
# def step_impl(context):
#     #call the functions
#     pass
#
# @when(u'user clicks on the add client button')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.add_clientbutton()
#
# @then(u'user is redirected to client page basic details tab')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.clientpage_nav()
#     allure.attach(context.driver.get_screenshot_as_png(), name="Redirect to clientpage basicinfo",
#                   attachment_type=allure.attachment_type.PNG)
#
# @given(u'user is on the client basic details tab')
# def step_impl(context):
#     pass
#
# @when(u'user enter the client name')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_clientname()
#
# @then(u'the client id is automatically fetched')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.clientid_fetch()
#
# @when(u'user selects the client type, country, enter tax id')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.select_clienttype()
#     clientbasic_page.select_country()
#     clientbasic_page.enter_taxid()
#
# @then(u'select tax category')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.select_taxcategory()
#
# @when(u'user selects the industry type')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.select_industrytype()
#
# @when(u'enters the website and email name')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_website()
#     clientbasic_page.enter_emailname()
#
# @when(u'user selects the country code')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.select_countrycode()
#
# @when(u'type the telephone number')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_telphoneno()
#
# @then(u'type the mobile number, fax number')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_mobileno()
#     clientbasic_page.enter_faxnumber()
#
# @when(u'user checks the checkbox to yes')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.check_yes()
#
# @then(u'the user will get the contract details to be filled')
# def step_impl(context):
#     allure.attach(context.driver.get_screenshot_as_png(), name="Contractdetails displayed",
#                   attachment_type=allure.attachment_type.PNG)
#
# @when(u'user checks the checkbox to no')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.check_no()
#
# @then(u'the user should not get the contract details')
# def step_impl(context):
#     # screenshot
#     pass
#
# @when(u'user enters contract title, start date, end date, description')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_contracttitle()
#     clientbasic_page.select_startdate()
#     clientbasic_page.select_enddate()
#     clientbasic_page.enter_description()
#
# @then(u'user will attach the contract document in the attachment')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.contract_attachment()
#     # add the file funtion
#
# @when(u'user clicks on the add icon')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_addcontract()
#
# @then(u'user will get the another set of contract adding section')
# def step_impl(context):
#     pass
#
# @when(u'user enters the address title')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_addresstitle()
#
# @when(u'user selectes the address type')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.select_addresstype()
#
# @when(u'user enters the address line')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_addressline1()
#     clientbasic_page.enter_addressline2()
#     clientbasic_page.enter_addressline3()
#
# @when(u'clicks on the add icon to add the extra address lines')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.add_addressline()
#
# @when(u'user selects the country, state, city')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.select_country()
#     clientbasic_page.select_state()
#     clientbasic_page.select_city()
#
# @then(u'user enters the postal code')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_postalcode()
#
# @when(u'user selects the primary billing address checkbox')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page. select_primarybilling()
#
# @then(u'the address will made into billing address')
# def step_impl(context):
#     pass
#
# @then(u'user selects the primary shipping address checkbox')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.select_shipping()
#
#
# @then(u'user will get the address as primary shipping address')
# def step_impl(context):
#     pass
#
# @when(u'user clicks on the save button')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'the client basic detail will be added to the client list table')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.clientlist()
#
# @when(u'user clicks on submit without entering both tax id and tax category')
# def step_impl(context):
#     # enter all details other than above two
#
# @then(u'user wants to submit it successfully')
# def step_impl(context):
#     # ss for submit successfully
#
# @when(u'user clicks on save without entering in client name')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the mandatory error message for client name field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.mandatory_clientname()
#
# @then(u'user enters the input other than text')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_clientname("12345")
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the validation error message for client name field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.validation_clientname()
#
# @when(u'user clicks on save without selecting client type and program')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the error message for client type, country dropdown')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.mandatory_clienttype()
#     clientbasic_page.mandatory_country()
#
# @when(u'user enters the tax id')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_taxid("123456")
#
# @when(u'clicks on save button without giving the tax category')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'user wants to get mandatory error message for tax category')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.mandatory_taxcategory()
#
# @when(u'user clicks on save without entering in industry type, email')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the mandatory error message for industry type, email field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.mandatory_industrytype()
#     clientbasic_page.mandatory_email
#
# @then(u'user enters the invalid email format')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_emailname("23.com")
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the validation error message for invalid email')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.validation_email()
#
# @when(u'user clicks on save without entering in telephone, mobile number')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the mandatory error message for telephone, mobile number field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.mandatory_telephoneno()
#     clientbasic_page.mandatory_mobileno()
#
# @then(u'user enters the input other than number')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_telphoneno("test")
#     clientbasic_page.enter_mobileno("test")
#
# @then(u'user wants to get the validation error message for telephone, mobile number field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.validation_telephoneno()
#     clientbasic_page.validation_mobileno()
#
# @when(u'user clicks on save without selecting the radio button for contract signed')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the mandatory error message for contract signed radio button')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.mandatory_contractradioyes()
#
# @when(u'user clicks on save without entering in contract title, start date, end date, attachment')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the mandatory error message for contract title, start date, end date, attachment field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.mandatory_contracttitle()
#     clientbasic_page.mandatory_startdate()
#     clientbasic_page.mandatory_enddate()
#     clientbasic_page.mandatory_attachment()
#
# @then(u'user enters input other that alphanumeric values in contract title')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_contracttitle("*1-=")
#     clientbasic_page.click_save()
#
# @then(u'user wants to get validation error message for contract title field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.validation_contracttitle()
#
# @when(u'user clicks on save without entering address title and address type')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the mandatory error message for address title and address type field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.mandatory_addresstitle()
#     clientbasic_page.mandatory_addresstype()
#
# @then(u'user enters input other than alphanumeric values in address title')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_addresstitle("12@#$")
#     clientbasic_page.click_save()
#
# @then(u'user wants to get validation error message for address title field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.validation_addresstitle()
#
# @when(u'user clicks on save without entering address line 1, address line 2, address line 3')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the mandatory error message for address line 1, address line 2, address line 3 field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.mandatory_addressline1()
#     clientbasic_page.mandatory_addressline2()
#     clientbasic_page.mandatory_addressline3()
#
# @when(u'user clicks on save without entering country, state, city, postalcode')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.click_save()
#
# @then(u'user wants to get the mandatory error message for country, state, city, postalcode')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.mandatory_country()
#     clientbasic_page.mandatory_state()
#     clientbasic_page.mandatory_city()
#     clientbasic_page.mandatory_postalcode()
#
# @then(u'user enters input other than numeric values in postalcode')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.enter_postalcode("test")
#     clientbasic_page.click_save()
#
# @then(u'user wants to get validation error message for postalcode field')
# def step_impl(context):
#     clientbasic_page = BasicinfoPage(context.driver)
#     clientbasic_page.validation_postalcode()
#
# @when(u'user enters the search keywords')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.enter_search("Test")
#
# @then(u'user wants to get the result regarding to the search')
# def step_impl(context):
#     #ss
#
# @when(u'user enters the search keywords which is not there in the table')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.enter_search("test1")
#
# @then(u'user will get the no data found message inside the table')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.error_searchmsg()
#
# @when(u'user selects the client name')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.select_clientname()
#
# @then(u'user will get the selected client name in the list')
# def step_impl(context):
#     #SS
#
# @when(u'user selects the client type')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.select_clienttype()
#
# @then(u'user will get the selected client type in the list')
# def step_impl(context):
#     #ss
#
# @when(u'user clicks on the reset button')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_reset()
#
# @then(u'filter fields will become empty')
# def step_impl(context):
#     # ss
#
# @when(u'user clicks on checkbox in the list')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_checkbox()
#
# @when(u'clicks ln the delete button')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_delete()
#
# @then(u'the confiration pop-up for delete will appear')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.confirmation_popup()
#
# @then(u'the user clicks on yes')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_yes()
#
# @then(u'the client will be deleted from the list')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.fetch_deletedmsg()
#
# @when(u'user clicks on the table settings')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_tablesetting()
#
# @then(u'user will get the pop-up of columns in the list')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.tablesetting_popup()
#
#
# @then(u'the user select or deselect the column name')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.select_columnname()
#
#
# @then(u'click on apply button')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_apply()
#
#
# @then(u'the list will be edited regarding the column changes')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.clientcolumn_table()
#
#
# @when(u'user clicks on the print icon')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_printicon()
#
#
# @then(u'user will get the pop-up for print to print the table')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.print_popup()
#
#
# @when(u'user clicks on the download icon')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_download()
#
#
# @then(u'it will download all the data in the table')
# def step_impl(context):
#     #refer
#
#
# @when(u'user clicks on the checkbox')
# def step_impl(context):
#
#
#
# @when(u'clicks on download icon')
# def step_impl(context):
#
#
#
# @then(u'user will get the selected clients detail downloaded')
# def step_impl(context):
#
#
#
# @when(u'user apply the filters')
# def step_impl(context):
#
#
#
# @when(u'click on the download icon')
# def step_impl(context):
#
#
#
# @then(u'user will get the applied filter client details')
# def step_impl(context):
#
#
#
# @when(u'user clicks on the arrow in the table header')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_sort()
#
#
# @then(u'the data will be sorted')
# def step_impl(context):
#     #SS
#
#
# @when(u'user toggle the button to active or inactive')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_toggle()
#
#
# @then(u'the client will activated or inactivated')
# def step_impl(context):
#     #SS
#
# @when(u'user clicks on the client name in the table')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.click_clientnametable()
#
# @then(u'user will be redirected to the client view page')
# def step_impl(context):
#     clientlist_page = BasicinfoPage(context.driver)
#     clientlist_page.fetch_clientview()
#
# @when(u'    And all the details will be fetched')
# def step_impl(context):
#     #SS