*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  validuser
    Set Password  validpassword123
    Set Password confirmation  validpassword123
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password And Confirmation
    Set Username  matchinguser
    Set Password  matchingpassword123
    Set Password confirmation  matchingpassword123
    Click  button >> text=Register
    Register Should Succeed

Register With Different Password And Confirmation
    Set Username  differentuser
    Set Password  matchingpassword123
    Set Password confirmation  differentpassword123
    Click  button >> text=Register
    Register Should Fail With Message  Password and password confirmation must match

Register With Password Containing Letters And Numbers
    Set Username  validuser3
    Set Password  kalle123
    Set Password confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Letters And Special Characters
    Set Username  validuser4
    Set Password  kalle#abc
    Set Password confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Lowercase Letters Only Password
    Set Username  validuser5
    Set Password  kallekalle
    Set Password confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Uppercase And Lowercase Letters Only Password
    Set Username  validuser6
    Set Password  KalleKalle
    Set Password confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  validpassword123
    Set Password confirmation  validpassword123
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
    Set Password  anotherpassword123
    Set Password confirmation  anotherpassword123
    Click  button >> text=Register
    Register Should Succeed
    Go To Register Page
    Set Username  validuser
    Set Password  anotherpassword456
    Set Password confirmation  anotherpassword456
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
