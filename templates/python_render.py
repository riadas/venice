import os
import matplotlib.pyplot as plt

dir_ = '../static/frames2/'

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

images = []
plt.axis('off')
img = None

for f in sorted(os.listdir(dir_)[:25]):
   print("wow")
   print(f)
   im = plt.imread(dir_ + f)
   images.append(im)

for im in images:
   print("wow2")
   if img is None:
      img = plt.imshow(im)
      plt.pause(0.1)
   else:
      img.set_data(im)
      plt.pause(0.05)
   plt.draw()
