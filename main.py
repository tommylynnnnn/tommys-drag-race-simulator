from queens import ALL_QUEENS, select_queens

def main():
    print("Welcome to the Drag Race Simulator!")
    print("Available queens:")
    for q in ALL_QUEENS:
        print("-", q)

    print("\nSelect between 4 and 18 queens (comma separated):")
    user_input = input("> ")

    chosen = [name.strip() for name in user_input.split(",")]
    cast = select_queens(chosen)

    print("\nYour cast is:")
    for queen in cast:
        print("-", queen)

if __name__ == "__main__":
    main()
