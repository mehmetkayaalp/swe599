import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from tomato.audio.audioanalyzer import AudioAnalyzer

audioAnalyzer = AudioAnalyzer(verbose=True)

audio_filename = "sample_music.mp3"
audio_features = audioAnalyzer.analyze(audio_filename)

audioAnalyzer.plot(audio_features)
matplotlib.pyplot.show()
