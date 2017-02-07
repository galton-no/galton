Feature: Import Twitter statuses
  In order to build a dataset of incidents in Oslo
  As a CLI user
  I need to be able to import Twitter statuses

  Scenario: No tweets in the database
    Given there are "0" Twitter statuses
    When I run "python incidents/import-twitter-statuses.py --screen_name oslopolitiops"
    Then there are "3200" Twitter statuses
