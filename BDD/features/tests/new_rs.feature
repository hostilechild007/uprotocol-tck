Feature: Test Manager and Test Agent messaging to each other directly or with SocketUTransport and Dispatcher
Scenario Outline: Testing Test Manager's registerlistener() and then send()
    #New Given: set data first for (UUri, UPayload, UAttributes)
    # should have separate scenarios checking status for registerlistener() and send()

    # Note: each step should be DESCRIPTIVE as POSSIBLE!
    Given protobuf UEntity "entity" sets parameter "name" equal to string "body.access"  
        And protobuf UResource "resource" sets parameter "name" equal to string "door" 
        And protobuf UResource "resource" sets parameter "instance" equal to string "front_left" 
        And protobuf UResource "resource" sets parameter "message" equal to string "Door" 

        And protobuf UUri "uuri" sets parameter "entity" equal to created protobuf "entity" UEntity
        And protobuf UUri "uuri" sets parameter "resource" equal to created protobuf "resource" UResource




    Examples: 
    | uE1     |
    | python  |