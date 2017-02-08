Feature: Import Twitter statuses
  In order to build a dataset of incidents in Oslo
  As a CLI user
  I need to be able to import Twitter statuses

  Scenario: No tweets in the database
    Given there are "0" Twitter statuses
    When I run "python manage.py import-twitter-statuses oslopolitiops"
    Then I see "Importing Twitter statuses"
    And there are "20" Twitter statuses
