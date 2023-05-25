// mudança de status do anel de LED e direção dos motores de passo
input.onSound(DetectedSound.Loud, function () {
    if (ligado == 0) {
        fator = 1
        ligado = 1
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        strip.show()
    } else {
        fator = -1
        ligado = 0
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
        strip.clear()
    }
})
let volta = 0
let fator = 0
let ligado = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P1, 12, NeoPixelMode.RGB)
strip.setBrightness(255)
strip.showColor(neopixel.colors(NeoPixelColors.Purple))
strip.show()
ligado = 0
fator = -1
// Controle do servo
basic.forever(function () {
    for (let índice = 0; índice <= 180; índice++) {
        hackbitmotors.Servo(hackbitmotors.Servos.S8, índice)
        basic.pause(100)
    }
    basic.pause(1000)
    volta = 180
    while (volta >= 0) {
        hackbitmotors.Servo(hackbitmotors.Servos.S8, volta)
        basic.pause(100)
        volta += 0 - 1
    }
    basic.pause(randint(1, 5) * 1000)
})
// controle dos motores de passo
basic.forever(function () {
    hackbitmotors.StepperDual(randint(200, 360) * fator, randint(200, 360) * fator)
})
