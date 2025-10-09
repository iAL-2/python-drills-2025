def letterGrade(score):
    grade = {
        10:"A",
        9: "A",
        8: "B",
        7: "C",
        6: "D"
    }
    return grade.get(score//10, "F")