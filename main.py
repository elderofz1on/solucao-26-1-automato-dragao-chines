def on_sound_loud():
    global frente, ligado
    if ligado == 0:
        frente = 0
        ligado = 1
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        strip.show()
    else:
        frente = 1
        ligado = 0
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
        strip.clear()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

volta = 0
frente = 0
ligado = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P1, 12, NeoPixelMode.RGB)
strip.set_brightness(255)
strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
strip.show()
ligado = 0
frente = 0
fator = 1

def on_forever():
    global fator, volta
    if frente == 0:
        fator = 1
    elif frente == 1:
        fator = -1
    for índice in range(181):
        hackbitmotors.servo(hackbitmotors.Servos.S8, índice)
        basic.pause(100)
    basic.pause(1000)
    volta = 180
    while volta >= 0:
        hackbitmotors.servo(hackbitmotors.Servos.S8, volta)
        basic.pause(100)
        volta += 0 - 1
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    hackbitmotors.stepper_degree(hackbitmotors.Steppers.M1, 360 * 1 * fator)
    basic.pause(100)
basic.forever(on_forever2)

def on_forever3():
    hackbitmotors.stepper_degree(hackbitmotors.Steppers.M2, 360 * 1 * fator)
    basic.pause(100)
basic.forever(on_forever3)
