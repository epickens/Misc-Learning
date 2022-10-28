import seaborn as sns
import matplotlib.pyplot as plt

from statsmodels.stats.proportion import proportions_ztest, proportion_confint
from statsmodels.stats.weightstats import zconfint


# groups
counts = [100, 15]
nobs = [1000, 100]

stat, pval = proportions_ztest(counts, nobs, alternative="larger")
print("The p-value of the hypothesis is true (both are equal) is: {}".format(pval))
print(
    "The p-value of the  hypothesis is false (group 1 has a greater proportion) is: {}".format(
        1 - pval
    )
)

confints = proportion_confint(counts, nobs)
print("The confidence intervals for each group's proportion are: {}".format(confints))

sns.set_style("white")
plt.vlines([confints[0][0], confints[1][0]], ymin=0, ymax=1, color="orange", ls="--")
plt.vlines(0.1, ymin=0, ymax=1, color="black")
plt.vlines([confints[0][1], confints[1][1]], ymin=0, ymax=1, color="black", ls="--")
plt.vlines(0.15, ymin=0, ymax=1, color="orange", lw=4)
plt.axvspan(confints[0][0], confints[1][1], color="grey", alpha=0.25, hatch=".")
plt.title("Means and Confidence Intervals")
plt.show()
