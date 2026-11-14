*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  validuser
    Set Password  validpassword
    Set Password confirmation  validpassword
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  validpassword
    Set Password confirmation  validpassword
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  validuser2
    Set Password  short
    Set Password confirmation  short
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Username That Is Already In Use
    Set Username  validuser
    Set Password  anotherpassword
    Set Password confirmation  anotherpassword
    Click  button >> text=Register
    Register Should Succeed
    Go To Register Page
    Set Username  validuser
    Set Password  anotherpassword2
    Set Password confirmation  anotherpassword2
    Click  button >> text=Register
    Register Should Fail With Message  User with username validuser already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Fill Text  id=password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

#Käyttäjätunnus ja salasana noudattavat seuraavia sääntöjä:

#Käyttäjätunnuksen on oltava vähintään 3 merkin pituinen merkkijono, joka ei ole vielä käytössä
#Salasanan on oltava pituudeltaan vähintään 8 merkkiä
