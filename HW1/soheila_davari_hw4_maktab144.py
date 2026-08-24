#4
def file_analyzer(filename):
    success=0
    skipped=0
    try:
        with open ( filename , "r") as file:
            for line in file:
                try:
                    line=line.strip()
                    name, score=line.split(",")
                    score= int(score)
                    print(f"{name} scored {score} points.")
                    success+=1
                except ValueError:
                    print(f"skipped bad line: {line}")
                    skipped+=1
            print(f"\nsuccessful lines: {success}")
            print(f"skipped lines: {skipped}")
    except FileNotFoundError:
        print("Error: file not found.")


file_analyzer("G:\venv\HW1\Untitled-1.txt")

