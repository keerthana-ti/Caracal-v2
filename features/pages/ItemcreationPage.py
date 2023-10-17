from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage
import logging
from utilities.ConfigReader import read_configuration
import allure

log_format= "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='Itemcreation.log', level='INFO', format=log_format)

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
    create_item_xpath = "//button[@type = 'submit']"
    itempage_xpath = "//p[contains(text(), 'New Item']"
    itemname_xpath = "//input[@id = 'itemName']"
    itemtype_xpath = "//li[contains(text(), 'Consumable']"
    SKU_xpath = "//input[@id = 'sku']"
    itemid_xpath = "//input[@id = 'itemId']"
    supplier_xpath = "//input[@name = 'supplier']"
    unit_xpath = "//li[contains(text(), 'Case']"
    addunit_xpath = "//svg[@class='iconify iconify--ph']"
    unitpopup_xpath = "//p[contains(text(), 'Add Unit ']"
    unitname_xpath = "//input[@name = 'unit']"
    unitdesc_xpath = "//input[@name = 'name']"
    unitsave_xpath = "//button[@type = 'submit']"
    costprice_xpath = "//input[@name = 'costPrice']"
    sellingprice_xpath = "//input[@name = 'sellingPrice']"
    length_xpath = "//input[@name = 'length']"
    width_xpath = "//input[@name = 'width']"
    height_xpath = "//input[@name = 'height']"
    dimensionunit_xpath = "//li[contains(text(), 'cm']"
    weight_xpath = "//input[@name = 'weight']"
    weightunit_xpath = "//li[contains(text(), 'kg']"
    reorderlevel_xpath = "//input[@id = 'reorderLevel']"
    stock_limit_xpath = "//input[@id = 'stockLimit']"
    itemdesc_xpath = "//input[@name = 'description']"
    returnableitemcheckbox_xpath = "//input[@name = 'purchaseReturn']"
    attachment_xpath = "//label[contains(text(), 'Attachment']"
    # imageclick_xpath =
    saveitem_xpath = "//button[@type = 'submit']"
    mandatory_itemname_xpath = "//p[contains(text(), 'Item name is required']"
    mandatory_itemtype_xpath = "//p[contains(text(), 'Item type is required']"
    mandatory_unit_xpath = "//p[contains(text(), 'Unit Weight is required']"
    mandatory_costprice_xpath = "//p[contains(text(), 'Cost Price is required']"
    mandatory_weight_xpath = "//p[contains(text(), 'Item name is required']"
    mandatory_reorderlevel_xpath = "//p[contains(text(), 'Item name is required']"
    mandatory_sellingprice_xpath = "//p[contains(text(), 'Selling Price   is required']"
    # validation_itemname_xpath =
    # validation_costprice_xpath =
    # validation_sellingprice_xpath =
    # validation_dimensions_xpath =
    # validation_weight_xpath =
    # validation_reorderlevel_xpath =
    # validation_stocklimit_xpath =
    # validation_itemname_xpath =
    search_xpath = "//input[@id = ':R5aj3aqql4qqpkq:']"
    search_errmsg_xpath = "//div[contains(text(), 'No records found']"
    # all_xpath =
    # low_xpath =
    # expired_xpath =
    suppliername_xpath = "//li[contains(text(), 'test']"
    item_xpath = "//li[contains(text(), 'Consumable']"
    # reset_xpath =
    checkbox_program_xpath = "//input[@id = 'MUIDataTableSelectCell-029672361598387376-0']"
    # delete_program_xpath =
    # confirmation_program_xpath =
    # yes_programdelete_xpath =
    # deletedmsg_xpath =
    tablesettings_xpath = "//svg[@data-testid = 'TableChartOutlinedIcon']"
    popup_table_xpath = "//h1[contains(text(), 'Table Settings']"
    select_column_xpath = "//button[contains(text(), 'unitPrice']"
    apply_xpath = "//button[contains(text(), 'Apply']"
    columnchanges_xpath = "//div[contains(text(), 'UNIT PRICE']"
    print_xpath = "//svg[@class = 'iconify iconify--ion']"
    download_xpath = "//svg[@class = 'iconify iconify--ic']"
    clicksort_xpath = "//div[contains(text(), 'UNIT PRICE']"
    item_name_xpath = "//div[contains(text(), 'test']"
    # viewpage_xpath =
    # click_costprice =
    # fetch_save =
    # fetch_cancel =
    # click_saveinedit_xpath =
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

    def select_itemtype(self):
        self.click_on_element("itemtype_xpath", self.itemtype_xpath)
        logging.info("Item type selected")

    def fetch_SKU(self):
        logging.info("SKU fetched successfully")
        return self.isElementDisplayed("SKU_xpath", self.SKU_xpath)

    def fetch_itemid(self):
        logging.info("Item Id fetched successfully")
        return self.isElementDisplayed("itemid_xpath", self.itemid_xpath)

    def select_supplier(self):
        self.click_on_element("supplier_xpath", self.supplier_xpath)
        logging.info("Supplier name selected")

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
        self.click_on_element("dimensionunit_xpath", self.dimensionunit_xpath)
        logging.info("Dimension unit selected")

    def enter_weight(self, weight):
        self.sendText("weight_xpath", self.weight_xpath, weight)
        logging.info("Weight entered")

    def select_weightunit(self):
        self.click_on_element("weightunit_xpath", self.weightunit_xpath)
        logging.info("Weight unit selected")

    def enter_reorderlevel(self, reorderlevel):
        self.sendText("reorderlevel_xpath", self.reorderlevel_xpath, reorderlevel)
        logging.info("Reorderlevel entered")

    def enter_stocklimit(self, stocklimit):
        self.sendText("stocklimit_xpath", self.stocklimit_xpath, stocklimit)
        logging.info("Stocklimit entered")

    def enter_sellingprice(self, sellingprice):
        self.sendText("sellingprice_xpath", self.sellingprice_xpath, sellingprice)
        logging.info("Sellingprice entered")

    def enter_itemdescription(self, description):
        self.sendText("itemdesc_xpath", self.itemdesc_xpath, description)
        logging.info("Item descriptiom entered")

    def click_returnableitemcheckbox(self):
        self.click_on_element("returnableitemcheckbox_xpath", self.returnableitemcheckbox_xpath)
        logging.info("Returnable item checkbox clicked")

    def click_attachment(self):
        self.click_on_element("attachment_xpath", self.attachment_xpath)
        logging.info("Attachment field clicked")

    def click_attachedimage(self):
        self.click_on_element("imageclick_xpath", self.imageclick_xpath)
        logging.info("Attached image clicked")

    def click_savebutton(self):
        self.click_on_element("saveitem_xpath", self.saveitem_xpath)
        logging.info("Save button clicked")

    def mandatory_itemname(self):
        logging.info("Item name mandatory error message displayed")
        return self.isElementDisplayed("mandatory_itemname_xpath", self.mandatory_itemname_xpath)

    def mandatory_itemtype(self):
        logging.info("Item type mandatory error message displayed")
        return self.isElementDisplayed("mandatory_itemtype_xpath", self.mandatory_itemtype_xpath)

    def mandatory_unit(self):
        logging.info("Unit mandatory error message displayed")
        return self.isElementDisplayed("mandatory_unit_xpath", self.mandatory_unit_xpath)

    def mandatory_costprice(self):
        logging.info("Costprice mandatory error message displayed")
        return self.isElementDisplayed("mandatory_costprice_xpath", self.mandatory_costprice_xpath)

    def mandatory_weight(self):
        logging.info("Weight mandatory error message displayed")
        return self.isElementDisplayed("mandatory_weight_xpath", self.mandatory_weight_xpath)

    def mandatory_reorderlevel(self):
        logging.info("Reorderlevel mandatory error message displayed")
        return self.isElementDisplayed("mandatory_reorderlevel_xpath", self.mandatory_reorderlevel_xpath)

    def mandatory_sellingprice(self):
        logging.info("Selling price mandatory error message displayed")
        return self.isElementDisplayed("mandatory_sellingprice_xpath", self.mandatory_sellingprice_xpath)

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

    def select_supplier(self):
        self.click_on_element("suppliername_xpath", self.suppliername_xpath)
        logging.info("Suppliername selected")

    def select_item(self):
        self.click_on_element("item_xpath", self.item_xpath)
        logging.info("Item selected")

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

    def clientcolumn_table(self):
        logging.info("Column change affected")
        return self.isElementDisplayed("columnchanges_xpath", self.columnchanges_xpath)

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