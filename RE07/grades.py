
def sort_grades(records):

    def grade_order(i):
        grade_sum = 0
        for grade in i[2]:
            grade_sum += grade
        return grade_sum

    def name_order(i):
        return i[0]

    def num_order(i):
        return int(i[1][2:])

    ordered_records = sorted(records, key=num_order)
    ordered_records = sorted(ordered_records, key=name_order)
    ordered_records = sorted(ordered_records, key=grade_order, reverse=True)

    return tuple(ordered_records)
