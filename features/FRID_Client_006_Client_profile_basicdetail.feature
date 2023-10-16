#Feature: Client profile screen - Basic details
#  Scenario: Verify that the user is able to get the basic details view screen when client list id clicked
#    Given user is on the client list page
#    When user clicks on the client name
#    Then user will be redirected to the view page of basic details
#
#  Scenario: Verify that the user is able to get all the details of the client
#    Given user is on the client list page
#    When user clicks on the client name
#    Then user will be redirected to the view page of basic details
#    And the entered details will be fetched
#
#  Scenario: Verify that the user is able to get the fields editable by clicking the edit icon
#    Given user is on the client view page
#    When user clicks on edit icon
#    Then the fields will become editable fields
#
#  Scenario: Verify that the user is able to edit the fields and update it
#    Given user is on the client view page
#    When user edit the fields
#    And click on update button
#    Then user will get the details updated successfully
#
#  Scenario: Verify that the user is able to get edit the profile picture
#    Given user is on the client view page
#    When user clicks on the edit icon in the profile picture
#    Then user is able to upload the image to the profile section
#
#  Scenario: Verify that the user is able to assign the client to the specific person
#    Given user is on the client view page
#    When user clicks tha add button
#    Then user will get the dropdown of names
#    And the client will be assigned to taht specific person by selecting from dropdown
#
#  Scenario: Verify that the user is able to attach documents
#    Given user is on the client view page
#    When user clicks on the attachment icon
#    Then user can able to attach the documents related to that client
#    And the attached documents will be listed below the attachment field
#
#  Scenario: Verify that the user is able to create tags for that specific clients
#    Given user is on the client view page
#    When user clicks on the add tag field
#    And enter the tag in that field
#    Then the tags will be displayed in that section