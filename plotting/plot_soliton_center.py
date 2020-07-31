"""
===========
Center in the soliton
===========

Shows how to use latex in a plot.

Also refer to the :doc:`/tutorials/text/usetex` guide.
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)

# interface tracking profiles
N = 500
delta = 0.6
X = np.linspace(-1, 1, N)
Y = np.ones(N)
y = np.zeros(N)
plt.plot(X, Y, 'r-.',
         X, y, 'r-.',
         X, (1 + np.tanh(4 * X / delta)) / 2, )  # phase field tanh profiles
# X, X > 0, 'k--')                        # sharp interface
# Draw a vertical line expanded
plt.axvspan(-0.2, 0.2, facecolor='#2ca02c', alpha=0.3)

# legend
# plt.legend(('phase field', 'level set', 'sharp interface'),
# shadow=True, loc=(0.01, 0.48), handlelength=1.5, fontsize=16)

# the arrow
plt.annotate("", xy=(-1, 0.5), xytext=(1, 0.5),
             arrowprops=dict(arrowstyle="<->", connectionstyle="arc3"))
plt.text(0, 0.5, r'$\delta$',
         {'color': 'black', 'fontsize': 18, 'ha': 'center', 'va': 'center',
          'bbox': dict(boxstyle="circle", fc="white", ec="black", pad=0.2)})
plt.text(0.45, 0.93, r'$u[i+1]$',
         {'color': 'black', 'fontsize': 14, 'ha': 'center', 'va': 'center',
          'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)})
plt.annotate("", xy=(0.3, 0.93), xytext=(0.18, 0.93),
             arrowprops=dict(arrowstyle="<-", connectionstyle="arc3"))
plt.text(-0.35, 0.07, r'$u[i]$',
         {'color': 'black', 'fontsize': 14, 'ha': 'center', 'va': 'center',
          'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)})
plt.annotate("", xy=(-0.28, 0.07), xytext=(-0.18, 0.07),
             arrowprops=dict(arrowstyle="<-", connectionstyle="arc3"))

# Use tex in labels
plt.xticks((-1, 0, 1), ('$0$', r'$50$', '$100$'), color='k', size=20)

# Left Y-axis labels, combine math mode and text mode
plt.xlabel(r'$x$', {'fontsize': 20})
plt.ylabel(r'$\phi(x)$', {'color': 'C0', 'fontsize': 20})
plt.yticks((0, 0.5, 1), (r'\bf{$-\pi$}', r'\bf{$0$}', r'\bf{$\pi$}'), color='k', size=20)

# Right Y-axis labels
# plt.text(1.02, 0.5, r"\bf{level set} $\phi$", {'color': 'C2', 'fontsize': 20},
# horizontalalignment='left',
# verticalalignment='center',
# rotation=90,
# clip_on=False,
# transform=plt.gca().transAxes)

# Use multiline environment inside a `text`.
# level set equations
eq1 = r'Which is the slope of the line?'

plt.text(0.2, 0.6, eq1, {'color': 'C2', 'fontsize': 12})

# phase field equations
# eq2 = r'\begin{eqnarray*}' + \
# r'\mathcal{F} &=& \int f\left( \phi, c \right) dV, \\ ' + \
# r'\frac{ \partial \phi } { \partial t } &=& -M_{ \phi } ' + \
# r'\frac{ \delta \mathcal{F} } { \delta \phi }' + \
# r'\end{eqnarray*}'
# plt.text(0.18, 0.18, eq2, {'color': 'C0', 'fontsize': 16})

plt.show()
