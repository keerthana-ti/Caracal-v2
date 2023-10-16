Feature: Client profile screen - Contact info
  Scenario: Verify that the user is able to get the contact info details view screen when contact info is clicked
    Given user is on the client list page
    When user clicks on the client name
    Then user will be redirected to the view page of basic details
    And click on the contact info tab

  Scenario: Verify that the user is able to get the address list, PoC list of contact info
    Given user is on the contact info tab
    When user get the address list in the table
    Then user will get the Poc list in the table

  Scenario: Verify that the user is able to add address and add POC in this view page also
    Given user is on the contact tab
    When user add address and add POC
    Then user wants to get it in the list

  Scenario: Verify that the user is able to edit the address details by clicking the address name in that list
    Given user is on the contact tab
    When user clicks on the address in the list
    Then user will be redirected to the address page

  Scenario: Verify that the user is able to get the fields editable by clicking the edit icon
    Given user is on the address view page
    When user clicks on edit icon
    Then the fields will become editable fields

  Scenario: Verify that the user is able to edit the fields and update it
    Given user is on the address view page
    When user edit the fields
    And click on update button
    Then user will get the details updated successfully

  Scenario: Verify that the user is able to edit the PoC details by clicking the address name in that list
    Given user is on the contact tab
    When user clicks on the PoC in the list
    Then user will be redirected to the PoC page

  Scenario: Verify that the user is able to get the fields editable by clicking the edt icon
    Given user is on the PoC view page
    When user clicks on edit icon
    Then the fields will become editable fields

  Scenario: Verify that the user is able to edit the fields and update it
    Given user is on the PoC view page
    When user edit the fields
    And click on update button
    Then user will get the details updated successfully