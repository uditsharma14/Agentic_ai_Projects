def calculate(expression: str):
    try:
        return eval(expression)
    except Exception as e:
        return f"Calculation error: {e}"


def average_dog_weight(breed: str):
    breed = breed.lower().strip()

    dog_weights = {
        "bulldog": "A Bulldog weighs around 51 lbs",
        "collie": "A Collie weighs around 50 lbs",
        "labrador": "A Labrador weighs around 70 lbs",
        "poodle": "A Poodle weighs around 45 lbs",
        "beagle": "A Beagle weighs around 25 lbs"
    }

    return dog_weights.get(
        breed,
        f"I do not know the average weight for {breed}"
    )


known_actions = {
    "calculate": calculate,
    "average_dog_weight": average_dog_weight
}