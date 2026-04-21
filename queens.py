ALL_QUEENS = [
    "Alaska", "Alyssa Edwards", "Bob the Drag Queen", "Katya",
    "Sasha Velour", "Bianca Del Rio", "Jinkx Monsoon",
    # Add more queens here
]

def select_queens(selected_names):
    if len(selected_names) < 4 or len(selected_names) > 18:
        raise ValueError("You must select between 4 and 18 queens.")

    for name in selected_names:
        if name not in ALL_QUEENS:
            raise ValueError(f"{name} is not a valid queen.")

    return selected_names
