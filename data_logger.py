import csv
import json
import os


def save_workout_to_csv(workout, filename="workouts.csv"):
    """
    Saves a workout record to a CSV file.
    """
    file_exists = os.path.isfile(filename)

    try:
        with open(filename, mode="a", newline="") as file:
            fieldnames = [
                "date",
                "exercise_type",
                "duration_minutes",
                "distance_km",
                "calories_burned",
                "average_heart_rate"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(workout)

    except Exception as error:
        print("Error saving workout:", error)


def load_workouts_from_csv(filename="workouts.csv"):
    """
    Loads workout records from a CSV file.
    """
    workouts = []

    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                workouts.append(row)

    except FileNotFoundError:
        print("No workout file found yet.")
    except Exception as error:
        print("Error loading workouts:", error)

    return workouts


def save_user_profile(profile, filename="user_profile.json"):
    """
    Saves the user profile to a JSON file.
    """
    try:
        with open(filename, mode="w") as file:
            json.dump(profile, file, indent=4)

    except Exception as error:
        print("Error saving user profile:", error)


def load_user_profile(filename="user_profile.json"):
    """
    Loads the user profile from a JSON file.
    """
    try:
        with open(filename, mode="r") as file:
            profile = json.load(file)
            return profile

    except FileNotFoundError:
        print("No user profile found yet.")
        return None
    except Exception as error:
        print("Error loading user profile:", error)
        return None
