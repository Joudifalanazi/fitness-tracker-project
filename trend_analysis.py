from datetime import datetime, timedelta
def average_calories(workouts):
    """
    Calculates average calories burned per workout.
    """
    if len(workouts) == 0:
        return 0

    total = 0

    for workout in workouts:
        total += float(workout["calories_burned"])

    return total / len(workouts)


def detect_improvement(workouts):
    """
    Detects improvement in distance performance.
    """

    if len(workouts) < 2:
        return "Not enough data"

    first_distance = float(
        workouts[0]["distance_km"]
    )

    last_distance = float(
        workouts[-1]["distance_km"]
    )

    if first_distance == 0:
        return "Invalid starting distance"

    improvement = (
        (last_distance - first_distance)
        / first_distance
    ) * 100

    return f"You improved by {improvement:.2f}%"
def workouts_this_week(workouts):
    """
    Counts workouts completed in the last 7 days.
    """

    today = datetime.today()

    week_ago = today - timedelta(days=7)

    count = 0

    for workout in workouts:

        workout_date = datetime.strptime(
            workout["date"],
            "%Y-%m-%d"
        )

        if workout_date >= week_ago:
            count += 1

    return count


def weekly_summary(workouts):
    """
    Generates a weekly workout summary.
    """

    total_calories = 0
    total_distance = 0

    for workout in workouts:

        total_calories += float(
            workout["calories_burned"]
        )

        total_distance += float(
            workout["distance_km"]
        )

    summary = (
        f"Weekly Summary:\n"
        f"Workouts: {len(workouts)}\n"
        f"Calories Burned: {total_calories}\n"
        f"Distance Covered: {total_distance} km"
    )

    return summary


if __name__ == "__main__":

    workouts = [

        {
            "date": "2026-05-10",
            "exercise_type": "Running",
            "duration_minutes": 30,
            "distance_km": 3,
            "calories_burned": 200,
            "average_heart_rate": 140
        },

        {
            "date": "2026-05-14",
            "exercise_type": "Running",
            "duration_minutes": 40,
            "distance_km": 5,
            "calories_burned": 350,
            "average_heart_rate": 150
        }
    ]

    print(average_calories(workouts))

    print(detect_improvement(workouts))

    print(workouts_this_week(workouts))

    print(weekly_summary(workouts))