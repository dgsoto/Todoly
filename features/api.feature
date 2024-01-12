Feature: API Testing with Todoly

  Scenario: Verify successful API request
    Given I make a GET request to "/todos/1"
    Then the response status code should be 200
    And the response should contain "title" with value "delectus aut autem"
