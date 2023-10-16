Feature: Client management module - Add POC screen
  Scenario: Verify that the user is able to redirect contact info tab while clicking on contact info
    Given user is on the basic details tab
    When user clicks on contact tab
    Then user will be redirected to contact tab

  Scenario: Verify that the user is able to redirect to add POC page by clicking on add above the POC list table
    Given user is on the contact info tab
    When user clicks on the add button
    Then user is redirected to POC page

  Scenario: Verify that the user is able to enter the name , select the department
    Given user is on the add POC page
    When user enters the name
    And user selects the department

  Scenario: Verify that the user is able to enter designation, emailid
    Given user is on the add POC page
    When user enters the designation field
    Then user enters the email id field

  Scenario: Verify that the user is able to select country code, enter contact number, description
    Given user is on the add POC page
    When user selects the country code
    Then enter the contact number, description

  Scenario: Verify that the user is able to add address for the entered POC
    Given user is on the add POC page
    When user select the address title and enter address type
    Then click on save button to add the address to the entered POC

  Scenario: Verify that the user is able to make the specific address to primary address
    Given user is on the add POC page
    When user enters all the details
    Then check the primary address checkbox
    And the address is mapped as primary address to that POC

  Scenario: Verify that the user is able to add many address for a single POC
    Given user is on the add POC page
    When user clicks on add button
    Then user will get the another set to add the address details
    And user wants to add the address details
    Then the user is able to get the added extra address to POC details
    ###
  Scenario: Verify that the user is able to create a new address for that POC by redirecting to address adding page
    Given user is on the add POC page
    When user clicks on new button
    Then user will be redirected to add address details page

  Scenario: Verify that the user is able to add the address details in new address detail page
    Given user is on the new address
    When user enters all the address details
    Then user will get the new address saved if any POC mapping is not needed by clicking the save button

  Scenario: Verify that the user is able to add POC multiple POC to that new address entered
    Given user is on the new address
    When user enters the address details
    Then user is able to map the newly created address to the existing POC
    When user selects the name, department
    And clicks the checkbox primary POC
    Then the address is mapped to multiple POC

  Scenario: Verify that the user is able to get the added address displayed in the dropdown of address
    Given user is on the new address
    When user enters all the details in new address page
    Then user click on save
    And the saved address will be displayed in the dropdown

  Scenario: Verify that the primary POC is clicked in the new address then a validation should pop-up while clicking on newly added primary address in add POC page
    Given user is on the new address
    When user enters all the details in new address page
    And clicks on primary POC in new address page
    And user clicks on save
    Then user checks the newly added address as primary address in add POC page
    And user wants to get validation error message for primary address is already mapped to another POC

  Scenario: Verify that the user is able to get the mandatory and validation error message for the add POC page details
    Given user is on the add POC page
    When user enters the invalid or clicks on save witout the required details
    Then user will get the error messaga for that

  Scenario: Verify that the user is able to get the added POC listed in the table
    Given user is on the POC adding page
    When user enters all the details
    Then user will get the added POC in the POC table