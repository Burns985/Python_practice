class Fibonacci:
    print("\nThe Fibonacci Series")
    lower = int(input("Please enter the starting term:\n"))
    limit = int(input("Please enter the last term:\n"))
    limited_series = []
    for i in range(-1, limit):
        if (i < 1):
            limited_series.append(i+1)
        elif(i == 1):
            limited_series.append(i)
        else:
            limited_series.append(limited_series[len(limited_series)-1] + limited_series[len(limited_series)-2])
            i = limited_series[len(limited_series)-1] + limited_series[len(limited_series)-2]

    print(limited_series[lower-1:limit])
