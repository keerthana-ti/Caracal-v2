Feature: Client profile screen - Program
  Scenario: Verify that the user is able to get the program details view screen when program tab is clicked
    Given user is on the client list page
    When user clicks on the client name
    Then user will be redirected to the view page of basic details
    And click on the program tab

  Scenario: Verify that the user is able to get the program list in that tab
    Given user is on the program tab
    When user get the program list in the table
    Then user will get the details listed in the table

  Scenario: Verify that the user is able to create a program and map department in program
    Given user is on the program tab
    When user clicks on add department
    Then program will be added in the list
    And department will be mapped in the add department screen
    When user clicks on create program in add program page
    Then a new program will be created

  Scenario: Verify that the user is able to edit the program details by clicking the program name in that list
    Given user is on the contact tab
    When user clicks on the program in the list
    Then user will be redirected to the address page

  Scenario: Verify that the user is able to get the fields editable by clicking the edit icon
    Given user is on the program view page
    When user clicks on edit icon
    Then the fields will become editable fields

  Scenario: Verify that the user is able to edit the fields and update it
    Given user is on the program view page
    When user edit the fields
    And click on update button
    Then user will get the details updated successfully