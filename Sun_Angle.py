def sun_angle(time):
    hours, mins = time.split(':')
    angle = 0
    if int(hours) < 6 or (int(hours) >= 18 and int(mins) > 0):
        return "I don't see the sun!"
    else:
        sun_day = 12 * 60
        time_past_six = (int(hours) - 6) * 60 + int(mins)
        angle = 180 * time_past_six / sun_day

    return round(angle, 2)

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")