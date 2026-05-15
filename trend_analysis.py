from datetime import datetime, timedelta
def average_calories(workouts):
    """
    Calculates average calories burned.
    """

    if len(workouts) == 0:
        return 0

    total = 0

    for workout in workouts:
        total += workout["calories"]

    return total / len(workouts)

def detect_improvement(workouts):
    """
    Detects improvement in distance performance.
    """

    if len(workouts) < 2:
        return "Not enough data"

    first_distance = workouts[0]["distance"]
    last_distance = workouts[-1]["distance"]

    improvement = ((last_distance - first_distance) / first_distance) * 100

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
        total_calories += workout["calories"]
        total_distance += workout["distance"]

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
            "distance": 3,
            "calories": 200
        },

        {
            "date": "2026-05-14",
            "distance": 5,
            "calories": 350
        }
    ]

    print(average_calories(workouts))

    print(detect_improvement(workouts))

    print(workouts_this_week(workouts))

    print(weekly_summary(workouts))