import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student marks
marks = [65, 72, 80, 55, 90, 68, 75, 82, 60, 78]

# Convert list into NumPy array
marks_array = np.array(marks)

# Statistical calculations
mean = np.mean(marks_array)
median = np.median(marks_array)
minimum = np.min(marks_array)
maximum = np.max(marks_array)
standard_deviation = np.std(marks_array)

# Display results
print("STATISTICAL ANALYSIS OF STUDENT MARKS")
print("--------------------------------------")
print("Marks:", marks)
print("Mean:", mean)
print("Median:", median)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Standard Deviation:", round(standard_deviation, 2))

# Create Pandas DataFrame
df = pd.DataFrame({"Student Marks": marks})

print("\nDESCRIPTIVE STATISTICS")
print("----------------------")
print(df.describe())

# Create histogram
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()