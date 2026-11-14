*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Starting Page

*** Test Cases ***
Click Login Link
    Click  text=Login
    Login Page Should Be Open

Click Register Link
    Click  text=Register new user
    Register Page Should Be Open

*** Keywords ***

Reset Application And Go To Starting Page
  Reset Application
  Go To Starting Page

Go To Starting Page
    Go To  ${HOME_URL}

Login Page Should Be Open
    Get Title  ==  Login

Main Page Should Be Open
    Get Title  ==  Ohtu Application main page

Register Page Should Be Open
    Get Title  ==  Register