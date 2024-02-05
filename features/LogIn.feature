Feature: OrangeHRM LogIn
  Scenario: LogIn with Valid parameters
    Given i lunch browser
    When i open OrangeHRM LogIn Page
    When Enter username "Admin" and password "admin123"
    When click on LogIn button
    Then User must sucessfull login to the Dashboard Page