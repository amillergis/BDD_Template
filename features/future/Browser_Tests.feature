Feature: I Should be able to use the browser to test web apps

As a user
I want to use the browser with behave
Because I need to test web applications

  @wip
  Scenario: Simple headless browser test
     Given that splinter and the phantomJS driver are installed correctly
      when I go to "Google.ca"
      	| url				   |
        | http://www.google.ca |
      then I should be taken to "Google.ca"
      	| title  |
      	| Google |