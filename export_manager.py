def export_report(data, filename="report.txt"):

    with open(filename, "w") as file:
        file.write("Fitness Tracker Report\n")
        file.write(str(data))

    print("Report exported successfully.")
