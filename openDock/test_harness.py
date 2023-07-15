# Train test Algorithm test harness
# Description:
# - The train_test is a method that is used to evaluate a machine learning algorithm
# Assumptions:
# - Function to split dataset into training and testing datasets
# - Function to evaluate the accuracy of the algorithm's predictions
# Objectives:
# - Consume dataset, and an algorithm
# - Evaluate the accuracy of the algorithm's predictions by returning a performance score

# def train_test(self, dataset, algorithm, split, *args):

from csv import reader
import os

PATH = "c:\\users\\saad0\\onedrive\\Desktop\\process-automation\\launchml\\datasets\\pima-diabetes.csv\\"


# Load a CSV file
def load_csv(filename):
    with open(filename, "r") as f:
        lines = reader(f)
        dataset = list(lines)
    return dataset


# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# Check current working directory.
retval = os.getcwd()

print("Current working directory %s" % retval)

# Now change the directory
os.chdir(PATH)

# Check current working directory.
retval = os.getcwd()

print("Directory changed successfully %s" % retval)

# Read the dataset from csv and store into a list object
csv_dataset = load_csv(retval + "\\" + "pima-indians-diabetes.csv")

# For each row in the dataset, convert each element to a floating point number
for i in range(len(csv_dataset[0])):
    str_column_to_float(csv_dataset, i)

print(csv_dataset)
