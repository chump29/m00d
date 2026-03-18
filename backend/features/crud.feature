@crud
Feature: Get mood data

  Scenario: Get mood by date
    Given that a user wants a mood by date
      When /get_by_date API endpoint is called
      Then mood data is returned
        And the date matches
        And it can be updated

  Scenario: Get all moods
    Given that a user wants all moods
      When /get API endpoint is called
      Then all mood data is returned
        And there is at least one row
