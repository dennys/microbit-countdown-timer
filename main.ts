input.onButtonPressed(Button.A, function () {
    vTime = vTime + 1
})
input.onButtonPressed(Button.B, function () {
    while (vTime > 0) {
        basic.pause(1000)
        vTime = vTime - 1
        music.playTone(659, music.beat(BeatFraction.Whole))
    }
})
let vTime = 0
vTime = 0
basic.forever(function () {
    basic.showNumber(vTime)
})
