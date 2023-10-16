Feature: Client management module - Add address screen
Scenario: Verify that the user is able to redirect contact info tab while clicking on contact info
    Given user is on the basic details tab
    When user clicks on contact tab
    Then user will be redirected to contact tab

  Scenario: Verify that the user is able to redirect to add address page by clicking on add above the address list table
    Given user is on the contact info tab
    When user clicks on the add button
    Then user is redirected to address page

  Scenario: Verify that the user is able to add address by entering address title, select address type, department
    Given user is on the address adding page
    When user enters the address title
    And selects the address type
    Then selects the department from the dropdown

  Scenario: Verify that the user is able to add the department by clicking the add button
    Given user is on the address adding page
    When user clicks on the add button
    Then user will get the pop-up for adding the department
    And user enters the department name
    Then clicks on save button
    And the dropdown is updated with the added department

  Scenario: Verify that the user is able to enter address line and add exta address lines
    Given user is on the address adding page
    When user enters the address line1, addressline2
    And user clicks on add button
    Then user will get the extra address lines to add
    And enters the addressline3, 4 if needed

  Scenario: Verify that the user is able to select the country, state, city
    Given user is on the address adding page
    When user selects the country
    And selects the displayed state
    Then select the city

  Scenario: Verify that the user is able to enter postal code, select country code, enter telphone number, mobile number, fax number, description
    Given user is on the address adding page
    When user enter postal code
    And user selects country code
    Then user enter telphone number, mobile number, fax number, description

  Scenario: Verify that the user is able to make the address entered as primary billing and shipping address
    Given user is on the address adding page
    When user selects the primary billing address
    Then user selects the primary shipping address to make the address as primary

  Scenario: Verify that the user is able to add poc for the entered address
    Given user is on the address adding page
    When user select the POC name and department
    Then click on save button to add the POC to the entered address

  Scenario: Verify that the user is able to make the specific POC to primary POC
    Given user is on the address adding page
    When user enters all the details
    Then check the primary poc checkbox
    And the POC is mapped as primary POC to that address

  Scenario: Verify that the user is able to add many POC for a single address
    Given user is on the address adding page
    When user clicks on add button
    Then user will get the another set to add the POC details
    And user wants to add the POC details
    Then the user is able to get the added extra POC to address details

  Scenario: Verify that the user is able to create a new POC for that address by redirecting to POC adding page
    Given user is on the address adding page
    When user clicks on new button
    Then user will be redirected to add POc details page

  Scenario: Verify that the user is able to add the POC details in new POC detail page
    Given user is on the new POC
    When user enters the name, select department, enter designation
    Then user enters the email, select country code, enter contact number, description

  Scenario: Verify that the user is able to add address multiple address to that new POC entered
    Given user is on the new POC
    When user enters the POC details
    Then user is able to map the newly created POC to the existing addresses
    When user selects the address title, enter address type
    And clicks the checkbox primary address
    Then the POC is mapped to multiple address

  Scenario: Verify that the user is able to get the added POC displayed in the dropdown of POC
    Given user is on the new POC
    When user enters all the details in new POC page
    Then user click on save
    And the saved POC will be displayed in the dropdown

  Scenario: Verify that the primary address is clicked in the new POC then a validation should pop-up while clicking on newly added primary POC in add address page
    Given user is on the new POC
    When user enters all the details in new POC page
    And clicks on primary address in new POC page
    And user clicks on save
    Then user checks the newly added POC as primary POC in add address page
    And user wants to get validation error message for primary POC is already mapped to another address

  Scenario: Verify that the user is able to get the mandatory and validation error message for address title field
    Given user is on the address adding page
    When user clicks on save button without address title
    Then user wants to get the mandatory error message
    When user enters other than alphanumeric values
    And user enters already exists address title
    Then user needs to get the validation error message

  Scenario: Verify that the user is able to get the mandatory error message for address type and department
    Given user is on the address adding page
    When user clicks on save button
    Then user will get the mandatory error message for address type and department

  Scenario: Verify that the user is able to get the mandatory error message while submitting without address line 1 field
    Given user is on the address adding page
    When user clicks on the save button without address line 1
    Then user will get the mandatory error message for address line 1 field

  Scenario: Verify that the user is able to get the mandatory error message while submitting without selecting country, state, city, postalcode
    Given user is on the address adding page
    When user clicks on the save button without selecting country, state, city, postalcode
    Then user will get the mandatory error message for country, state, city, postalcode

  Scenario: Verify that the user is able to enter only number not text in telephone number, mobile number, fax number
    Given user is on the address adding page
    When user enters the text in telephone number, mobile number
    Then the user would not be able to enter the text

  Scenario: Verify that the user is able to get the mandatory error message for submitting without mobile number field
    Given user is on the address adding page
    When user clicks on save button without entering the mobile number field
    Then user will get the mandatory error message for mobile number field

  Scenario: Verify that the user is able to get the mandatory and validation error message for submitting without name, department
    Given user is on the new POC
    When user clicks on save button without entering the name, department
    Then user will get the mandatory error message for name, department
    When user enters other than text in the name field
    Then user will get the validation error message for name field

  Scenario:  Verify that the user is able to get the mandatory and validation error message for submitting without designation, emailid, contact number
    Given user is on the new POC
    When user clicks on save button without entering the designation, emailid, contact number
    Then user will get the mandatory error message for designation, emailid, contact number
    When user enters other than text in the designation field
    Then user will get the validation error message for designation field
    And user enters other than alphanumeric in the emailid field
    Then user will get the validation error message for emailid field
    And user enters other than number in the contact number
    Then user will get the validation error message for contact number field

  Scenario: Verify that the user is able to get the added address listed in the table
    Given user is on the address adding page
    When user enters all the details
    Then user will get the added address in the address table