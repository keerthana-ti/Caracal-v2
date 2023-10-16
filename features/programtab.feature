#Feature: Program creation module
#  Scenario: Verify that the user is able to loggedin and redirected to program module
#    Given user is on the login page
#    When user enters the credentials
#    And click on the login
#    Then user is logged to dashboard page
#    When user clicks on the client module menu in side nav bar
#    Then user will be directed to client module page
#    And clicks on the add client button
#    Then click on program tab to view the list
#
#  Scenario: Verify that the user is able to directed to program add page when add button is clicked
#    Given user is on the program tab
#    When user clicks on the add button
#    Then user is redirected to program adding page
#
#  Scenario: Verify that the user is able to add the program to the list
#    Given user is on the program adding tab
#    When user selects the program name
#    And the program id, program value wants to be auotmtically fetched
#    Then the item and department details also need to be fetched automatically
#    And click on save button
#    Then the program will be displayed in the list
#
#  Scenario: Verify that the user is able to create a program and add in the list if need a new program
#    Given user is on the program tab
#    When user clicks on the add button
#    Then user will be redirected to add program page
#    And if the program needed was not there
#    Then the click on the create program button in the page
#    And the user will be redirected to create program page
#    And add all the neccessary details
#    And click on save
#    Then the program created will be displayed in the dropdown
#    And by selecting that user can able to add the program
#    Then the program is added in the list
#
#  Scenario: Verify that the user is able to get the department adding section by clicking add department button in add program page
#    Given user is on the program adding tab
#    When user clicks on the add department button
#    Then user will be able to get the department adding section below the list
#
#  Scenario: Verify that the user is able to add the department by giving all the details
#    Given user is on the program adding tab
#    When user selects the department name, active from , active to, description
#    And user will get the items fetched automatically
#    Then click on save button to get the department listed in the above table
#
#  Scenario: Verify that the user is able to set the tier price for the items in the department adding page
#    Given user is on the program adding page
#    When user clicks on the add department
#    And user enters the order limit
#    And add the tier 1 for the item
#    And enter start unit, discount
#    Then tier price will be automatically fetched
#    And click on save button
#
#  Scenario: Verify that the user is able to get the view and edit of the department by clicking the department name
#    Given user is on the program adding page
#    When user clicks on the department name
#    Then user will get the department details fetch in the page
#    And if any update needed while clicking on the fields
#    Then save button will appear to update it
#