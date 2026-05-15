def create_workout(date, exercise_type, duration_minutes, distance_km, calories_burned, average_heart_rate):
    """
    Creates a workout record using a dictionary.
    """
    workout = {
        "date": date,
        "exercise_type": exercise_type,
        "duration_minutes": duration_minutes,
        "distance_km": distance_km,
        "calories_burned": calories_burned,
        "average_heart_rate": average_heart_rate
    }
    return workout


def display_workout(workout):
    """
    Displays workout details in a readable format.
    """
    print("-----------------------------")
    print(f"Date: {workout['date']}")
    print(f"Exercise Type: {workout['exercise_type']}")
    print(f"Duration: {workout['duration_minutes']} minutes")
    print(f"Distance: {workout['distance_km']} km")
    print(f"Calories Burned: {workout['calories_burned']}")
    print(f"Average Heart Rate: {workout['average_heart_rate']} bpm")
    print("-----------------------------")
