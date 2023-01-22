Feature: Check logo

  Scenario: Logo presence on website
    Given launch chrome browser
    When open homepage
    Then verify that the logo present on the page
    And close browser