import matplotlib.pyplot as plt
import numpy as np

sets = ["MNIST digits", "MNIST fashion", "CIFAR10", "CIFAR100 coarse", "CIFAR100 fine"]

ANNfig = plt.figure()
ax = ANNfig.add_axes([0,0,1,1])
ANNaccuracy = [96.87,84.86,10.02,5,1]
ax.bar(sets,ANNaccuracy)
ax.set_ylabel('Accuracy(%)')
ax.set_title('Accuracy of ANN Network')
ax.set_xticks(sets)
ax.set_yticks(np.arange(0,101,10))
plt.show()

# CNNfig = plt.figure()
# ax = CNNfig.add_axes([0,0,1,1])
# ANNaccuracy = [99.2,92.38,77.19,53.16,39.79]
# ax.bar(sets,ANNaccuracy)
# ax.set_ylabel('Accuracy(%)')
# ax.set_title('Accuracy of CNN Network')
# ax.set_xticks(sets)
# ax.set_yticks(np.arange(0,101,10))
# plt.show()