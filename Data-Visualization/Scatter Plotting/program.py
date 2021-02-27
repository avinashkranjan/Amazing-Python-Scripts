# importing matplotlib module
from matplotlib import pyplot as plt

plt.plot([1, 2, 3, 4],
         [1, 4, 9, 16], 'ro')

# ro to make red circles
plt.axis([0, 6, 0, 20])   
plt.show()      
