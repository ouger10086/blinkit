radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        serial.writeString("0041000")
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
    } else if (receivedNumber == 2) {
        serial.writeString("0042000")
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
    } else if (receivedNumber == 3) {
        serial.writeString("0045000")
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    } else if (receivedNumber == 4) {
        serial.writeString("0046000")
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
    } else if (receivedNumber == 8) {
        serial.writeString("0043000")
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # . .
            . # # # .
            . . # . .
            `)
    } else if (receivedNumber == 5) {
        serial.writeString("0044000")
        basic.showLeds(`
            . . # . .
            . # # # .
            . . # . .
            . . # . .
            . . # . .
            `)
    }
})
radio.setGroup(1)
basic.showNumber(0)
serial.redirect(
SerialPin.P8,
SerialPin.P16,
BaudRate.BaudRate9600
)
