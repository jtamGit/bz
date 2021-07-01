music.set_volume(255)
music.start_melody(music.built_in_melody(Melodies.RINGTONE),
    MelodyOptions.FOREVER)

def on_forever():
    pass
basic.forever(on_forever)
