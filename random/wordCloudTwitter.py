from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = '''Early years
'''

our_mask = np.array(Image.open(r'C:\Users\pc\Desktop\twitter_mask.png'))

cloud = WordCloud(background_color="white", mask = our_mask).generate(text)

plt.imshow(cloud)
plt.axis('off')
plt.show()