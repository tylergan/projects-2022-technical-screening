"""
First attempt. Later realised the readability on this is terrible.
"""


def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course
    can be unlocked by them.

    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """

    if target_course == "COMP1511":
        return True

    if target_course in ["COMP1521", "COMP1531", "COMP2041", "COMP2521"]:
        return any(required in courses_list for required in ["COMP1511", "DPST1091", "COMP1917", "COMP1921"])

    if target_course == "COMP2111":
        return "MATH1081" in courses_list and\
               any(required in courses_list for required in ["COMP1511", "DPST1091", "COMP1917", "COMP1921"])

    if target_course == "COMP2121":
        return any(required in courses_list for required in ["COMP1511", "COMP1521", "COMP1917", "COMP1921", "DPST1091", "DPST1092"]) or\
               all(required in courses_list for required in ["MTRN2500", "COMP1911"])

    if target_course == "COMP2511":
        return "COMP1531" in courses_list and any(required in courses_list for required in ["COMP2521", "COMP1927"])

    if target_course == "COMP3121":
        return any(required in courses_list for required in ["COMP1927", "COMP2521"])

    if target_course == "COMP3131":
        return any(required in courses_list for required in ["COMP2511", "COMP2911"])

    if target_course == "COMP3141":
        return any(required in courses_list for required in ["COMP1927", "COMP2521"])

    if target_course == "COMP3151":
        return "COMP1927" in courses_list or\
               (any(required in courses_list for required in ["COMP1521", "DPST1092"]) and "COMP2521" in courses_list)

    if target_course == "COMP3153":
        return "MATH1081" in courses_list

    if target_course == "COMP3161":
        return any(required in courses_list for required in ["COMP2521", "COMP1927"])

    if target_course == "COMP3211":
        return any(required in courses_list for required in ["COMP3222", "ELEC2141"])

    if target_course == "COMP3900":
        total_uoc = len(courses_list) * 6
        return "COMP1531" in courses_list and any(required in courses_list for required in ["COMP2521", "COMP1927"]) and total_uoc >= 102

    if target_course == "COMP3901":
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

    if target_course == "COMP3902":
        if "COMP3901" in courses_list:
            level_3_uoc = 0
            for course in courses_list:
                num = int(course[4:])
                if 3000 <= num < 4000:
                    level_3_uoc += 6

                if level_3_uoc >= 12:
                    return True

        return False

    if target_course == "COMP4121":
        return any(required in courses_list for required in ["COMP3121", "COMP3821"])

    if target_course == "COMP4128":
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

    if target_course == "COMP4141":
        return "MATH1081" in courses_list and\
               any(required in courses_list for required in ["COMP1927", "COMP2521"])

    if target_course == "COMP4161":
        total_uoc = len(courses_list) * 6
        return total_uoc >= 18

    if target_course == "COMP4336":
        return "COMP3311" in courses_list

    if target_course == "COMP4418":
        return "COMP3411" in courses_list

    if target_course == "COMP4601":
        total_uoc = len(courses_list) * 6
        return any(required in courses_list for required in ["COMP2511", "COMP2911"]) and total_uoc >= 24

    if target_course == "COMP4951":
        comp_uoc = 0
        for course in courses_list:
            if "COMP" in course:
                comp_uoc += 6

            if comp_uoc >= 36:
                return True

        return False

    if target_course == "COMP4952":
        return "COMP4951" in courses_list

    if target_course == "COMP4953":
        return "COMP4952" in courses_list

    if target_course in ["COMP9301", "COMP9302"]:
        required = set(["COMP6443", "COMP6843", "COMP6445", "COMP6845", "COMP6447"])
        courses_taken_from_req = len(required.intersection(set(courses_list)))

        if target_course == "COMP9301":
            return courses_taken_from_req >= 2
        return any(required in courses_list for required in ["COMP6441", "COMP6841"]) and courses_taken_from_req >= 2

    if target_course == "COMP9417":
        return "MATH1081" in courses_list and any(required in courses_list for required in ["COMP1531", "COMP2041", "COMP1927", "COMP2521"])

    if target_course == "COMP9418":
        return any(required in courses_list for required in ["MATH5836", "COMP9417"])

    if target_course == "COMP9444":
        return any(required in courses_list for required in ["COMP1927", "COMP2521", "MTRN3500"])

    if target_course == "COMP9447":
        return any(required in courses_list for required in ["COMP6441", "COMP6841", "COMP3441"])

    if target_course == "COMP9491":
        required = set(["COMP9417", "COMP9418", "COMP9444", "COMP9447"])
        courses_taken_from_req = len(required.intersection(set(courses_list)))
        return courses_taken_from_req >= 3
