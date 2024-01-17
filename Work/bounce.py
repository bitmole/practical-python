# bounce.py
#
# Exercise 1.5

def main():
    cur_height = 100

    for bounce in range(10):
        cur_height *= 3/5
        print(bounce+1, round(cur_height, 4))

if __name__ == "__main__":
    main()
