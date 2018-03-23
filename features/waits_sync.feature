Feature: Demonstrate Waits

 Scenario: Implicit Wait timeout
 When I open seleniumframework wait website
 And I set implicit timeout
 Then I print the text for periodic element

 Scenario: Script timeout
 When I open seleniumframework website
 And I set script timeout

 Scenario: Explicit Wait block using presence of element located
 When I open seleniumframework website
 Then I wait for presence of element using id

 Scenario: Explicit Wait block using text to be present in element
 When I open seleniumframework website
 Then I wait for text to be present in element

 Scenario: Explicit Wait block to wait for text in value attribute of element
 When I open seleniumframework website
 Then I wait for value attribute in element

 Scenario: Explicit Wait block to wait for alert
 When I open seleniumframework website
 Then I wait for alert

 Scenario: Expected Conditions staleness of element
 When I open seleniumframework website
 Then I check for staleness of element