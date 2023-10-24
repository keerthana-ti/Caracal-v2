Feature: Program module with client mapping
  Scenario: Verify that the user is able to loggedin and redirected to program module
    Given user is on the login page
    When user enters the credentials
    And click on the login
    Then user is logged to dashboard page
    When user clicks on the program module menu in side nav bar
    Then user will be directed to program module page

  Scenario: Verify that the user is able to get the program creation page with client panel in the left by clicking the new program in program list
    Given user is on program module page
    When user clicks new program button
    Then user will get the create program page with client panel in left

  Scenario: Verify that the user is able add the new program to get that display in the list
    Given user is on the program creation page
    When user enters the program details and item details
    Then click on save button to get the program listed in the table

  Scenario: Verify that the user is able to add the new program and get the client adding section if add in the client panel is clicked
    Given user is on the program creation page
    When user enters the program details and item details
    And clicks on add in the client panel
    Then the client mapping section will appear

  Scenario: Verify that the user is able to create a new program and map client for that program
    Given user is on the program creation page
    When user enters the program and item details
    And clicks on add in the client panel
    Then the client mapping section will appear
    And select client, department, active from, active to
    Then enter program notes
    And click on save button to map the client to that program

  Scenario: Verify that the user is able to set a tier price for the item while mapping the client and also the added tier wants to display in item list panel
    Given user is on the program creation page
    When user enters the client details
    Then user selects the item from the dropdown, enter the order limit
    And selects the tier name from the dropdown inside the table
    Then enters the start unit, discount
    And the tier price will be automatically calculated
    When user clicks the add tier button
    Then the item will be listed in the right side item list panel

  Scenario: Verify that the user is able to edit the added tier price by clicking item name in the item list
    Given user is on the program creation page
    When user clicks on the item name in the item list
    Then the user will get the details of the selected item displayed
    And if the user needs to edit the item tier price
    Then edit the details
    And click on save to update the details

  Scenario: Verify that once the tier price is set for an item the item will not display in the item dropdown
    Given user is on the program creation page
    When user saved a tier price for a item
    And user wants to add another item tier price
    Then the previously added item will not be displayed in dropdown

  Scenario: Verify that the user is able to get the next row with tier name dropdown automatically after selecting the first tier name
    Given user is on the program creation page
    When user selects the tier name from the dropdown
    Then user will get the second entry line automatically

  Scenario: Verify that the user is able to calculate the start unit from the number provided previously
    Given user is on the program creation page
    When user enters the start unit for the first tier as 10
    And user enteres the start unit for the second tier as 30
    Then the start unit for second tier wants to calculate from 11-30 item limit

  Scenario: Verify that the user is able to delete the tier price added by clicking the delete button
    Given user is on the program creation page
    When user checks the checkbox
    Then clicks on the delete icon
    And the tier price line will get deleted

  Scenario: Verify that the user is able to enable tax for the item by selecting the tax toggle
    Given user is on the program creation page
    When user selects the tax
    Then tax will be calculated for that item

  Scenario: Verify that the user is able to enable and disable the item for that specific program and client by toggling the item toggle
    Given user is on the program creation page
    When user on the toggle button
    Then user will get the item in the program and department

  Scenario: Verify that the user is able to remove the tier added item by clicking the remove icon in the item list
    Given user is on the program creation page
    When user clicks on the remove icon
    Then tier added item will be removed

  Scenario: Verify that the user is able to add client for the existing program
    Given user is on the program module page
    When user clicks on the program name in the list
    Then user get the program details with the client list panel in left
    And user clicks on the add button to map more clients to the existing program
    When user enters the client details
    Then user selects the item from the dropdown, enter the order limit
    And selects the tier name from the dropdown inside the table
    Then enters the start unit, discount
    And the tier price will be automatically calculated
    When user clicks the add tier button
    Then the item will be listed in the right side item list panel
    And click on save button to map the client with this existing program

  Scenario: Verify that the user is able to get the mandatory error message for client and department name in client mapping section
    Given user is on the program module page
    When user clicks on submit without client and department name
    Then user will get the mandatory error message
