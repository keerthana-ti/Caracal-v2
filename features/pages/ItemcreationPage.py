from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage
import logging
from utilities.ConfigReader import read_configuration
import allure

log_format= "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='Itemcreation.log', filemode = 'w', level='INFO', format=log_format)

class ItemPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    login_page_xpath = "//h4[contains(text(), 'Login')]"
    username_xpath = "//input[@name = 'userName']"
    password_xpath = "//input[@name = 'password']"
    login_button_xpath = "//button[@type = 'submit']"
    dashboard_page_xpath = "//h1[contains(text(), 'Dashboard')]"
    inventory_menu_xpath = "//span[contains(text(), 'Inventory')]"
    inventory_page_xpath = "//div[contains(text(), 'Inventory')]"
    sidenav_xpath = "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiIconButton-root') and contains(@class, 'sidenavButton')]"
    create_item_xpath = "//button[@type = 'submit']"
    itempage_xpath = "//p[@class = 'newItem_newItemHead__sckuc']"
    itemname_xpath = "//input[@id = 'itemName']"
    itemtypeid_xpath = "//div[@class='MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-jedpe8-MuiSelect-select-MuiInputBase-input-MuiOutlinedInput-input']"
    itemtype_xpath = "//li[@data-value='652537aa3bb0b22e273fa876']"
    SKU_xpath = "//input[@id = 'sku']"
    itemid_xpath = "//input[@id = 'itemId']"
    supplier_xpath = "//input[@name = 'supplier']"
    unittype_xpath = "//input[@name='itemUnitId']/ancestor::div[contains(@class,'MuiSelect-root')]"
    unit_xpath = "//li[@data-value='652537aa3bb0b22e273fa86d']"
    addunit_xpath = "(//div[@class='MuiGrid-root'])[1]/svg"
    unitpopup_xpath = "//p[contains(text(), 'Add Unit ']"
    unitname_xpath = "//input[@name = 'unit']"
    unitdesc_xpath = "//input[@name = 'name']"
    unitsave_xpath = "//button[@type = 'submit']"
    costprice_xpath = "//input[@name = 'costPrice']"
    sellingprice_xpath = "//input[@name = 'sellingPrice']"
    length_xpath = "//input[@name = 'length']"
    width_xpath = "//input[@name = 'width']"
    height_xpath = "//input[@name = 'height']"
    dimensionunittype_xpath = "//input[@name='unitLwh']/ancestor::div[contains(@class,'MuiSelect-root')]"
    dimensionunit_xpath = "//li[@data-value='cm']"
    weight_xpath = "//input[@name = 'weight']"
    weighttype_xpath = "//input[@name='unitWeight']/ancestor::div[contains(@class,'MuiSelect-root')]"
    weightunit_xpath = "//li[@data-value='g']"
    reorderlevel_xpath = "//input[@id = 'reorderLevel']"
    stock_limit_xpath = "//input[@id = 'stockLimit']"
    itemdesc_xpath = "//textarea[@name = 'description']"
    returnableitemcheckbox_xpath = "//input[@name = 'purchaseReturn']"
    attachment_xpath = "//label[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-fullWidth MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-fullWidth newItem_itemAttachment__SK3Y4 css-xsqe0f-MuiButtonBase-root-MuiButton-root']"
    # imageclick_xpath =
    saveitem_xpath = "//button[@type = 'submit']"
    mandatory_itemname_xpath = "//p[contains(text(), 'Item name is required')]"
    mandatory_itemtype_xpath = "//p[contains(text(), 'Item type is required')]"
    mandatory_unit_xpath = "//p[contains(text(), 'Unit Weight is required')]"
    mandatory_costprice_xpath = "//p[contains(text(), 'Cost Price is required')]"
    mandatory_weight_xpath = "//p[contains(text(), 'Item name is required')]"
    mandatory_reorderlevel_xpath = "//p[contains(text(), 'Item name is required')]"
    mandatory_sellingprice_xpath = "//p[contains(text(), 'Selling Price   is required')]"
    # validation_itemname_xpath =
    # validation_costprice_xpath =
    # validation_sellingprice_xpath =
    # validation_dimensions_xpath =
    # validation_weight_xpath =
    # validation_reorderlevel_xpath =
    # validation_stocklimit_xpath =
    # validation_itemname_xpath =
    search_xpath = "//div[contains(@class, 'MuiFormControl-root')]/descendant::input[@type='text']"
    search_errmsg_xpath = "//div[contains(text(), 'No records found')]"
    # all_xpath =
    # low_xpath =
    # expired_xpath =
    suppliernameclick_xpath = "//div[contains(@class, 'MuiFormControl-root') and contains(@class, 'MuiFormControl-fullWidth') and .//label[text()='Supplier']]"
    suppliername_xpath = "//li[@data-value='test']"
    itemnameclick_xpath = "//div[contains(@class, 'MuiFormControl-root') and contains(@class, 'MuiFormControl-fullWidth') and .//label[text()='Item Type']]"
    item_xpath = "//li[@data-value='Product']"
    # reset_xpath =
    checkbox_program_xpath = "//input[@type = 'checkbox']"
    # delete_program_xpath =
    # confirmation_program_xpath =
    # yes_programdelete_xpath =
    # deletedmsg_xpath =
    tablesettings_xpath = "//div[contains(@class, 'MuiGrid-root') and contains(@class, 'css-scwsia-MuiGrid-root')]"
    popup_table_xpath = "//h1[@class = 'tableSettings_tableSettingsHeader__gt6UG']"
    select_column_xpath = "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'tableSettings_defautbuttonId__HbqjZ') and contains(text(), 'unitPrice')]"
    apply_xpath = "//button[contains(@class, 'MuiButtonBase-root') and contains(text(), 'Apply')]"
    # columnchanges_xpath = "//th[contains(@class,'MuiTableCell-head') and contains(text(),'UNIT PRICE')]"
    print_xpath = "//div[contains(@class, 'MuiGrid-root') and contains(@class, 'css-1arhiqq-MuiGrid-root')]"
    download_xpath = "//div[contains(@class, 'MuiGrid-root') and contains(@class, 'css-1tbgb7m-MuiGrid-root')]"
    clicksort_xpath = "//div[contains(text(), 'UNIT PRICE']"
    item_name_xpath = "//div[contains(text(), 'Pendrive']"
    viewpage_xpath = "//p[contains(text(), 'Update Item')]"
    # fetch_updatepopup =
    # fetch_updatedsuccess =
    # cancel_xpath =

    def login_page_nav(self):
        logging.info("Login page launched")
        return self.isElementDisplayed("login_page_xpath", self.login_page_xpath)

    def enter_credentials(self, uname, pwd):
        self.sendText("username_xpath", self.username_xpath, uname)
        self.sendText("password_xpath", self.password_xpath, pwd)
        logging.info("Username entered")
        logging.info("Password entered")

    def login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        logging.info("Login button clicked")

    def redirect_to_dashboard(self):
        logging.info("Redirected to dashboard")
        return self.isElementDisplayed("dashboard_page_xpath", self.dashboard_page_xpath)

    def click_inventorymenu(self):
        self.click_on_element("inventory_menu_xpath", self.inventory_menu_xpath)
        logging.info("Inventory menu clicked")

    def close_sidenav(self):
        self.click_on_element("sidenav_xpath", self.sidenav_xpath)
        logging.info("Sidenav menu clicked")

    def inventory_redirect(self):
        logging.info("Redirected to Item list page")
        return self.isElementDisplayed("inventory_page_xpath", self.inventory_page_xpath)

    def click_createitem(self):
        self.click_on_element("create_item_xpath", self.create_item_xpath)
        logging.info("Create item clicked")

    def createitem_page(self):
        logging.info("Redirected to item creation page")
        return self.isElementDisplayed("itempage_xpath", self.itempage_xpath)

    def enter_itemname(self, itemname):
        self.sendText("itemname_xpath", self.itemname_xpath, itemname)
        logging.info("Item name entered")

    def click_itemtype(self):
        self.click_on_element("itemtypeid_xpath", self.itemtypeid_xpath)
        logging.info("Item type clicked")

    def select_itemtype(self):
        self.click_on_element("itemtype_xpath", self.itemtype_xpath)
        logging.info("Item type selected")

    def fetch_SKU(self):
        logging.info("SKU fetched successfully")
        return self.isElementDisplayed("SKU_xpath", self.SKU_xpath)

    def fetch_itemid(self):
        logging.info("Item Id fetched successfully")
        return self.isElementDisplayed("itemid_xpath", self.itemid_xpath)

    def enter_supplier(self, suppliername):
        self.sendText("supplier_xpath", self.supplier_xpath, suppliername)
        logging.info("Supplier name selected")

    def select_unittype(self):
        self.click_on_element("unittype_xpath", self.unittype_xpath)
        logging.info("unit dropdown clicked")

    def select_unit(self):
        self.click_on_element("unit_xpath", self.unit_xpath)
        logging.info("Unit selected")

    def addunit_button(self):
        self.click_on_element("addunit_xpath", self.addunit_xpath)
        logging.info("Add unit button clicked")

    def unit_popup(self):
        logging.info("Add unit popup displayed")
        return self.isElementDisplayed("unitpopup_xpath", self.unitpopup_xpath)

    def enter_unitname(self, unitname):
        self.sendText("unitname_xpath", self.unitname_xpath, unitname)
        logging.info("Unitname entered")

    def enter_unitdesc(self, unitdescription):
        self.sendText("unitdesc_xpath", self.unitdesc_xpath, unitdescription)
        logging.info("Unit description entered")

    def click_unitsave(self):
        self.click_on_element("unitsave_xpath", self.unitsave_xpath)
        logging.info("Save button clicked")

    def enter_costprice(self, costprice):
        self.sendText("costprice_xpath", self.costprice_xpath, costprice)
        logging.info("Costprice entered")

    def enter_length(self, length):
        self.sendText("length_xpath", self.length_xpath, length)
        logging.info("Length entered")

    def enter_width(self, width):
        self.sendText("width_xpath", self.width_xpath, width)
        logging.info("Width entered")

    def enter_height(self, height):
        self.sendText("height_xpath", self.height_xpath, height)
        logging.info("Height entered")

    def select_dimensionunit(self):
        self.click_on_element("dimensionunittype_xpath", self.dimensionunittype_xpath)
        self.click_on_element("dimensionunit_xpath", self.dimensionunit_xpath)
        logging.info("Dimension unit selected")

    def enter_weight(self, weight):
        self.sendText("weight_xpath", self.weight_xpath, weight)
        logging.info("Weight entered")

    def select_weightunit(self):
        self.click_on_element("weighttype_xpath", self.weighttype_xpath)
        self.click_on_element("weightunit_xpath", self.weightunit_xpath)
        logging.info("Weight unit selected")

    def enter_reorderlevel(self, reorderlevel):
        self.sendText("reorderlevel_xpath", self.reorderlevel_xpath, reorderlevel)
        logging.info("Reorderlevel entered")

    def enter_stocklimit(self, stocklimit):
        self.sendText("stock_limit_xpath", self.stock_limit_xpath, stocklimit)
        logging.info("Stocklimit entered")

    def enter_sellingprice(self, sellingprice):
        self.sendText("sellingprice_xpath", self.sellingprice_xpath, sellingprice)
        logging.info("Sellingprice entered")

    def enter_itemdescription(self, description):
        self.scrollTo("itemdesc_xpath", self.itemdesc_xpath)
        self.sendText("itemdesc_xpath", self.itemdesc_xpath, description)
        logging.info("Item descriptiom entered")

    def click_returnableitemcheckbox(self):
        self.click_on_element("returnableitemcheckbox_xpath", self.returnableitemcheckbox_xpath)
        logging.info("Returnable item checkbox clicked")

    def click_attachment(self):
        self.scrollTo("attachment_xpath", self.attachment_xpath)
        self.click_on_element("attachment_xpath", self.attachment_xpath)
        logging.info("Attachment field clicked")

    def click_attachedimage(self):
        self.click_on_element("imageclick_xpath", self.imageclick_xpath)
        logging.info("Attached image clicked")

    def click_savebutton(self):
        self.scrollTo("saveitem_xpath", self.saveitem_xpath)
        self.click_on_element("saveitem_xpath", self.saveitem_xpath)
        logging.info("Save button clicked")

    def mandatory_itemname(self):
        self.scrollTo("mandatory_itemname_xpath", self.mandatory_itemname_xpath)
        expected_message = "Please enter the item name"
        element = self.getLocatorType("mandatory_itemname_xpath", self.mandatory_itemname_xpath)
        actual_message = element.text
        try:
            assert actual_message == expected_message, f"Assertion failed. Expected: '{expected_message}', Actual: '{actual_message}'"
            logging.info("Item name mandatory error message displayed")
        except AssertionError as e:
            logging.error(e)
            raise e


    def mandatory_itemtype(self):
        self.scrollTo("mandatory_itemtype_xpath", self.mandatory_itemtype_xpath)
        expected_message = "Please select the item type"
        element = self.getLocatorType("mandatory_itemtype_xpath", self.mandatory_itemtype_xpath)
        actual_message = element.text
        try:
            assert actual_message == expected_message, f"Assertion failed. Expected: '{expected_message}', Actual: '{actual_message}'"
            logging.info("Item type mandatory error message displayed")
        except AssertionError as e:
            logging.error(e)
            raise e

    def mandatory_unit(self):
        self.scrollTo("mandatory_unit_xpath", self.mandatory_unit_xpath)
        expected_message = "please select the unit"
        element = self.getLocatorType("mandatory_unit_xpath", self.mandatory_unit_xpath)
        actual_message = element.text
        try:
            assert actual_message == expected_message, f"Assertion failed. Expected: '{expected_message}', Actual: '{actual_message}'"
            logging.info("Unit mandatory error message displayed")
        except AssertionError as e:
            logging.error(e)
            raise e

    def mandatory_costprice(self):
        expected_message = "Please enter the cost price"
        element = self.getLocatorType("mandatory_costprice_xpath", self.mandatory_costprice_xpath)
        actual_message = element.text
        try:
            assert actual_message == expected_message, f"Assertion failed. Expected: '{expected_message}', Actual: '{actual_message}'"
            logging.info("Costprice mandatory error message displayed")
        except AssertionError as e:
            logging.error(e)
            raise e

    def mandatory_weight(self):
        expected_message = "please enter the item weight"
        element = self.getLocatorType("mandatory_weight_xpath", self.mandatory_weight_xpath)
        actual_message = element.text
        try:
            assert actual_message == expected_message, f"Assertion failed. Expected: '{expected_message}', Actual: '{actual_message}'"
            logging.info("Weight mandatory error message displayed")
        except AssertionError as e:
            logging.error(e)
            raise e

    def mandatory_reorderlevel(self):
        expected_message = "Please enter the reorder limit"
        element = self.getLocatorType("mandatory_reorderlevel_xpath", self.mandatory_reorderlevel_xpath)
        actual_message = element.text
        try:
            assert actual_message == expected_message, f"Assertion failed. Expected: '{expected_message}', Actual: '{actual_message}'"
            logging.info("Reorder level mandatory error message displayed")
        except AssertionError as e:
            logging.error(e)
            raise e

    def mandatory_sellingprice(self):
        expected_message = "Please enter the selling price"
        element = self.getLocatorType("mandatory_sellingprice_xpath", self.mandatory_sellingprice_xpath)
        actual_message = element.text
        try:
            assert actual_message == expected_message, f"Assertion failed. Expected: '{expected_message}', Actual: '{actual_message}'"
            logging.info("Selling price mandatory error message displayed")
        except AssertionError as e:
            logging.error(e)

    def validation_itemname(self):
        logging.info("Item name validation error message displayed")
        return self.isElementDisplayed("validation_itemname_xpath", self.validation_itemname_xpath)

    def validation_costprice(self):
        logging.info("Cost price validation error message displayed")
        return self.isElementDisplayed("validation_costprice_xpath", self.validation_costprice_xpath)

    def validation_sellingprice(self):
        logging.info("Selling price validation error message displayed")
        return self.isElementDisplayed("validation_sellingprice_xpath", self.validation_sellingprice_xpath)

    def validation_dimensions(self):
        logging.info("Dimensions validation error message displayed")
        return self.isElementDisplayed("validation_dimensions_xpath", self.validation_dimensions_xpath)

    def validation_weight(self):
        logging.info("Weight validation error message displayed")
        return self.isElementDisplayed("validation_weight_xpath", self.validation_weight_xpath)

    def validation_reorderlevel(self):
        logging.info("Reorder level validation error message displayed")
        return self.isElementDisplayed("validation_reorderlevel_xpath", self.validation_reorderlevel_xpath)

    def validation_stocklimit(self):
        logging.info("Stocklimit validation error message displayed")
        return self.isElementDisplayed("mandatory_stocklimit_xpath", self.validation_stocklimit_xpath)

    def enter_search(self, searchkey):
        self.click_on_element("search_xpath", self.search_xpath)
        self.sendText("search_xpath", self.search_xpath, searchkey)
        logging.info("Search entered")

    def get_searcherrormsg(self):
        logging.info("Error message for search displayed")
        return self.isElementDisplayed("search_errmsg_xpath", self.search_errmsg_xpath)

    def get_all(self):
        self.click_on_element("all_xpath", self.all_xpath)
        logging.info("All is clicked")

    def get_low(self):
        self.click_on_element("low_xpath", self.low_xpath)
        logging.info("Low is clicked")

    def get_expired(self):
        self.click_on_element("expired_xpath", self.expired_xpath)
        logging.info("Expired is clicked")

    def click_supplier(self):
        self.click_on_element("suppliernameclick_xpath", self.suppliernameclick_xpath)
        logging.info("Supplier clicked")

    def select_supplier(self):
        self.click_on_element("suppliername_xpath", self.suppliername_xpath)
        logging.info("Suppliername selected")

    def click_itemtypemenu(self):
        self.click_on_element("itemnameclick_xpath", self.itemnameclick_xpath)
        logging.info("Item type clicked")

    def select_itemtypemenu(self):
        self.click_on_element("item_xpath", self.item_xpath)
        logging.info("Item type selected")

    def click_reset(self):
        self.click_on_element("reset_xpath", self.reset_xpath)
        logging.info("Reset clicked")

    def click_checkbox(self):
        self.click_on_element("checkbox_program_xpath", self.checkbox_program_xpath)
        logging.info("Checkbox clicked")

    def click_deleteprogram(self):
        self.click_on_element("delete_program_xpath", self.delete_program_xpath)
        logging.info("Program deleted")

    def confirmation_popup(self):
        logging.info("Confirmation pop-up displayed")
        return self.isElementDisplayed("confirmation_program_xpath", self.confirmation_program_xpath)

    def click_yesin_delete(self):
        self.click_on_element("yes_programdelete_xpath", self.yes_programdelete_xpath)
        logging.info("Yes clicked")

    def fetch_deletedmsg(self):
        logging.info("Deleted successfully")
        return self.isElementDisplayed("deletedmsg_xpath", self.deletedmsg_xpath)

    def click_tablesetting(self):
        self.click_on_element("tablesettings_xpath", self.tablesettings_xpath)
        logging.info("Table setting clicked")

    def tablesetting_popup(self):
        logging.info("Table setting popup displayed")
        return self.isElementDisplayed("popup_table_xpath", self.popup_table_xpath)

    def select_columnname(self):
        self.click_on_element("select_column_xpath", self.select_column_xpath)
        logging.info("Column name selected")

    def click_apply(self):
        self.click_on_element("apply_xpath", self.apply_xpath)
        logging.info("Apply button clicked")

    # def clientcolumn_table(self):
    #     logging.info("Column change affected")
    #     return self.isElementDisplayed("columnchanges_xpath", self.columnchanges_xpath)

    def click_printicon(self):
        self.click_on_element("print_xpath", self.print_xpath)
        logging.info("Print icon clicked")

    def click_download(self):
        self.click_on_element("download_xpath", self.download_xpath)
        logging.info("File downloaded")

    def click_sort(self):
        self.click_on_element("clicksort_xpath", self.clicksort_xpath)
        logging.info("Program table sorted")

    def click_itemname(self):
        self.click_on_element("item_name_xpath", self.item_name_xpath)
        logging.info("Itemname clicked")

    def redirect_viewpage(self):
        logging.info("Redirected to view page")
        return self.isElementDisplayed("viewpage_xpath", self.viewpage_xpath)

    def click_itemfield(self):
        self.click_on_element("click_costprice", self.click_costprice)
        logging.info("Clicked on costprice")

    def fetch_save(self):
        logging.info("Save button appeared")
        return self.isElementDisplayed("fetch_save", self.fetch_save)

    def fetch_cancel(self):
        logging.info("Cancel button appeared")
        return self.isElementDisplayed("fetch_cancel", self.fetch_cancel)

    def click_saveinedit(self):
        self.click_on_element("click_saveinedit_xpath", self.click_saveinedit_xpath)
        logging.info("Save clicked")

    def fetch_updateconfirmation(self):
        logging.info("Update confitmation popup appeared")
        return self.isElementDisplayed("fetch_updatepopup", self.fetch_updatepopup)

    def fetch_updatesuccess(self):
        logging.info("Update success message appeared")
        return self.isElementDisplayed("fetch_updatedsuccess", self.fetch_updatedsuccess)

    def click_cancel(self):
        self.click_on_element("cancel_xpath", self.cancel_xpath)
        logging.info("Cancel clicked")