# from behave import *
# from features.pages.ProgramCreation import ProgramCreationPage
# from features.pages.BasicinfoPage import BasicinfoPage
#
# @given(u'user is on the login page')
# def login_page(context):
#     login_page = ItemPage(context.driver)
#     login_page.login_page_nav()
#
# @when(u'user enters the credentials')
# def enter_cred(context):
#     login_page = ItemPage(context.driver)
#     login_page.enter_credentials("admin", "Password@123")
#     allure.attach(context.driver.get_screenshot_as_png(), name="Login details",
#                   attachment_type=allure.attachment_type.PNG)
#
# @when(u'click on the login')
# def click_login(context):
#     login_page = ItemPage(context.driver)
#     login_page.login_button()
#     time.sleep(5)
#
# @then(u'user is logged to dashboard page')
# def redirect_dashboard(context):
#     dashboard_page = ItemPage(context.driver)
#     dashboard_page.redirect_to_dashboard()
#     allure.attach(context.driver.get_screenshot_as_png(), name="Redirect to dashboard",
#                   attachment_type=allure.attachment_type.PNG)
#     time.sleep(5)
#
# @when(u'user clicks on the program module menu in side nav bar')
# def click_program(context):
#     dashboard_page = ProgramCreationPage(context.driver)
#     dashboard_page.click_programmenu()
#
# @then(u'user will be directed to program module page')
# def program_redirect(context):
#     program_page = ProgramCreationPage(context.driver)
#     program_page.program_redirect()
#
# @given(u'user is on the program menu')
# def program_page(context):
#     login_page(context)
#     enter_cred(context)
#     click_login(context)
#     redirect_dashboard(context)
#     click_program(context)
#     program_redirect(context)
#
# @when(u'user clicks on the add program button')
# def click_addprogram(context):
#     program_page = ProgramCreationPage(context.driver)
#     program_page.add_program()
#
# @then(u'user is redirected to program adding page')
# def redirect_addprogram(context):
#     program_page = ProgramCreationPage(context.driver)
#     program_page.programadd_redirect()
#
# @given(u'user is on the program adding page')
# def programadd_page(context):
#     program_page(context)
#     click_addprogram(context)
#     redirect_addprogram(context)
#
# @when(u'user enter the program name')
# def enter_progname(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.enter_programname("Program1")
#
# @then(u'the program id is automatically fetched')
# def fetch_progid(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.fetch_programid()
#
# @when(u'user clicks on the dropdown inside the item name table column')
# def click_item(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.click_itemdropdown()
#
# @when(u'selects the item from the dropdown')
# def select_item(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.select_item()
#
# @then(u'user will get all the details automatically fetched')
# def item_data(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.fetch_itemdata()
#
# @then(u'the program value will be displayed based on the items selling price displayed in the table')
# def fetch_sellingprice(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.fetch_programvalue()
#
# @when(u'user selects the item from the dropdown in the item name table column')
# def select_item(context):
#     program_page(context)
#     click_addprogram(context)
#     redirect_addprogram(context)
#     enter_progname(context)
#     fetch_progid(context)
#     click_item(context)
#     select_item(context)
#
# @then(u'all the details of the item will be fetched in the table automatically')
# def fetch_itemdet(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.fetch_firstitem()
#
# # @then(u'after selected the first item name')
# # def step_impl(context):
# #     #SS of table with first item
#
# # @then(u'the user will get the another row for adding another item')
# # def step_impl(context):
# #     programcreation_page = ProgramCreationPage(context.driver)
# #     programcreation_page.fetch_nextrow()
#
# @then(u'click on save button to map the added item to the program creating')
# def click_save(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.click_save()
#
# @when(u'user clicks on the create item button')
# def click_createitem(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.click_createitem()
#
# @then(u'user will be redirected to item adding page')
# def item_page(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.createitem_page()
#
# @given(u'user is on the new item page')
# def new_item(context):
#     program_page(context)
#     click_addprogram(context)
#     redirect_addprogram(context)
#     click_createitem(context)
# @when(u'user enters itemname, select item type')
# def enter_itemname(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.enter_itemname("Pen")
#     newitem_page.select_itemtype()
#
# @when(u'SKU, item id will be autogenerated')
# def fetch_Skuitemid(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.fetch_SKU()
#     newitem_page.fetch_itemid()
#
# @when(u'user selects supplier, unit')
# def select_supplierunit(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.select_supplier()
#     newitem_page.select_unit()
#
# @when(u'enter costprice in that field')
# def enter_costprice(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.enter_costprice("23.90")
#
# @when(u'user clicks on the add icon in the page')
# def click_addicon(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.addunit_button()
#
# @then(u'user will get the pop-up to enter unit details')
# def enter_unit(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.unit_popup()
#
# @then(u'the user enters the details')
# def enter_details(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.enter_unitname()
#     newitem_page.enter_unitdesc()
#
# @then(u'click on add to get the unit in the dropdown')
# def click_add(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.click_unitsave()
#     newitem_page.select_unit()
#
# @when(u'user enters the length, width, height')
# def enter_lwh(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.enter_length("10")
#     newitem_page.enter_width("10")
#     newitem_page.enter_height("10")
#
# @when(u'enters the weight in that field')
# def enter_weight(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.enter_weight("10")
#
# @then(u'selects the unit for both fields')
# def select_unit(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.select_dimensionunit()
#     newitem_page.select_weightunit()
#
# @when(u'user enters the reorder level, stock limit')
# def enter_reorderstock(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.enter_reorderlevel("20")
#     newitem_page.enter_stocklimit("30")
#
# @then(u'user enters the selling price')
# def enter_sellingprice(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.enter_sellingprice("23.32")
#
# @when(u'user enter the description')
# def enter_description(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.enter_itemdescription("Testing")
#
# @when(u'click the returnable item checkbox')
# def click_returnableitem(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.click_returnableitemcheckbox()
#
# @when(u'user clicks on the attachment icon')
# def click_attachmenticon(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.click_attachment()
#
# @when(u'attaches the image')
# def attach_image(context):
#     #attach image functions
#     pass
# @then(u'user is abe to get the list of imaged attched below the field')
# def list_image(context):
#     # SS
#     pass
#
# @then(u'user clicks on the image it will give a pop-up of that clicked image')
# def popup_image(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.click_attachedimage()
#
# @when(u'user enters all the details')
# def enter_alldetails(context):
#     enter_itemname(context)
#     fetch_Skuitemid(context)
#     select_supplierunit(context)
#     enter_costprice(context)
#     click_addicon(context)
#     enter_unit(context)
#     enter_details(context)
#     click_add(context)
#     enter_lwh(context)
#     enter_weight(context)
#     select_unit(context)
#     enter_reorderstock(context)
#     enter_sellingprice(context)
#     enter_description(context)
#     click_returnableitem(context)
#     click_attachmenticon(context)
#     attach_image(context)
#
# @when(u'clicks on save button')
# def click_save(context):
#     newitem_page = ProgramCreationPage(context.driver)
#     newitem_page.click_savebutton()
#
# @then(u'the page will be redirected to program creation page')
# def redirect_programcreate(context):
#     #put assert in page
#     pass
#
# @then(u'if the user clicks on the item name dropdown')
# def click_itemname(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.select_item()
#
# @then(u'the item added will be displayed')
# def step_impl(context):
#     # ss of the item name page
#     pass
#
# # @when(u'user clicks on save button without entering item name, item type, unit')
# # def save_itemname(context):
# #     newitem_page = ProgramCreationPage(context.driver)
# #     newitem_page.click_savebutton()
# #
# # @then(u'user will get the mandatory error message for item name, item type, unit fields')
# # def mandate_(context):
# #     newitem_page = ProgramCreationPage(context.driver)
# #     newitem_page.mandatory_itemname()
# #     newitem_page.mandatory_itemtype()
# #     newitem_page.mandatory_unit()
# #
# # @when(u'user clicks on save button without entering cost price, weight, reorder level, selling price')
# # def step_impl(context):
# #     newitem_page = ProgramCreationPage(context.driver)
# #     newitem_page.click_savebutton()
# #
# # @then(u'user will get the mandatory error message for cost price, weight, reorder level, selling price fields')
# # def step_impl(context):
# #     newitem_page = ProgramCreationPage(context.driver)
# #     newitem_page.mandatory_costprice()
# #     newitem_page.mandatory_weight()
# #     newitem_page.mandatory_reorderlevel()
# #     newitem_page.mandatory_sellingprice()
# #
# # @when(u'user enters other than alphanumeric in the item name')
# # def step_impl(context):
# #     newitem_page = ProgramCreationPage(context.driver)
# #     newitem_page.enter_itemname("@12#")
# #
# # @then(u'user will get the validation error message for item name')
# # def step_impl(context):
# #     newitem_page = ProgramCreationPage(context.driver)
# #     newitem_page.validation_itemname()
# #
# # @then(u'SKU, Item id needs to be in alphanumeric')
# # def step_impl(context):
# #     newitem_page = ProgramCreationPage(context.driver)
# #     newitem_page.fetch_SKU()
# #     newitem_page.fetch_itemid()
# #
# # @when(u'user enters other than numbers in the cost price, selling price, dimensions, weight, reorder level, stock limit')
# # def step_impl(context):
# #     newitem_page = ProgramCreationPage(context.driver)
# #     newitem_page.enter_costprice("test")
# #     newitem_page.enter_sellingprice("test")
# #     newitem_page.enter_length("test")
# #     newitem_page.enter_width("test")
# #     newitem_page.enter_height("test")
# #     newitem_page.enter_weight("test")
# #     newitem_page.enter_reorderlevel("test")
# #     newitem_page.enter_stocklimit("test")
# #
# # @then(u'user will get the validation error message for cost price, selling price, dimensions, weight, reorder level, stock limit fields')
# # def step_impl(context):
# #     newitem_page = ProgramCreationPage(context.driver)
# #     newitem_page.validation_costprice()
# #     newitem_page.validation_sellingprice()
# #     newitem_page.validation_dimensions()
# #     newitem_page.validation_weight()
# #     newitem_page.validation_reorderlevel()
# #     newitem_page.validation_stocklimit()
#
# @when(u'user clicks on checkbox in the list')
# def click_checkbox(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.click_itemcheckbox()
#
# @when(u'clicks ln the delete button')
# def click_delete(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.click_itemdelete()
#
# @then(u'the confiration pop-up for delete will appear')
# def confirmation_popup(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.item_confirmpopup()
#
# @then(u'the user clicks on yes')
# def click_yes(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.click_yesinpopup()
#
# @then(u'the item will be deleted from the list')
# def item_deleted(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.deleted_success()
#
# @when(u'user toggle the button on')
# def item_toggle(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.click_itemtoggleOn()
#
# @then(u'the item will be mapped to that program')
# def item_mapping(context):
#     # screenshot
#     pass
#
# @when(u'user toggle the button off')
# def toggle_off(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.click_itemtoggleoff()
#
# @then(u'the item will not be mapped')
# def item_mappingprog(context):
#     # screenshot
#     pass
#
# @when(u'user clicks on the arrow in the table header')
# def click_sort(context):
#     programcreation_page = ProgramCreationPage(context.driver)
#     programcreation_page.click_itemsort()
#
# @then(u'the data will be sorted')
# def data_sort(context):
#     # screenshot of that step
#     pass
#
# @when(u'user add all the details needed')
# def enter_progdet(context):
#     # call all the function to add program and item
#     pass
#
#
# @then(u'user will get the program displayed in the program list table')
# def prog_list(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.display_program()
#
# @given(u'user is on the program list page')
# def prog_listpage(context):
#     #call the functions to achieve this
#     pass
#
# @when(u'user enters the search keywords')
# def search_keywords(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.enter_search("Program1")
#
# @then(u'user wants to get the result regarding to the search')
# def search_result(context):
#     # Screenshot of serach results
#     pass
#
# @when(u'user enters the search keywords which is not there in the table')
# def search_keyword(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.enter_search("test")
#
# @then(u'user wants to get the no data found message inside the table')
# def search_errmsg(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.get_searcherrormsg()
#
# # @when(u'user selects the client name')
# # def client_name(context):
# #     programlist_page = ProgramCreationPage(context.driver)
# #     programlist_page.select_clientname()
# #
# # @then(u'user will get the selected client name in the list')
# # def select_clientname(context):
# #     #screenshot
#
# @when(u'user selects the item')
# def select_item(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.select_item()
#
# @then(u'user will get the selected item in the list')
# def select_itemlist(context):
#     #screenshot
#     pass
#
# @when(u'user clicks on the reset button')
# def reset_button(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.click_reset()
#
# @then(u'filter fields will become empty')
# def filter_empty(context):
#     #SS
#     pass
#
# @when(u'user clicks on checkbox in the list in program table')
# def click_programcheckbox(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.click_checkbox()
#
# @when(u'clicks ln the delete button in program list page')
# def delete_program(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.click_deleteprogram()
#
# @then(u'the confiration pop-up for delete will appear in program list page')
# def confirmation_popup(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.confirmation_popup()
#
# @then(u'the user clicks on yes in the pop-up')
# def click_yesinpopup(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.click_yesin_delete()
#
# @then(u'the program will be deleted from the list')
# def program_list(context):
#     # SS
#     pass
#
# @when(u'user toggle the button on in program table')
# def program_toggleon(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.program_toggleon()
#
# @then(u'the program will be mapped')
# def program_mapping(context):
#     #SS
#     pass
#
# @when(u'user toggle the button off in program table')
# def toggle_off(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.program_toggleoff()
#
# @then(u'the program will not be mapped')
# def program_mappinglist(context):
#     #SS
#     pass
#
# @when(u'user clicks on the table settings')
# def table_settings(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.click_tablesetting()
#
# @then(u'user will get the pop-up of columns in the list')
# def tablesetting_popup(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.tablesetting_popup()
#
# @then(u'the user select or deselect the column name')
# def select_columnname(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.select_columnname()
#
# @then(u'click on apply button')
# def click_apply(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.click_apply()
#
# @then(u'the list will be edited regarding the column changes')
# def columnchange(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.clientcolumn_table()
#
# @when(u'user clicks on the print icon')
# def click_print(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.click_printicon()
#
# @then(u'user will get the pop-up for print to print the table')
# def print_popup(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.print_popup()
#
# @when(u'user clicks on the download icon')
# def click_download(context):
#     programlist_page = ProgramCreationPage(context.driver)
#     programlist_page.click_download()
#
# @then(u'it will download all the data\'s in the table')
# def downloaded_data(context):
#     #refer to open excel
#     pass
#
# @when(u'user clicks on the checkbox')
# def click_programcb(context):
#     click_programcheckbox(context)
#
# @then(u'user will get the selected program detail downloaded')
# def select_download(context):
#     # refer to open excel
#     pass
#
# @when(u'user apply the filters')
# def apply_filters(context):
#     click_itemname(context)
#
# @then(u'user will get the applied filter program details')
# def filter_program(context):
#     # refer to open excel
#     pass