Feature: Cases where cut drops is placed in the evino website shopping cart page
@a
Scenario: Cart with one unit of the same wine
    Given one cart with "1" wines
    When user checks the cart
    Then must have "1" evino cut drops in the cart at no additional cost
    And the number on the cart logo must have be "1"
@b
Scenario: Cart with more than one unit of the same wine
    Given one cart with "5" wines
    When user checks the cart
    Then must have "5" evino cut drops in the cart at no additional cost
    And the number on the cart logo must have be "5"
@c
Scenario: Cart with different wines
    Given one cart with "5" wines
    When and with "3" wines of another type
    And user checks the cart
    Then must have "8" evino cut drops in the cart at no additional cost
    And the number on the cart logo must have be "8"