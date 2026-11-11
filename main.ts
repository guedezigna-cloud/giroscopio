input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    wuKong.setMotorSpeed(wuKong.MotorList.M1, 50)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Meh)
    wuKong.setMotorSpeed(wuKong.MotorList.M1, -50)
})
