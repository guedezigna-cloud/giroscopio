def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    wuKong.set_motor_speed(wuKong.MotorList.M1, 50)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.MEH)
    wuKong.set_motor_speed(wuKong.MotorList.M1, -50)
input.on_button_pressed(Button.B, on_button_pressed_b)
