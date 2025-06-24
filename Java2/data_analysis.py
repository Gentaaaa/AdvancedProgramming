import sys
import csv
import statistics
from math import sqrt

def read_csv(file_path):
    """Reads CSV and returns list of dict rows."""
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

def extract_column(data, column):
    """Extract numeric column values as float."""
    try:
        values = [float(row[column]) for row in data]
        return values
    except KeyError:
        print(f"Error: Column '{column}' not found in data.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Non-numeric data found in column '{column}'.")
        sys.exit(1)

def stats(values):
    """Calculate mean, median, mode, std deviation."""
    try:
        mean_val = statistics.mean(values)
        median_val = statistics.median(values)
        mode_val = statistics.mode(values)
        stddev_val = statistics.stdev(values)
        print(f"Mean: {mean_val:.3f}")
        print(f"Median: {median_val:.3f}")
        print(f"Mode: {mode_val}")
        print(f"Standard Deviation: {stddev_val:.3f}")
    except statistics.StatisticsError as e:
        print(f"Statistics error: {e}")

def histogram(values, bins=10):
    """Print simple text histogram."""
    min_val, max_val = min(values), max(values)
    bin_size = (max_val - min_val) / bins
    bins_count = [0]*bins

    for v in values:
        index = int((v - min_val) / bin_size)
        if index == bins:  # edge case max value
            index -= 1
        bins_count[index] += 1

    for i, count in enumerate(bins_count):
        start = min_val + i*bin_size
        end = start + bin_size
        bar = "*" * count
        print(f"{start:.2f} - {end:.2f} | {bar}")

def correlation(data, col1, col2):
    """Calculate Pearson correlation coefficient."""
    x = extract_column(data, col1)
    y = extract_column(data, col2)
    if len(x) != len(y):
        print("Error: Columns have different lengths.")
        sys.exit(1)
    n = len(x)
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)
    numerator = sum((x[i] - mean_x)*(y[i] - mean_y) for i in range(n))
    denominator = sqrt(sum((x[i] - mean_x)**2 for i in range(n)) * sum((y[i] - mean_y)**2 for i in range(n)))
    if denominator == 0:
        print("Error: Standard deviation zero, correlation undefined.")
        sys.exit(1)
    corr = numerator / denominator
    print(f"Correlation between '{col1}' and '{col2}': {corr:.3f}")

def detect_outliers(values, threshold=2.0):
    """Detect outliers using z-score method."""
    mean_val = statistics.mean(values)
    stddev_val = statistics.stdev(values)
    outliers = []
    for i, v in enumerate(values):
        z_score = abs((v - mean_val) / stddev_val)
        if z_score > threshold:
            outliers.append((i, v))
    if outliers:
        print(f"Outliers (threshold z-score={threshold}):")
        for idx, val in outliers:
            print(f"Index {idx}: {val}")
    else:
        print(f"No outliers detected with threshold z-score={threshold}.")

def print_usage():
    print("Usage examples:")
    print(" python data_analysis.py sample_data.csv stats temperature")
    print(" python data_analysis.py sample_data.csv histogram humidity 10")
    print(" python data_analysis.py sample_data.csv correlation temperature humidity")
    print(" python data_analysis.py sample_data.csv outliers wind_speed 2.0")

def main():
    if len(sys.argv) < 4:
        print("Error: Not enough arguments.")
        print_usage()
        sys.exit(1)

    file_path = sys.argv[1]
    command = sys.argv[2].lower()
    data = read_csv(file_path)

    if command == "stats":
        column = sys.argv[3]
        values = extract_column(data, column)
        stats(values)

    elif command == "histogram":
        if len(sys.argv) < 5:
            print("Error: Histogram requires a bin count.")
            print_usage()
            sys.exit(1)
        column = sys.argv[3]
        try:
            bins = int(sys.argv[4])
        except ValueError:
            print("Error: Bin count must be an integer.")
            sys.exit(1)
        values = extract_column(data, column)
        histogram(values, bins)

    elif command == "correlation":
        if len(sys.argv) < 5:
            print("Error: Correlation requires two columns.")
            print_usage()
            sys.exit(1)
        col1 = sys.argv[3]
        col2 = sys.argv[4]
        correlation(data, col1, col2)

    elif command == "outliers":
        if len(sys.argv) < 5:
            print("Error: Outliers command requires a threshold.")
            print_usage()
            sys.exit(1)
        column = sys.argv[3]
        try:
            threshold = float(sys.argv[4])
        except ValueError:
            print("Error: Threshold must be a float.")
            sys.exit(1)
        values = extract_column(data, column)
        detect_outliers(values, threshold)

    else:
        print(f"Error: Unknown command '{command}'.")
        print_usage()
        sys.exit(1)

if __name__ == "__main__":
    main()
