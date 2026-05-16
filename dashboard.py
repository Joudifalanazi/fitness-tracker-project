def start_dashboard():
    while True:
        print("\nFitness Tracker Dashboard")
        print("1. Create User Profile")
        print("2. Add Workout")
        print("3. View Statistics")
        print("4. View Trends")
        print("5. Check Goals")
        print("6. Export Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("User profile feature selected.")
        elif choice == "2":
            print("Add workout feature selected.")
        elif choice == "3":
            print("Statistics feature selected.")
        elif choice == "4":
            print("Trend analysis feature selected.")
        elif choice == "5":
            print("Goal monitor feature selected.")
        elif choice == "6":
            print("Export report feature selected.")
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    start_dashboard()
