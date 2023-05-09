# Windows version
def play_song(notations):
    import winsound

    frequencies = {
        'C3' : 130.81,    # 1
        'C#3': 138.59,    # 1#
        'D3' : 146.83,    # 2
        'D#3': 155.56,    # 2#
        'E3' : 164.81,    # 3
        'F3' : 174.61,    # 4
        'F#3': 185.00,    # 4#
        'G3' : 196.00,    # 5
        'G#3': 207.65,    # 5#
        'A3' : 220.00,    # 6
        'A#3': 233.08,    # 6#
        'B3' : 246.94,    # 7
        'C4' : 261.63,    # 1
        'C#4': 277.18,    # 1#
        'D4' : 293.66,    # 2
        'D#4': 311.13,    # 2#  
        'E4' : 329.63,    # 3
        'F4' : 349.23,    # 4
        'F#4': 369.99,    # 4#    
        'G4' : 391.99,    # 5
        'G#4': 415.30,    # 5#
        'A4' : 440.00,    # 6
        'A#4': 466.16,    # 6#
        'B4' : 493.88,    # 7
        'C5' : 523.25,    # 1
        'C#5': 554.37,    # 1#
        'D5' : 587.33,    # 2
        'D#5': 622.25,    # 2#  
        'E5' : 659.26,    # 3
        'F5' : 698.46,    # 4
        'F#5': 739.99,    # 4#    
        'G5' : 783.99,    # 5
        'G#5': 830.61,    # 5#
        'A5' : 880.00,    # 6
        'A#5': 932.33,    # 6#
        'B5' : 987.77,    # 7
    }

    # durations = {'H': 300, 'M': 600, 'D': 1200, 'T': 1800, 'Q': 2400}
    durations = {'H': 250, 'M': 500, 'D': 1000, 'T': 1500, 'Q': 2000}

    for notation in notations:
        note = notation.split()
        frequency = round(frequencies.get(note[0]))
        duration = durations.get(note[1])
        winsound.Beep(frequency, duration)
        

notations = ('G4 H', 'G4 H', 'A4 M', 'G4 M', 'C5 M', 'B4 D', 'G4 H', 'G4 H', 
             'A4 M', 'G4 M', 'D5 M', 'C5 D', 'G4 H', 'G4 H', 'G5 M', 'E5 M', 
             'C5 M', 'B4 M', 'A4 M', 'F5 H', 'F5 H', 'E5 M', 'C5 M', 'D5 M', 'C5 T')
play_song(notations)