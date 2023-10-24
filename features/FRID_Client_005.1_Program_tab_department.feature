Feature: Program tab - department mapping
  Scenario: Verify that the user is able to loggedin and redirected to program module
    Given user is on the login page
    When user enters the credentials
    And click on the login
    Then user is logged to dashboard page
    When user clicks on the client module menu in side nav bar
    Then user will be directed to client module page
    And clicks on the add client button
    Then click on program tab to view the list

  Scenario: Verify that the user is able to directed to program add page when add button is clicked
    Given user is on the program tab
    When user clicks on the add button
    Then user is redirected to program adding page

  Scenario: Verify that the user is able to add the program and redirected to add program page
    Given user is on the program adding page
    When user selects the program name
    And the program id, program value wants to be automatically fetched
    Then the item and department details also need to be fetched automatically
    And click on save button
    Then after the program saved it will redirect to add program page

  Scenario: Verify that the user is able to get the department adding section by clicking add department button in add program page
    Given user is on the program adding page
    When user clicks on the add department button
    Then user will be able to get the department adding section below the list

  Scenario: Verify that the user is able to add the department by giving all the details
    Given user is on the program adding page
    When user selects the department name, active from , active to, description
    And user will get the items fetched automatically
    Then click on save button to get the department listed in the above table

  Scenario: Verify that the user is able to set a tier price for the item while mapping the department and also the added tier wants to display in item list panel
    Given user is on the program adding page
    When user enters the department details
    Then user selects the item from the dropdown, enter the order limit
    And selects the tier name from the dropdown inside the table
    Then enters the start unit, discount
    And the tier price will be automatically calculated
    When user clicks the add tier button
    Then the item will be listed in the right side item list panel

  Scenario: Verify that the user is able to edit the added tier price by clicking item name in the item list
    Given user is on the program adding page
    When user clicks on the item name in the item list
    Then the user will get the details of the selected item displayed
    And if the user needs to edit the item tier price
    Then edit the details
    And click on save to update the details

  Scenario: Verify that once the tier price is set for an item the item will not display in the item dropdown
    Given user is on the program adding page
    When user saved a tier price for a item
    And user wants to add another item tier price
    Then the previously added item will not be displayed in dropdown

  Scenario: Verify that the user is able to get the next row with tier name dropdown automatically after selecting the first tier name
    Given user is on the program adding page
    When user selects the tier name from the dropdown
    Then user will get the second entry line automatically

  Scenario: Verify that the user is able to calculate the start unit from the number provided previously
    Given user is on the program adding page
    When user enters the start unit for the first tier as 10
    And user enteres the start unit for the second tier as 30
    Then the start unit for second tier wants to calculate from 11-30 item limit

  Scenario: Verify that the user is able to delete the tier price added by clicking the delete button
    Given user is on the program adding page
    When user checks the checkbox
    Then clicks on the delete icon
    And the tier price line will get deleted

  Scenario: Verify that the user is able to enable tax for the item by selecting the tax toggle
    Given user is on the program adding page
    When user selects the tax
    Then tax will be calculated for that item

  Scenario: Verify that the user is able to enable and disable the item for that specific program and department by toggling the item toggle
    Given user is on the program adding page
    When user on the toggle button
    Then user will get the item in the program and department

  Scenario: Verify that the user is able to remove the tier added item by clicking the remove icon in the item list
    Given user is on the program adding page
    When user clicks on the remove icon
    Then tier added item will be removed

  Scenario: Verify that the user is able to map the program to the department by clicking selecting the program name and other details
    Given User is on the program adding page
    When user selectes the program name
    Then user will get the details fetched for the program selected
    And user add department if not mapped
    Then after added department click on save button
    And the program mapped with the department in the add program page

  Scenario: Verify that the user is able to get the mandatory error message for department name
    Given user is on the program adding page
    When user clicks submit without department name
    Then user will get the mandatory error message for department name

  Scenario: Verify that the user is able to get the department module edit screen
    Given user is on the program page
    When user clicks the program name
    Then user will get the program details, item details, department details fetched
    And the department while clicking department details needs to fetch
    Then all the program details will be displayed
