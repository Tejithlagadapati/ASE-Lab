
def calculate_cost(hours, rate):
    if hours <= 0 or rate < 0:
        raise ValueError("Invalid booking details")
    return hours * rate


if __name__ == "__main__":
    print("Booking cost:", calculate_cost(3, 200))
