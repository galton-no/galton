Feature: Check system
  In order to verify that the system doesn't have any issues
  As a CLI user
  I need to be able to run a system check

  Scenario: No arguments
    When I run "python manage.py check"
    Then I see "System check identified no issues"
