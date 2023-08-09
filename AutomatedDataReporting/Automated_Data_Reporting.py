import pandas as pd


def generate_data_report(data_file_path, report_file_path):
    df = pd.read_csv(data_file_path)

    summary_statistics = df.describe()
    column_means = df.mean()
    column_max_values = df.max()
    column_min_values = df.min()

    with open(report_file_path, 'w') as report_file:
        report_file.write("Data Report\n")
        report_file.write("Summary Statistics:\n")
        report_file.write(str(summary_statistics) + "\n\n")
        report_file.write("Column Means:\n")
        report_file.write(str(column_means) + "\n\n")
        report_file.write("Column Maximum Values:\n")
        report_file.write(str(column_max_values) + "\n\n")
        report_file.write("Column Minimum Values:\n")
        report_file.write(str(column_min_values))


if __name__ == "__main__":
    data_file_path = "path/to/your/data.csv"
    report_file_path = "path/to/your/report.csv"

    generate_data_report(data_file_path, report_file_path)
    print("Data report generated successfully!")
