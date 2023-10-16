Feature: Client management module - Contact tab list
  Scenario: Verify that the user is able to redirect contact info tab while clicking on contact info
    Given user is on the basic details tab
    When user clicks on contact tab
    Then user will be redirected to contact tab

  Scenario: Verify that the user is able to redirect to add address page by clicking on add above the address list table
    Given user is on the contact info tab
    When user clicks on the add button
    Then user is redirected to address page

  Scenario: Verify that the user is able to redirect to add POC page by clicking on add above the POC list table
    Given user is on the contact info tab
    When user clicks on the add button
    Then user is redirected to POC page

  Scenario: Verify that the user is able to get the added address listed in the table
    Given user is on the address adding page
    When user enters all the details
    Then user will get the added address in the address table

  Scenario: Verify that the user is able to delete the address from the table
    Given user is on the contact info page
    When user clicks the checkbox
    Then delete button will appear
    And clicks on delete button
    Then user wants to get confirmation pop-up
    And user clicks on the yes
    Then the address get deleted form the list

  Scenario: Verify that the user is able to get the added POC listed in the table
    Given user is on the POC adding page
    When user enters all the details
    Then user will get the added POC in the POC table

  Scenario: Verify that the user is able to delete the POC from the table
    Given user is on the contact info page
    When user clicks the checkbox
    Then delete button will appear
    And clicks on delete button
    Then user wants to get confirmation pop-up
    And user clicks on the yes
    Then the POC get deleted form the list