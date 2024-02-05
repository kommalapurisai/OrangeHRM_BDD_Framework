Feature: LogIn DataDrivenTest
  Scenario Outline: LogIn to the OrangeHRM with multiple parameters
    Given I Lunch My Browser
    When I Open OrangeHRMLogIn Page
    When I Entered username "<username>" and "<password>"
    When I Click on LogIn button
    Then Verify Profile is present or not
    Examples:
      | username | password |
      | Admin    | admin123 |
      | Admin    | Admin123 |
      | admin    | admin123 |
      | Admin    | 123456   |
      | Admin    | admin123 |
