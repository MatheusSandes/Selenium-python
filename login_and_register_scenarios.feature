Feature: Login and register
@a
Scenario: Register a user
    Given user at register page
    When fill the register form
    Then the user must be registered

Scenario: Register user with invalid fields
    Given user at register page
    When fill the register form with invalid fields
    Then the system must show an invalid field error

Scenario: Register user missing fields
    Given user at register page
    When fill the register form with missing fields
    Then the system must show an error

Scenario: Login as admin user
    Given user at login page
    When fill the login form as admin user
    Then user should be logged in as admin

Scenario: Login as normal user
    Given normal user at login page
    When fill the login form as normal user
    Then user should be logged in as normal user

Scenario: Wrong password as admin user 
    Given user at login page
    When fill the login formas normal user with wrong password
    Then user should be logged in as admin

Scenario: Wrong as normal user
    Given normal user at login page
    When fill the login form as normal user with wrong password
    Then user should be logged in as normal user