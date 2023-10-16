# import logging
# from selenium.webdriver.common.by import By
# from features.pages.BasePage import BasePage
# from utilities.ConfigReader import read_configuration
#
# log_format= "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename='Basicinfo.log', level='INFO', format=log_format)
#
# class BasicinfoPage(BasePage):
#     def __init__(self,driver):
#         super().__init__(driver)
#
#     login_page_xpath=
#     username_xpath=
#     password_xpath=
#     login_button_xpath=
#     dashboard_page_xpath=
#     client_menu_xpath=
#     client_page_xpath=
#     addclient_xpath=
#     basicinfo_page_xpath=
#     clientname_xpath=
#     clientid_xpath=
#     clienttype_xpath=
#     country_xpath=
#     taxid_xpath=
#     taxcategory_xpath=
#     industrytype_xpath=
#     website_xpath=
#     email_xpath=
#     countrycode_xpath=
#     telephonenumber_xpath=
#     mobilenumber_xpath=
#     faxnumber_xpath=
#     contractsignedyes_xpath=
#     contractsignedno_xpath=
#     contracttitle_xpath=
#     startdate_xpath=
#     enddate_xpath=
#     description_xpath=
#     documentattach_xpath=
#     addcontract_xpath=
#     addresstitle_xpath=
#     addresstype_xpath=
#     addressline1_xpath=
#     addressline2_xpath=
#     addressline3_xpath=
#     addaddressline_xpath=
#     addressline4_xpath=
#     addressline5_xpath=
#     countrycompany_xpath=
#     state_xpath=
#     city_xpath=
#     postalcode_xpath=
#     primarybilling_xpath=
#     primaryshipping_xpath=
#     save_xpath=
#     clientlist_xpath=
#     mandatory_clientname_xpath=
#     validation_clientname_xpath=
#     mandatory_clienttype_xpath=
#     mandatory_country_xpath=
#     mandatory_taxcate_xpath=
#     mandatory_indtype_xpath=
#     mandatory_email_xpath=
#     validation_email_xpath=
#     mandatory_telephone_xpath=
#     mandatory_mobile_xpath=
#     validation_telphone_xpath=
#     validation_mobile_xpath=
#     mandatory_conyes_xpath=
#     mandatory_conno_xpath=
#     mandatory_conttitle_xpath=
#     mandatory_stratdate_xpath=
#     mandatory_enddate_xpath=
#     mandatory_attach_xpath=
#     validation_conttitle_xpath=
#     mandatory_addresstitle_xpath=
#     validation_addresstitle_xpath=
#     mandatory_addresstype_xpath=
#     mandatory_addressline1_xpath=
#     mandatory_addressline2_xpath =
#     mandatory_addressline3_xpath =
#     mandatory_country_xpath =
#     mandatory_state_xpath =
#     mandatory_city_xpath =
#     mandatory_postalcode_xpath =
#     validation_postalcode_xpath=
#     search_xpath=
#     search_errmsg_xpath=
#     clientname_drop_xpath=
#     clienttype_drop__xpath=
#     reset_xpath=
#     checkbox_xpath=
#     delete_xpath=
#     confirmation_popup_xpath=
#     yes_xpath=
#     deletedmsg_xpath=
#     tablesett_xpath=
#     set_popup_xpath=
#     select_columnname_xpath=
#     apply_xpath=
#     column_changes_xpath=
#     print_xpath=
#     printpopup_xpath=
#     downloadicon_xpath=
#     sorting_xpath=
#     toggle_xpath=
#     clientnametable_xpath=
#     redirectclientview_xpath=
#
#     def login_page_nav(self):
#         logging.info("Login page launched")
#         return self.isElementDisplayed("login_page_xpath", self.login_page_xpath)
#
#     def enter_credentials(self,uname,pwd):
#         self.sendText("username_xpath", self.username_xpath, uname)
#         self.sendText("password_xpath", self.password_xpath, pwd)
#         logging.info("Username entered")
#         logging.info("Password entered")
#
#     def login_button(self):
#         self.click_on_element("login_button_xpath", self.login_button_xpath)
#         logging.info("Login button clicked")
#
#     def redirect_to_dashboard(self):
#         logging.info("Redirected to dashboard")
#         return self.isElementDisplayed("dashboard_page_xpath", self.dashboard_page_xpath)
#
#     def click_clientmodule(self):
#         self.click_on_element("client_menu_xpath", self.client_menu_xpath)
#         logging.info("Client module clicked")
#
#     def clientpage_nav(self):
#         logging.info("Navigated to client page")
#         return self.isElementDisplayed("client_page_xpath", self.client_page_xpath)
#
#     def add_clientbutton(self):
#         self.click_on_element("addclient_xpath", self.addclient_xpath)
#         logging.info("Add client button clicked")
#
#     def client_basicdetails_nav(self):
#         logging.info("Redirected to basic details tab")
#         return self.isElementDisplayed("basicinfo_page_xpath", self.basicinfo_page_xpath)
#
#     def enter_clientname(self,clientname):
#         self.sendText("clientname_xpath", self.clientname_xpath, clientname)
#         logging.info("Clientname entered")
#
#     def clientid_fetch(self):
#         logging.info("Clientid fetched")
#         return self.isElementDisplayed("clientid_xpath", self.clientid_xpath)
#
#     def select_clienttype(self):
#         self.click_on_element("clienttype_xpath", self.clienttype_xpath)
#         logging.info("Clienttype selected")
#
#     def select_country(self):
#         self.click_on_element("country_xpath", self.country_xpath)
#         logging.info("Clientname entered")
#
#     def enter_taxid(self,taxid):
#         self.sendText("taxid_xpath", self.taxid_xpath,taxid)
#         logging.info("Taxid entered")
#
#     def select_taxcategory(self):
#         self.click_on_element("taxcategory_xpath", self.taxcategory_xpath)
#         logging.info("Tax category selected")
#
#     def select_industrytype(self):
#         self.click_on_element("industrytype_xpath", self.industrytype_xpath)
#         logging.info("Industry type selected")
#
#     def enter_website(self,website):
#         self.sendText("website_xpath", self.website_xpath,website)
#         logging.info("website entered")
#
#     def enter_emailname(self,email):
#         self.sendText("email_xpath", self.email_xpath,email)
#         logging.info("Email entered")
#
#     def select_countrycode(self):
#         self.click_on_element("countrycode_xpath", self.countrycode_xpath)
#         logging.info("Countrycode selected")
#
#     def enter_telphoneno(self,telephoneno):
#         self.sendText("telephonenumber_xpath", self.telephonenumber_xpath, telephoneno)
#         logging.info("Telephone number entered")
#
#     def enter_mobileno(self, mobileno):
#         self.sendText("mobilenumber_xpath", self.mobilenumber_xpath, mobileno)
#         logging.info("Mobile number entered")
#
#     def enter_faxnumber(self, faxnumber):
#         self.sendText("faxnumber_xpath", self.faxnumber_xpath, faxnumber)
#         logging.info("Faxnumber entered")
#
#     def check_yes(self):
#         self.click_on_element("contractsignedyes_xpath", self.contractsignedyes_xpath)
#         logging.info("Yes clicked")
#
#     def check_no(self):
#         self.click_on_element("contractsignedno_xpath", self.contractsignedno_xpath)
#         logging.info("No clicked")
#
#     def enter_contracttitle(self, contracttitle):
#         self.sendText("contracttitle_xpath", self.contracttitle_xpath, contracttitle)
#         logging.info("Contract title entered")
#
#     def select_startdate(self):
#         self.click_on_element("startdate_xpath", self.startdate_xpath)
#         logging.info("Startdate selected")
#
#     def select_enddate(self):
#         self.click_on_element("enddate_xpath", self.enddate_xpath)
#         logging.info("Enddate selected")
#
#     def enter_description(self, description):
#         self.sendText("description_xpath", self.description_xpath, description)
#         logging.info("Description entered")
#
#     def contract_attachment(self):
#         self.click_on_element("documentattach_xpath", self.documentattach_xpath)
#         logging.info("Document attached")
#
#     def click_addcontract(self):
#         self.click_on_element("addcontract_xpath", self.addcontract_xpath)
#         logging.info("Contract added")
#
#     def enter_addresstitle(self,addresstitle):
#         self.sendText("addresstitle_xpath", self.addresstitle_xpath,addresstitle)
#         logging.info("Address title added")
#
#     def select_addresstype(self):
#         self.click_on_element("addresstype_xpath", self.addresstype_xpath)
#         logging.info("Address type selected")
#
#     def enter_addressline1(self, addressline):
#         self.sendText("addressline1_xpath", self.addressline1_xpath, addressline1)
#         logging.info("Addressline1 entered")
#
#     def enter_addressline2(self, addressline):
#         self.sendText("addressline2_xpath", self.addressline2_xpath, addressline2)
#         logging.info("Addressline2 entered")
#
#     def enter_addressline3(self, addressline):
#         self.sendText("addressline3_xpath", self.addressline3_xpath, addressline3)
#         logging.info("Addressline3 entered")
#
#     def add_addressline(self):
#         self.click_on_element("addaddressline_xpath", self.addaddressline_xpath)
#         logging.info("Addressline added")
#
#     def select_country(self):
#         self.click_on_element("countrycompany_xpath", self.countrycompany_xpath)
#         logging.info("Country selected")
#
#     def select_state(self):
#         self.click_on_element("state_xpath", self.state_xpath)
#         logging.info("State selected")
#
#     def select_city(self):
#         self.click_on_element("city_xpath", self.city_xpath)
#         logging.info("City selected")
#
#     def enter_postalcode(self, postalcode):
#         self.sendText("postalcode_xpath", self.postalcode_xpath, postalcode)
#         logging.info("Postalcode entered")
#
#     def select_primarybilling(self):
#         self.click_on_element("primarybilling_xpath", self.primarybilling_xpath)
#         logging.info("Primary billing selected")
#
#     def select_shipping(self):
#         self.click_on_element("primaryshipping_xpath", self.primaryshipping_xpath)
#         logging.info("Primary shipping selected")
#
#     def click_save(self):
#         self.click_on_element("save_xpath", self.save_xpath)
#         logging.info("Save button clicked")
#
#     def clientlist(self):
#         logging.info("Clientlist displayed")
#         return self.isElementDisplayed("clientlist_xpath", self.clientlist_xpath)
#
#     def mandatory_clientname(self):
#         return self.isElementDisplayed("mandatory_clientname_xpath", self.mandatory_clientname_xpath)
#
#     def validation_clientname(self):
#         return self.isElementDisplayed("validation_clientname_xpath", self.validation_clientname_xpath)
#
#     def mandatory_clienttype(self):
#         return self.isElementDisplayed("mandatory_clienttype_xpath", self.mandatory_clienttype_xpath)
#
#     def mandatory_country(self):
#         return self.isElementDisplayed("mandatory_country_xpath", self.mandatory_country_xpath)
#
#     def mandatory_taxcategory(self):
#         return self.isElementDisplayed("mandatory_taxcate_xpath", self.mandatory_taxcate_xpath)
#
#     def mandatory_industrytype(self):
#         return self.isElementDisplayed("mandatory_indtype_xpath", self.mandatory_indtype_xpath)
#
#     def mandatory_email(self):
#         return self.isElementDisplayed("mandatory_email_xpath", self.mandatory_email_xpath)
#
#     def validation_email(self):
#         return self.isElementDisplayed("validation_email_xpath", self.validation_email_xpath)
#
#     def mandatory_telephoneno(self):
#         return self.isElementDisplayed("mandatory_telephone_xpath", self.mandatory_telephone_xpath)
#
#     def mandatory_mobileno(self):
#         return self.isElementDisplayed("mandatory_mobile_xpath", self.mandatory_mobile_xpath)
#
#     def validation_telephoneno(self):
#         return self.isElementDisplayed("validation_telphone_xpath", self.validation_telphone_xpath)
#
#     def validation_mobileno(self):
#         return self.isElementDisplayed("validation_mobile_xpath", self.validation_mobile_xpath)
#
#     def mandatory_contractradioyes(self):
#         return self.isElementDisplayed("mandatory_conyes_xpath", self.mandatory_conyes_xpath)
#
#     def mandatory_contracttitle(self):
#         return self.isElementDisplayed("mandatory_conttitle_xpath", self.mandatory_conttitle_xpath)
#
#     def mandatory_startdate(self):
#         return self.isElementDisplayed("mandatory_stratdate_xpath", self.mandatory_stratdate_xpath)
#
#     def mandatory_enddate(self):
#         return self.isElementDisplayed("mandatory_enddate_xpath", self.mandatory_enddate_xpath)
#
#     def mandatory_attachment(self):
#         return self.isElementDisplayed("mandatory_attach_xpath", self.mandatory_attach_xpath)
#
#     def validation_contracttitle(self):
#         return self.isElementDisplayed("validation_conttitle_xpath", self.validation_conttitle_xpath)
#
#     def mandatory_addresstitle(self):
#         return self.isElementDisplayed("mandatory_addresstitle_xpath", self.mandatory_addresstitle_xpath)
#
#     def validation_addresstitle(self):
#         return self.isElementDisplayed("validation_addresstitle_xpath", self.validation_addresstitle_xpath)
#
#     def mandatory_addresstype(self):
#         return self.isElementDisplayed("mandatory_addresstype_xpath", self.mandatory_addresstype_xpath)
#
#     def mandatory_addressline1(self):
#         return self.isElementDisplayed("mandatory_addressline1_xpath", self.mandatory_addressline1_xpath)
#
#     def mandatory_addressline2(self):
#         return self.isElementDisplayed("mandatory_addressline2_xpath", self.mandatory_addressline2_xpath)
#
#     def mandatory_addressline3(self):
#         return self.isElementDisplayed("mandatory_addressline3_xpath", self.mandatory_addressline3_xpath)
#
#     def mandatory_country(self):
#         return self.isElementDisplayed("mandatory_country_xpath", self.mandatory_country_xpath)
#
#     def mandatory_state(self):
#         return self.isElementDisplayed("mandatory_state_xpath", self.mandatory_state_xpath)
#
#     def mandatory_city(self):
#         return self.isElementDisplayed("mandatory_city_xpath", self.mandatory_city_xpath)
#
#     def mandatory_postalcode(self):
#         return self.isElementDisplayed("mandatory_postalcode_xpath", self.mandatory_postalcode_xpath)
#
#     def validation_postalcode(self):
#         return self.isElementDisplayed("validation_postalcode_xpath", self.validation_postalcode_xpath)
#
#     def enter_search(self, searchkey):
#         self.sendText("search_xpath", self.search_xpath, searchkey)
#
#     # def search_result(self):
#     #     return self.isElementDisplayed("", self.)
#
#     def error_searchmsg(self):
#         return self.isElementDisplayed("search_errmsg_xpath", self.search_errmsg_xpath)
#
#     def select_clientname(self):
#         self.click_on_element("clientname_drop_xpath", self.clientname_drop_xpath)
#
#     def select_clienttype(self):
#         self.click_on_element("clienttype_drop__xpath", self.clienttype_drop__xpath)
#
#     def click_reset(self):
#         self.click_on_element("reset_xpath", self.reset_xpath)
#
#     def click_checkbox(self):
#         self.click_on_element("checkbox_xpath", self.checkbox_xpath)
#
#     def click_delete(self):
#         self.click_on_element("delete_xpath", self.delete_xpath)
#
#     def confirmation_popup(self):
#         return self.isElementDisplayed("confirmation_popup_xpath", self.confirmation_popup_xpath)
#
#     def click_yes(self):
#         self.click_on_element("yes_xpath", self.yes_xpath)
#
#     def fetch_deletedmsg(self):
#         return self.isElementDisplayed("deletedmsg_xpath", self.deletedmsg_xpath)
#
#     def click_tablesetting(self):
#         self.click_on_element("tablesett_xpath", self.tablesett_xpath)
#
#     def tablesetting_popup(self):
#         return self.isElementDisplayed("set_popup_xpath", self.set_popup_xpath)
#
#     def select_columnname(self):
#         self.click_on_element("select_columnname_xpath", self.select_columnname_xpath)
#
#     def click_apply(self):
#         self.click_on_element("apply_xpath", self.apply_xpath)
#
#     def clientcolumn_table(self):
#         return self.isElementDisplayed("column_changes_xpath", self.column_changes_xpath)
#
#     def click_printicon(self):
#         self.click_on_element("print_xpath", self.print_xpath)
#
#     def print_popup(self):
#         return self.isElementDisplayed("printpopup_xpath", self.printpopup_xpath)
#
#     def click_download(self):
#         self.click_on_element("downloadicon_xpath", self.downloadicon_xpath)
#
#     def click_sort(self):
#         self.click_on_element("sorting_xpath", self.sorting_xpath)
#
#     def click_toggle(self):
#         self.click_on_element("toggle_xpath", self.toggle_xpath)
#
#     def click_clientnametable(self):
#         self.click_on_element("clientnametable_xpath", self.clientnametable_xpath)
#
#     def fetch_clientview(self):
#         return self.isElementDisplayed("redirectclientview_xpath", self.redirectclientview_xpath)