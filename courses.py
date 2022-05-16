''''
A bunch of functions containing the course requirement logic for each course outlined in conditions.json. These functions are then assigned to a hashtable which the main program uses to call
each function for each respective course, thus improving the readability of the actual function in the main program.
'''


def comp1511(courses_list):
    return True


def comp1521_comp1531_comp2041_comp2521(courses_list):
    return any(required in courses_list for required in ["COMP1511", "DPST1091", "COMP1917", "COMP1921"])


def comp2111(courses_list):
    return "MATH1081" in courses_list and\
           any(required in courses_list for required in ["COMP1511", "DPST1091", "COMP1917", "COMP1921"])


def comp2121(courses_list):
    return any(required in courses_list for required in ["COMP1511", "COMP1521", "COMP1917", "COMP1921", "DPST1091", "DPST1092"]) or\
           all(required in courses_list for required in ["MTRN2500", "COMP1911"])


def comp2511(courses_list):
    return "COMP1531" in courses_list and any(required in courses_list for required in ["COMP2521", "COMP1927"])


def comp3121(courses_list):
    return any(required in courses_list for required in ["COMP1927", "COMP2521"])


def comp3131(courses_list):
    return any(required in courses_list for required in ["COMP2511", "COMP2911"])


def comp3141(courses_list):
    return any(required in courses_list for required in ["COMP1927", "COMP2521"])


def comp3151(courses_list):
    return "COMP1927" in courses_list or\
           (any(required in courses_list for required in ["COMP1521", "DPST1092"]) and "COMP2521" in courses_list)


def comp3153(courses_list):
    return "MATH1081" in courses_list


def comp3161(courses_list):
    return any(required in courses_list for required in ["COMP2521", "COMP1927"])


def comp3211(courses_list):
    return any(required in courses_list for required in ["COMP3222", "ELEC2141"])


def comp3900(courses_list):
    total_uoc = len(courses_list) * 6
    return "COMP1531" in courses_list and any(required in courses_list for required in ["COMP2521", "COMP1927"]) and total_uoc >= 102


def comp3901(courses_list):
    level_1_uoc, level_2_uoc = 0, 0
    for course in courses_list:
        num = int(course[4:])
        if 1000 <= num < 2000:
            level_1_uoc += 6
        elif 2000 <= num < 3000:
            level_2_uoc += 6
            
        if level_1_uoc >= 12 and level_2_uoc >= 18:
            return True

    return False


def comp3902(courses_list):
    if "COMP3901" in courses_list:
        level_3_uoc = 0
        for course in courses_list:
            num = int(course[4:])
            if 3000 <= num < 4000:
                level_3_uoc += 6

            if level_3_uoc >= 12:
                return True

    return False


def comp4121(courses_list):
    return any(required in courses_list for required in ["COMP3121", "COMP3821"])


def comp4128(courses_list):
    if "COMP3821" in courses_list:
        return True

    if "COMP3121" in courses_list:
        level_3_uoc = 0
        for course in courses_list:
            num = int(course[4:])
            if 3000 <= num < 4000:
                level_3_uoc += 6

            if level_3_uoc >= 12:
                return True

    return False


def comp4141(courses_list):
    return "MATH1081" in courses_list and\
           any(required in courses_list for required in ["COMP1927", "COMP2521"])


def comp4161(courses_list):
    total_uoc = len(courses_list) * 6
    return total_uoc >= 18


def comp4336(courses_list):
    return "COMP3311" in courses_list


def comp4418(courses_list):
    return "COMP3411" in courses_list


def comp4601(courses_list):
    total_uoc = len(courses_list) * 6
    return any(required in courses_list for required in ["COMP2511", "COMP2911"]) and total_uoc >= 24


def comp4951(courses_list):
    comp_uoc = 0
    for course in courses_list:
        if "COMP" in course:
            comp_uoc += 6

        if comp_uoc >= 36:
            return True

    return False


def comp4952(courses_list):
    return "COMP4951" in courses_list


def comp4953(courses_list):
    return "COMP4952" in courses_list


def comp9301(courses_list):
    required = set(["COMP6443", "COMP6843", "COMP6445", "COMP6845", "COMP6447"])
    courses_taken_from_req = len(required.intersection(set(courses_list)))
    return courses_taken_from_req >= 2


def comp9302(courses_list):
    required = set(["COMP6443", "COMP6843", "COMP6445", "COMP6845", "COMP6447"])
    courses_taken_from_req = len(required.intersection(set(courses_list)))
    return any(required in courses_list for required in ["COMP6441", "COMP6841"]) and courses_taken_from_req >= 2


def comp9417(courses_list):
    return "MATH1081" in courses_list and any(required in courses_list for required in ["COMP1531", "COMP2041", "COMP1927", "COMP2521"])


def comp9418(courses_list):
    return any(required in courses_list for required in ["MATH5836", "COMP9417"])


def comp9444(courses_list):
    return any(required in courses_list for required in ["COMP1927", "COMP2521", "MTRN3500"])


def comp9447(courses_list):
    return any(required in courses_list for required in ["COMP6441", "COMP6841", "COMP3441"])


def comp9491(courses_list):
    required = set(["COMP9417", "COMP9418", "COMP9444", "COMP9447"])
    courses_taken_from_req = len(required.intersection(set(courses_list)))
    return courses_taken_from_req >= 3


COURSES = {
    "COMP1511": comp1511,
    "COMP1521": comp1521_comp1531_comp2041_comp2521,
    "COMP1531": comp1521_comp1531_comp2041_comp2521,
    "COMP2041": comp1521_comp1531_comp2041_comp2521,
    "COMP2111": comp2111,
    "COMP2121": comp2121,
    "COMP2511": comp2511,
    "COMP2521": comp1521_comp1531_comp2041_comp2521,
    "COMP3121": comp3121,
    "COMP3131": comp3131,
    "COMP3141": comp3141,
    "COMP3151": comp3151,
    "COMP3153": comp3153,
    "COMP3161": comp3161,
    "COMP3211": comp3211,
    "COMP3900": comp3900,
    "COMP3901": comp3901,
    "COMP3902": comp3902,
    "COMP4121": comp4121,
    "COMP4128": comp4128,
    "COMP4141": comp4141,
    "COMP4161": comp4161,
    "COMP4336": comp4336,
    "COMP4418": comp4418,
    "COMP4601": comp4601,
    "COMP4951": comp4951,
    "COMP4952": comp4952,
    "COMP4953": comp4953,
    "COMP9301": comp9301,
    "COMP9302": comp9302,
    "COMP9417": comp9417,
    "COMP9418": comp9418,
    "COMP9444": comp9444,
    "COMP9447": comp9447,
    "COMP9491": comp9491,
}