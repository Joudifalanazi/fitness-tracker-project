from workout import create_workout, display_workout

from user_profile import (
    create_user_profile,
    display_user_profile,
    calculate_bmi
)

from data_logger import (
    save_workout_to_csv,
    load_workouts_from_csv,
    save_user_profile
)

from statistics import (
    calculate_pace_distribution,
    calculate_performance_index,
    calculate_weekly_volume_trend
)

from trend_analysis import (
    weekly_summary,
    detect_improvement
)

from goal_monitor import (
    check_weekly_goal,
    calculate_streak
)

from export_manager import export_report


def start_dashboard():

    workouts = []

    while True:

        print("\n===== Fitness Tracker Dashboard =====")

        print("1. Create User Profile")
        print("2. Add Workout")
        print("3. View Statistics")
        print("4. View Trends")
        print("5. Check Goals")
        print("6. Export Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        # CREATE USER PROFILE
        if choice == "1":

            name = input("Enter name: ")

            age = int(input("Enter age: "))

            weight = float(input("Enter weight (kg): "))

            height = float(input("Enter height (cm): "))

            weekly_goal_minutes = int(
                input("Weekly goal minutes: ")
            )

            weekly_goal_calories = int(
                input("Weekly calorie goal: ")
            )

            profile = create_user_profile(
                name,
                age,
                weight,
                height,
                weekly_goal_minutes,
                weekly_goal_calories
            )

            save_user_profile(profile)

            display_user_profile(profile)

            bmi = calculate_bmi(weight, height)

            print(f"BMI: {bmi:.2f}")

        # ADD WORKOUT
        elif choice == "2":

            date = input("Date (YYYY-MM-DD): ")

            exercise_type = input(
                "Exercise type: "
            )

            duration_minutes = float(
                input("Duration (minutes): ")
            )

            distance_km = float(
                input("Distance (km): ")
            )

            calories_burned = float(
                input("Calories burned: ")
            )

            average_heart_rate = float(
                input("Average heart rate: ")
            )

            workout = create_workout(
                date,
                exercise_type,
                duration_minutes,
                distance_km,
                calories_burned,
                average_heart_rate
            )

            workouts.append(workout)

            save_workout_to_csv(workout)

            print("\nWorkout added successfully.")

            display_workout(workout)

        # VIEW STATISTICS
        elif choice == "3":

            loaded_workouts = load_workouts_from_csv()

            if len(loaded_workouts) == 0:
                print("No workouts found.")

            else:

                latest = loaded_workouts[-1]

                pace = calculate_pace_distribution(
                    latest["duration_minutes"],
                    latest["distance_km"]
                )

                performance = (
                    calculate_performance_index(
                        latest["calories_burned"],
                        latest["distance_km"]
                    )
                )

                volume = (
                    calculate_weekly_volume_trend(
                        loaded_workouts
                    )
                )

                print(f"\nPace: {pace} min/km")

                print(
                    f"Performance Index: "
                    f"{performance}"
                )

                print(
                    f"Weekly Volume: "
                    f"{volume} minutes"
                )

        # VIEW TRENDS
        elif choice == "4":

            loaded_workouts = load_workouts_from_csv()

            print(
                weekly_summary(
                    loaded_workouts
                )
            )

            print(
                detect_improvement(
                    loaded_workouts
                )
            )

        # GOAL MONITOR
        elif choice == "5":

            loaded_workouts = load_workouts_from_csv()

            streak = calculate_streak(
                loaded_workouts
            )

            print(
                f"Workout Streak: "
                f"{streak} days"
            )

            goal_result = (
                check_weekly_goal(
                    len(loaded_workouts),
                    4
                )
            )

            print(goal_result)

        # EXPORT REPORT
        elif choice == "6":

            loaded_workouts = load_workouts_from_csv()

            summary = weekly_summary(
                loaded_workouts
            )

            export_report(summary)

        # EXIT
        elif choice == "7":

            print("Exiting program.")

            break

        else:
            print("Invalid choice.")
