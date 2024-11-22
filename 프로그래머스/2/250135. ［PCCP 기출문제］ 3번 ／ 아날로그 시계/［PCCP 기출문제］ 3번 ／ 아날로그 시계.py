def solution(h1, m1, s1, h2, m2, s2):
    def set_times_to_sec(h, m, s):
        seconds = h * 3600 + m * 60 + s

        second_degree = (s * 6) % 360
        minute_degree = (m * 6 + s * 0.1) % 360
        hour_degree = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360

        result = (h * 60 + m) * 2 - h

        if second_degree >= minute_degree:
            result += 1
        if second_degree >= hour_degree:
            result += 1

        if h >= 12:
            result -= 2

        return result

    result = set_times_to_sec(h2, m2, s2) - set_times_to_sec(h1, m1, s1)

    if h1 in [0, 12] and m1 == 0 and s1 == 0:
        result += 1

    return result
