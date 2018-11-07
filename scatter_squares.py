import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [1,4,9,16,25]
x = list(range(1,1001))
y = [x_value**2 for x_value in x]

# plt.scatter(x,y,c='red',edgecolors='none',s=10)
# plt.scatter(x,y,c=(0.5,0,0),edgecolors='none',s=10)
# colormap
plt.scatter(x,y,c=y,cmap=plt.cm.Blues,edgecolors='none',s=10)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of label",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)  # which indicates the main scale
plt.axis([0,1100,0,1100000])
# plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')  #automatically save the image to current directory and clip the white region