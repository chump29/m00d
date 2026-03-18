@crud
Feature: Get mood by date
  Scenario: Get mood by date
    Given that a user wants their mood by date
      When /get_by_date API endpoint is called
      Then mood data is returned
        And the date matches
        And it can be updated
