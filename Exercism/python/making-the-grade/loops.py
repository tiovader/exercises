def round_scores(student_scores: list[float]) -> list[int]:
    '''
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    '''

    return [*map(round, student_scores[::-1])]


def count_failed_students(student_scores: list[int]) -> int:
    '''
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    '''

    return sum(score <= 40 for score in student_scores)


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    '''
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    '''

    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> list[int]:
    '''
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    '''
    step = (highest - 40) // 4
    return [41 + i * step for i in range(4)]


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    '''
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     '''
    return [f'{i}. {name}: {score}'
            for i, (name, score) in enumerate(zip(student_names, student_scores), 1)]


def perfect_score(student_info: list[str, int]) -> list[str, int]:
    '''
    :param student_info: list of [<student name>, <score>] lists
    :return: [<student name>, 100].
    '''
    perfect_scores = [student for student in student_info if student[-1] == 100]
    return perfect_scores and perfect_scores[0]
