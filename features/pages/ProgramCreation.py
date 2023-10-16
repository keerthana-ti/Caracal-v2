# import logging
# from selenium.webdriver.common.by import By
# from features.pages.BasePage import BasePage
# from utilities.ConfigReader import read_configuration
#
# log_format= "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename='Basicinfo.log', level='INFO', format=log_format)
#
# class ProgramCreationPage(BasePage):
#     def __init__(self,driver):
#         super().__init__(driver)
#
#     program_menu_xpath=
#     program_page_xpath=
#     add_program_xpath=
#     programadding_page_xpath=
#     program_name_xpath=
#     program_id_xpath=
#     itemname_dropdown__xpath=
#     select_item_xpath=
#     fetch_sellingprice_xpath=
#     fetch_programvalue_xpath=
#     fetch_firstitem_xpath=
#     next_row_xpath=
#     save_xpath=
#     create_item_xpath=
#     itempage_xpath=
#     itemname_xpath=
#     itemtype_xpath=
#     SKU_xpath=
#     itemid_xpath=
#     supplier_xpath=
#     unit_xpath=
#     addunit_xpath=
#     unitpopup_xpath=
#     unitname_xpath=
#     unitdesc_xpath=
#     unitsave_xpath=
#     costprice_xpath=
#     length_xpath=
#     width_xpath=
#     height_xpath=
#     dimensionunit_xpath=
#     weight_xpath=
#     weightunit_xpath=
#     reorderlevel_xpath=
#     stocklimit_xpath=
#     sellingprice_xpath=
#     itemdesc_xpath=
#     returnableitemcheckbox_xpath=
#     attachment_xpath=
#     imageclick_xpath=
#     saveitem_xpath=
#     mandatory_itemname_xpath=
#     mandatory_itemtype_xpath =
#     mandatory_unit_xpath =
#     mandatory_costprice_xpath =
#     mandatory_weight_xpath =
#     mandatory_reorderlevel_xpath =
#     mandatory_sellingprice_xpath =
#     validation_itemname_xpath=
#     validation_costprice_xpath =
#     validation_sellingprice_xpath =
#     validation_dimensions_xpath =
#     validation_weight_xpath =
#     validation_reorderlevel_xpath =
#     validation_stocklimit_xpath =
#     validation_itemname_xpath =
#     checkbox_xpath=
#     delete_xpath=
#     confirmation_popup_xpath=
#     yes_xpath=
#     itemdelete_success_xpath=
#     itemtoggleon_xpath=
#     itemtoggleoff_xpath=
#     itemsorting_xpath=
#     program_display_xpath=
#     search_xpath=
#     search_errmsg_xpath=
#     clientname_xpath=
#     item_xpath=
#     reset_xpath=
#     checkbox_program_xpath=
#     delete_program_xpath=
#     confirmation_program_xpath=
#     yes_programdelete_xpath=
#     programtoggleon_xpath=
#     programtoggleoff_xpath=
#     tablesettings_xpath=
#     popup_table_xpath=
#     select_column_xpath=
#     apply_xpath=
#     columnchanges_xpath=
#     print_xpath=
#     print_popup_xpath=
#     download_xpath=
#     clicksort_xpath=
#
#     def click_programmenu(self):
#         self.click_on_element("program_menu_xpath",self.program_menu_xpath)
#         logging.info("Program menu clicked")
#
#     def program_redirect(self):
#         logging.info("Redirected to program list page")
#         return self.isElementDisplayed("program_page_xpath",self.program_page_xpath)
#
#     def add_program(self):
#         self.click_on_element("add_program_xpath",self.add_program_xpath)
#         logging.info("Add program button clicked")
#
#     def programadd_redirect(self):
#         logging.info("Add program page redirected")
#         return self.isElementDisplayed("programadding_page_xpath", self.programadding_page_xpath)
#
#     def enter_programname(self,programname):
#         self.sendText("program_name_xpath",self.program_name_xpath,programname)
#         logging.info("Program name entered")
#
#     def fetch_programid(self):
#         logging.info("Program id fetched")
#         return self.isElementDisplayed("program_id_xpath", self.program_id_xpath)
#
#     def click_itemdropdown(self):
#         self.click_on_element("itemname_dropdown__xpath",self.itemname_dropdown__xpath)
#         logging.info("Item dropdown clicked")
#
#     def select_item(self):
#         self.click_on_element("select_item_xpath",self.select_item_xpath)
#         logging.info("Item selected")
#
#     def fetch_itemdata(self):
#         logging.info("Item data fetched")
#         return self.isElementDisplayed("fetch_sellingprice_xpath",self.fetch_sellingprice_xpath)
#
#     def fetch_programvalue(self):
#         logging.info("Program value fetched")
#         return self.isElementDisplayed("fetch_programvalue_xpath",self.fetch_programvalue_xpath)
#
#     def fetch_firstitem(self):
#         logging.info("First item row fetched")
#         return self.isElementDisplayed("fetch_firstitem_xpath", self.fetch_firstitem_xpath)
#
#     def fetch_nextrow(self):
#         logging.info("Next row fetched")
#         return self.isElementDisplayed("next_row_xpath", self.next_row_xpath)
#
#     def click_save(self):
#         self.click_on_element("save_xpath",self.save_xpath)
#         logging.info("Save button clicked")
#
#     def click_createitem(self):
#         self.click_on_element("create_item_xpath", self.create_item_xpath)
#         logging.info("Create item clicked")
#
#     def createitem_page(self):
#         logging.info("Redirected to item creation page")
#         return self.isElementDisplayed("itempage_xpath", self.itempage_xpath)
#
#     def enter_itemname(self, itemname):
#         self.sendText("itemname_xpath", self.itemname_xpath, itemname)
#         logging.info("Item name entered")
#
#     def select_itemtype(self):
#         self.click_on_element("itemtype_xpath", self.itemtype_xpath)
#         logging.info("Item type selected")
#
#     def fetch_SKU(self):
#         logging.info("SKU fetched successfully")
#         return self.isElementDisplayed("SKU_xpath", self.SKU_xpath)
#
#     def fetch_itemid(self):
#         logging.info("Item Id fetched successfully")
#         return self.isElementDisplayed("itemid_xpath", self.itemid_xpath)
#
#     def select_supplier(self):
#         self.click_on_element("supplier_xpath", self.supplier_xpath)
#         logging.info("Supplier name selected")
#
#     def select_unit(self):
#         self.click_on_element("unit_xpath", self.unit_xpath)
#         logging.info("Unit selected")
#
#     def addunit_button(self):
#         self.click_on_element("addunit_xpath", self.addunit_xpath)
#         logging.info("Add unit button clicked")
#
#     def unit_popup(self):
#         logging.info("Add unit popup displayed")
#         return self.isElementDisplayed("unitpopup_xpath", self.unitpopup_xpath)
#
#     def enter_unitname(self, unitname):
#         self.sendText("unitname_xpath", self.unitname_xpath, unitname)
#         logging.info("Unitname entered")
#
#     def enter_unitdesc(self, unitdescription):
#         self.sendText("unitdesc_xpath", self.unitdesc_xpath, unitdescription)
#         logging.info("Unit description entered")
#
#     def click_unitsave(self):
#         self.click_on_element("unitsave_xpath", self.unitsave_xpath)
#         logging.info("Save button clicked")
#
#     def enter_costprice(self, costprice):
#         self.sendText("costprice_xpath", self.costprice_xpath, costprice)
#         logging.info("Costprice entered")
#
#     def enter_length(self, length):
#         self.sendText("length_xpath", self.length_xpath, length)
#         logging.info("Length entered")
#
#     def enter_width(self, width):
#         self.sendText("width_xpath", self.width_xpath, width)
#         logging.info("Width entered")
#
#     def enter_height(self, height):
#         self.sendText("height_xpath", self.height_xpath, height)
#         logging.info("Height entered")
#
#     def select_dimensionunit(self):
#         self.click_on_element("dimensionunit_xpath", self.dimensionunit_xpath)
#         logging.info("Dimension unit selected")
#
#     def enter_weight(self, weight):
#         self.sendText("weight_xpath", self.weight_xpath, weight)
#         logging.info("Weight entered")
#
#     def select_weightunit(self):
#         self.click_on_element("weightunit_xpath", self.weightunit_xpath)
#         logging.info("Weight unit selected")
#
#     def enter_reorderlevel(self, reorderlevel):
#         self.sendText("reorderlevel_xpath", self.reorderlevel_xpath, reorderlevel)
#         logging.info("Reorderlevel entered")
#
#     def enter_stocklimit(self, stocklimit):
#         self.sendText("stocklimit_xpath", self.stocklimit_xpath, stocklimit)
#         logging.info("Stocklimit entered")
#
#     def enter_sellingprice(self, sellingprice):
#         self.sendText("sellingprice_xpath", self.sellingprice_xpath, sellingprice)
#         logging.info("Sellingprice entered")
#
#     def enter_itemdescription(self, description):
#         self.sendText("itemdesc_xpath", self.itemdesc_xpath, description)
#         logging.info("Item descriptiom entered")
#
#     def click_returnableitemcheckbox(self):
#         self.click_on_element("returnableitemcheckbox_xpath", self.returnableitemcheckbox_xpath)
#         logging.info("Returnable item checkbox clicked")
#
#     def click_attachment(self):
#         self.click_on_element("attachment_xpath", self.attachment_xpath)
#         logging.info("Attachment field clicked")
#
#     def click_attachedimage(self):
#         self.click_on_element("imageclick_xpath", self.imageclick_xpath)
#         logging.info("Attached image clicked")
#
#     def click_savebutton(self):
#         self.click_on_element("saveitem_xpath", self.saveitem_xpath)
#         logging.info("Save button clicked")
#
#     def mandatory_itemname(self):
#         logging.info("Item name mandatory error message displayed")
#         return self.isElementDisplayed("mandatory_itemname_xpath", self.mandatory_itemname_xpath)
#
#     def mandatory_itemtype(self):
#         logging.info("Item type mandatory error message displayed")
#         return self.isElementDisplayed("mandatory_itemtype_xpath", self.mandatory_itemtype_xpath)
#
#     def mandatory_unit(self):
#         logging.info("Unit mandatory error message displayed")
#         return self.isElementDisplayed("mandatory_unit_xpath", self.mandatory_unit_xpath)
#
#     def mandatory_costprice(self):
#         logging.info("Costprice mandatory error message displayed")
#         return self.isElementDisplayed("mandatory_costprice_xpath", self.mandatory_costprice_xpath)
#
#     def mandatory_weight(self):
#         logging.info("Weight mandatory error message displayed")
#         return self.isElementDisplayed("mandatory_weight_xpath", self.mandatory_weight_xpath)
#
#     def mandatory_reorderlevel(self):
#         logging.info("Reorderlevel mandatory error message displayed")
#         return self.isElementDisplayed("mandatory_reorderlevel_xpath", self.mandatory_reorderlevel_xpath)
#
#     def mandatory_sellingprice(self):
#         logging.info("Selling price mandatory error message displayed")
#         return self.isElementDisplayed("mandatory_sellingprice_xpath", self.mandatory_sellingprice_xpath)
#
#     def validation_itemname(self):
#         logging.info("Item name validation error message displayed")
#         return self.isElementDisplayed("validation_itemname_xpath", self.validation_itemname_xpath)
#
#     def validation_costprice(self):
#         logging.info("Cost price validation error message displayed")
#         return self.isElementDisplayed("validation_costprice_xpath", self.validation_costprice_xpath)
#
#     def validation_sellingprice(self):
#         logging.info("Selling price validation error message displayed")
#         return self.isElementDisplayed("validation_sellingprice_xpath", self.validation_sellingprice_xpath)
#
#     def validation_dimensions(self):
#         logging.info("Dimensions validation error message displayed")
#         return self.isElementDisplayed("validation_dimensions_xpath", self.validation_dimensions_xpath)
#
#     def validation_weight(self):
#         logging.info("Weight validation error message displayed")
#         return self.isElementDisplayed("validation_weight_xpath", self.validation_weight_xpath)
#
#     def validation_reorderlevel(self):
#         logging.info("Reorder level validation error message displayed")
#         return self.isElementDisplayed("validation_reorderlevel_xpath", self.validation_reorderlevel_xpath)
#
#     def validation_stocklimit(self):
#         logging.info("Stocklimit validation error message displayed")
#         return self.isElementDisplayed("mandatory_stocklimit_xpath", self.validation_stocklimit_xpath)
#
#     def click_item(self):
#         self.click_on_element("checkbox_xpath", self.checkbox_xpath)
#         logging.info("Item checkbox clicked")
#
#     def click_itemdelete(self):
#         self.click_on_element("delete_xpath", self.delete_xpath)
#         logging.info("Clicked item delete")
#
#     def item_confirmpopup(self):
#         logging.info("Confirm pop-up displayed")
#         return self.isElementDisplayed("confirmation_popup_xpath", self.confirmation_popup_xpath)
#
#     def click_yesinpopup(self):
#         self.click_on_element("yes_xpath", self.yes_xpath)
#         logging.info("Clicked yes in confirmation pop-up")
#
#     def deleted_success(self):
#         logging.info("Item deleted successfully")
#         return self.isElementDisplayed("itemdelete_success_xpath", self.itemdelete_success_xpath)
#
#     def click_itemtoggleOn(self):
#         self.click_on_element("itemtoggleon_xpath",self.itemtoggleon_xpath)
#         logging.info("Clicked item toggle on")
#
#     def click_itemtoggleoff(self):
#         self.click_on_element("itemtoggleoff_xpath", self.itemtoggleoff_xpath)
#         logging.info("Clicked item toggle off")
#
#     def click_itemsort(self):
#         self.click_on_element("itemsorting_xpath",self.itemsorting_xpath)
#         logging.info("Item sort arrow clicked")
#
#     def display_program(self):
#         logging.info("Program displayed in list page")
#         return self.isElementDisplayed("program_display_xpath", self.program_display_xpath)
#
#     def enter_search(self,searchkey):
#         self.sendText("search_xpath", self.search_xpath,searchkey)
#         logging.info("Search entered")
#
#     def get_searcherrormsg(self):
#         logging.info("Error message for search displayed")
#         return self.isElementDisplayed("search_errmsg_xpath", self.search_errmsg_xpath)
#
#     def select_clientname(self):
#         self.click_on_element("clientname_xpath", self.clientname_xpath)
#         logging.info("Clientname selected")
#
#     def select_item(self):
#         self.click_on_element("item_xpath", self.item_xpath)
#         logging.info("Item selected")
#
#     def click_reset(self):
#         self.click_on_element("reset_xpath",self.reset_xpath)
#         logging.info("Reset clicked")
#
#     def click_checkbox(self):
#         self.click_on_element("checkbox_program_xpath", self.checkbox_program_xpath)
#         logging.info("Checkbox clicked")
#
#     def click_deleteprogram(self):
#         self.click_on_element("delete_program_xpath", self.delete_program_xpath)
#         logging.info("Program deleted")
#
#     def confirmation_popup(self):
#         logging.info("Confirmation pop-up displayed")
#         return self.isElementDisplayed("confirmation_program_xpath", self.confirmation_program_xpath)
#
#     def click_yesin_delete(self):
#         self.click_on_element("yes_programdelete_xpath", self.yes_programdelete_xpath)
#         logging.info("Yes clicked")
#
#     def program_toggleon(self):
#         self.click_on_element("programtoggleon_xpath", self.programtoggleon_xpath)
#         logging.info("Program toggle on")
#
#     def program_toggleoff(self):
#         self.click_on_element("programtoggleoff_xpath", self.programtoggleoff_xpath)
#         logging.info("program toggle off")
#
#     def click_tablesetting(self):
#         self.click_on_element("tablesettings_xpath", self.tablesettings_xpath)
#         logging.info("Table setting clicked")
#
#     def tablesetting_popup(self):
#         logging.info("Table setting popup displayed")
#         return self.isElementDisplayed("popup_table_xpath", self.popup_table_xpath)
#
#     def select_columnname(self):
#         self.click_on_element("select_column_xpath", self.select_column_xpath)
#         logging.info("Column name selected")
#
#     def click_apply(self):
#         self.click_on_element("apply_xpath", self.apply_xpath)
#         logging.info("Apply button clicked")
#
#     def clientcolumn_table(self):
#         logging.info("Column change affected")
#         return self.isElementDisplayed("columnchanges_xpath", self.columnchanges_xpath)
#
#     def click_printicon(self):
#         self.click_on_element("print_xpath", self.print_xpath)
#         logging.info("Print icon clicked")
#
#     def print_popup(self):
#         logging.info("Popup visible for print")
#         return self.isElementDisplayed("print_popup_xpath", self.print_popup_xpath)
#
#     def click_download(self):
#         self.click_on_element("download_xpath", self.download_xpath)
#         logging.info("File downloaded")
#
#     def click_sort(self):
#         self.click_on_element("clicksort_xpath", self.clicksort_xpath)
#         logging.info("Program table sorted")
#
