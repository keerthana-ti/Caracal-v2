Feature: Program list module
  Scenario: Verify that the user is able to loggedin and redirected to program module
    Given user is on the login page
    When user enters the credentials
    And click on the login
    Then user is logged to dashboard page
    When user clicks on the client module menu in side nav bar
    Then user will be directed to program module page

  Scenario: Verify that the user is able to directed to program add page when add button is clicked
    Given user is on the program tab
    When user clicks on the add button
    Then user is redirected to program adding page

  Scenario: Verify that the user is able to add the program to the list
    Given user is on the program adding tab
    When user selects the program name
    And the program id, program value wants to be auotmtically fetched
    Then the item and department details also need to be fetched automatically
    And click on save button
    Then the program will be displayed in the list

  Scenario: Verify that the user is able to delete the program from the table
    Given user is on the program tab
    When user clicks the checkbox
    Then delete button will appear
    And clicks on delete button
    Then user wants to get confirmation pop-up
    And user clicks on the yes
    Then the program get deleted form the list