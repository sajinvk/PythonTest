# coding: utf-8
from matplotlib import pyplot as plt
movies = [ "A" ,"V", "Titanic" ,"WOWS" ]
oscars = [ 3 , 8 , 12, 4 ]
xs = [ i for i, values in enumerate(movies)]
plt.bar(xs, oscars)
plt.show()
plt.bar(xs, oscars)
plt.show()
xs = [ i for i, _ in enumerate(movies)]
plt.bar(xs, oscars)
plt.show()
plt.xticks([i for i, values in enumerate(movies)], movies)
plt.bar(xs, oscars)
plt.xticks([i for i, values in enumerate(movies)], movies)
plt.show()
