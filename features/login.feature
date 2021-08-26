Feature: Validate Login Feature

    Background:
        Given launch the browser
        When open the perpus website
        Then the website has been opened
        Then click menu login


    Scenario: Login with valid credential
        And input the username "Dikasan123" and password "Dika123"
        And click th login button
        Then login is successfull 
        And close browser

    # Scenario Outline: Login with invalid credential
    #     And input the username "<username>" and password "<password>"
    #     And click th login button
    #     Then login is failed and error message credential is displayed
    #     And close browser
    #     Examples:
    #       | username | password |
    #       | Dikasan123 | Dika1234 |
    #       | Diikasan123| Dika123 |

    Scenario: Login with invalid username
        And input the username "Diikasan123" and password "Dika123"
        And click th login button
        Then login is failed and error message invalid username is displayed
        And close browser

    Scenario: Login with invalid password
        And input the username "Dikasan123" and password "Dika1234"
        And click th login button
        Then login is failed and error message invalid password is displayed
        And close browser


    Scenario: Login with empty username
        And input the password "Dika123"
        And click th login button
        Then login is failed and error message empty username is displayed
        And close browser

        Scenario: Login with empty password
        And input the username "Dikasan123"
        And click th login button
        Then login is failed and error message empty password is displayed
        And close browser


