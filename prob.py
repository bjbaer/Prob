import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

data = [1, 4, 5, 6, 9, 9, 9] # I was not sure if we were supposed to use this data or the longer set or random data, I tested using all three in place of this and they worked

count = collections.Counter(data)
count_sum = sum(count.values())

for k,v in count.iteritems():
	print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

plt.boxplot(data) #create a box plot of the data
plt.title('Sample boxplot')
plt.savefig("boxplot.png") #save the graph

plt.figure()#resets the graph, without this it overlaid the histogram ontop of the boxplot
plt.hist(data, histtype = 'bar') #create a histogram of the data
plt.title('Sample histogram')
plt.savefig("histogram.png") #save the histogram

plt.figure() #setup the figure
graph1 = stats.probplot(data, dist = "norm", plot=plt) #create the QQ graph, checking it against normal distribution
plt.title('Sample QQ plot')
plt.savefig("QQplot.png") #save the QQ plot
