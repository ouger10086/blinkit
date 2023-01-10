def on_received_number(receivedNumber):
    if receivedNumber == 1:
        serial.write_string("0041000")
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
    elif receivedNumber == 2:
        serial.write_string("0042000")
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
    elif receivedNumber == 3:
        serial.write_string("0045000")
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
    elif receivedNumber == 4:
        serial.write_string("0046000")
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
    elif receivedNumber == 8:
        serial.write_string("0043000")
        basic.show_leds("""
            . . # . .
                        . . # . .
                        . . # . .
                        . # # # .
                        . . # . .
        """)
    elif receivedNumber == 5:
        serial.write_string("0044000")
        basic.show_leds("""
            . . # . .
                        . # # # .
                        . . # . .
                        . . # . .
                        . . # . .
        """)
radio.on_received_number(on_received_number)

radio.set_group(1)
basic.show_number(0)
serial.redirect(SerialPin.P8, SerialPin.P16, BaudRate.BAUD_RATE9600)