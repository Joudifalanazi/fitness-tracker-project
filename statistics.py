
def calculate_pace_distribution(duration_minutes, distance_km):
    """
    Calculates pace in minutes per kilometer.
    """

    try:

        duration_minutes = float(duration_minutes)
        distance_km = float(distance_km)

        if distance_km == 0:
            return 0

        pace = duration_minutes / distance_km

        return round(pace, 2)

    except Exception as error:
        print("Error calculating pace:", error)
        return 0


def calculate_heart_rate_zones(average_heart_rate):
    """
    Classifies heart rate zone.
    """

    try:

        average_heart_rate = float(average_heart_rate)

        if average_heart_rate < 120:
            return "Light"

        elif average_heart_rate <= 150:
            return "Moderate"

        else:
            return "Intense"

    except Exception as error:
        print("Error calculating heart rate zone:", error)
        return "Unknown"


def calculate_training_stress_score(
    duration_minutes,
    average_heart_rate
):
    """
    Estimates workout stress score.
    """

    try:

        duration_minutes = float(duration_minutes)
        average_heart_rate = float(average_heart_rate)

        score = (
            duration_minutes *
            average_heart_rate
        ) / 100

        return round(score, 2)

    except Exception as error:
        print("Error calculating stress score:", error)
        return 0


def calculate_performance_index(
    calories_burned,
    distance_km
):
    """
    Calculates performance score.
    """

    try:

        calories_burned = float(calories_burned)
        distance_km = float(distance_km)

        score = (
            calories_burned +
            (distance_km * 10)
        )

        return round(score, 2)

    except Exception as error:
        print("Error calculating performance:", error)
        return 0


def calculate_consistency_score(workouts_per_week):
    """
    Calculates consistency score out of 100.
    """

    try:

        workouts_per_week = int(workouts_per_week)

        score = workouts_per_week * 20

        if score > 100:
            score = 100

        return score

    except Exception as error:
        print("Error calculating consistency:", error)
        return 0


def calculate_recovery_index(
    sleep_hours,
    stress_level
):
    """
    Estimates recovery quality.
    """

    try:

        sleep_hours = float(sleep_hours)
        stress_level = float(stress_level)

        recovery = (
            sleep_hours * 10
        ) - stress_level

        return round(recovery, 2)

    except Exception as error:
        print("Error calculating recovery:", error)
        return 0


def calculate_vo2_max_estimate(
    max_heart_rate,
    resting_heart_rate
):
    """
    Estimates VO2 max.
    """

    try:

        max_heart_rate = float(max_heart_rate)
        resting_heart_rate = float(resting_heart_rate)

        if resting_heart_rate == 0:
            return 0

        vo2 = (
            15 *
            (max_heart_rate / resting_heart_rate)
        )

        return round(vo2, 2)

    except Exception as error:
        print("Error calculating VO2 max:", error)
        return 0


def calculate_weekly_volume_trend(workouts):
    """
    Calculates total weekly workout duration.
    """

    try:

        total_duration = 0

        for workout in workouts:

            total_duration += float(
                workout["duration_minutes"]
            )

        return round(total_duration, 2)

    except Exception as error:
        print("Error calculating weekly volume:", error)
        return 0


#test only won't effect anything
if __name__ == "__main__":

    sample_workout = {

        "date": "2026-05-15",
        "exercise_type": "Running",
        "duration_minutes": 30,
        "distance_km": 5,
        "calories_burned": 300,
        "average_heart_rate": 145
    }

    print(
        "Pace:",
        calculate_pace_distribution(
            sample_workout["duration_minutes"],
            sample_workout["distance_km"]
        ),
        "min/km"
    )

    print(
        "Heart Rate Zone:",
        calculate_heart_rate_zones(
            sample_workout["average_heart_rate"]
        )
    )

    print(
        "Training Stress Score:",
        calculate_training_stress_score(
            sample_workout["duration_minutes"],
            sample_workout["average_heart_rate"]
        )
    )

    print(
        "Performance Index:",
        calculate_performance_index(
            sample_workout["calories_burned"],
            sample_workout["distance_km"]
        )
    )

    print(
        "Consistency Score:",
        calculate_consistency_score(4)
    )

    print(
        "Recovery Index:",
        calculate_recovery_index(8, 20)
    )

    print(
        "VO2 Max Estimate:",
        calculate_vo2_max_estimate(190, 60)
    )

    workouts = [
        sample_workout,
        {
            "date": "2026-05-16",
            "exercise_type": "Cycling",
            "duration_minutes": 45,
            "distance_km": 12,
            "calories_burned": 500,
            "average_heart_rate": 150
        }
    ]

    print(
        "Weekly Volume Trend:",
        calculate_weekly_volume_trend(workouts),
        "minutes"
    )
