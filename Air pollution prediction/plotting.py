import numpy as np
from matplotlib import pyplot as plt 


fig,ax = plt.subplots(figsize=(12,8))

plot_start = 225
# plot the training data 
ax.plot(y_train.index[plot_start:],y_train.values[plot_start:],'navy',marker='o',label='observed')
# plot the test data
ax.plot(y_test.index,y_test.values,'navy',marker='o')
ax.plot(y_test.index,pred,'darkgreen',marker='o',label='pred')

sigma = np.sqrt(std)
ax.fill(np.concatenate([y_test.index,y_test.index[::-1]]),
        np.concatenate([pred-1.960*sigma,(pred+1.9600*sigma)[::-1]]),
        alpha=.5,fc='silver',ec='tomato',label='95% confidence interval')

ax.legend(loc='upper left',prop={'size':16})