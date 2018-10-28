import matplotlib
matplotlib.use('Agg')
import essentia
import essentia.standard
import essentia.streaming

loader = essentia.standard.MonoLoader(filename='sample_music.mp3')
audio = loader()
from pylab import plot, show, figure, imshow
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (15, 6)

plot(audio[1*44100:2*44100])
plt.title("This is how the 2nd second of this audio looks like:")
plt.savefig('analyzer10.png')


