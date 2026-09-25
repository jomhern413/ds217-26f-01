measurements = [18, 21, 24, 19]
review_threshold_text = "20"

# Replace this scaffold output with your calculation, loop, decision, and summary.

# Converting review_threshold_text to integer:
review_threshold = int(review_threshold_text)
# Checking to make sure that the conversion worked properly:
# print("The review threshold is", review_threshold, "The class type of this variable is", type(review_threshold))

# Making variables total and review_count as integers:
total = 0
review_count = 0
# Checking to make sure that these variables are formatted correctly:
# print("The variable type for total and review_count are:", type(total), type(review_count))

# For loop to label the data:
for measurement in measurements:
    total = total + measurement
    if measurement >= review_threshold:
        print("Measurement:", measurement, "review")
        review_count = review_count + 1
    else:
        print("Measurement:", measurement, "within range")

print("Count:", len(measurements))
print("Total:", total)
print("Mean:", total/len(measurements))
print("Review count:", review_count)
    