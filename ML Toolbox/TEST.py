import scipy.stats as stats
import numpy as np

# Generate a sample of data (replace this with your own dataset)
np.random.seed(42)  # for reproducibility
sample_data = np.random.normal(loc=50, scale=10, size=30)  # mean=50, standard deviation=10, size=30

# Calculate the mean and standard error of the sample
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1)  # ddof=1 for sample standard deviation

# Set the confidence level (e.g., 95% confidence interval)
confidence_level = 0.95

# Calculate the confidence interval using t-distribution
lower_bound, upper_bound = stats.t.interval(confidence_level, df=len(sample_data)-1, loc=sample_mean, scale=sample_std/np.sqrt(len(sample_data)))

# Print the results
print(f"Sample Mean: {sample_mean}")
print(f"Confidence Interval ({confidence_level*100}%): ({lower_bound}, {upper_bound})")