Feature: Program module view screen
  Scenario: Verify that the user is able to view the program and item details by clicking the program name in the list
    Given user is on the program module page
    When user clicks the program name
    Then user will get the program details, item details
    And the client list in the left panel

  Scenario: Verify that the user is able to edit the program details by clicking the edit icon
    Given user is on the program details page
    When user clicks the edit icon
    Then the field become editable
    And clicks the program description, edit it
    Then clicks on save button to reflect the changes

  Scenario: Verify that the user is able to get the department details by clicking the client name in the left panel
    Given user is on the program details page
    When user clicks on the client name
    Then user will get the department details for that client

  Scenario: Verify that the user is able to view the department with item tier price by clicking the department details in the list
    Given user is on the program details page
    When user clicks on the department name
    Then user will get the details of the department with item tier price details

  Scenario: Verify that the user is able to add the department in view screen also by clicking the add department button
    Given user is on the program details page
    When user clicks on the add department button
    Then user will get the department details adding section
    And enter the department name, other details
    Then clicks on save button to get the department added to the list

  Scenario: Verify that the user is able to remove the client from the list by clicking the remove icon
    Given user is on the program details page
    When user clicks the remove icon
    Then the client will be removed from the program
