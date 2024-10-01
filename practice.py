def my_final_grade_calculation(data_list):
    grade_report = {}

    learner = data_list[0].strip().lower()
    quiz_marks = []
    task_scores = []
    exam_midterm = int(data_list[11])
    exam_final = int(data_list[12])

    quiz_marks = [int(data_list[i]) for i in range(1, 7)]
    task_scores = [int(data_list[j]) for j in range(7, 11)]

    quiz_marks = sorted(quiz_marks)[2:]
    task_scores = sorted(task_scores)[1:]

    avg_quiz = sum(quiz_marks) // len(quiz_marks)
    avg_task = sum(task_scores) // len(task_scores)

    final_grade = (avg_quiz + avg_task + exam_midterm + exam_final) / 4
    result_status = "pass" if final_grade >= 60 else "fail"

    grade_report[learner] = result_status
    return grade_report

summary_results = {}
with open("data.txt", "r") as file_handler:
    for line in file_handler:
        parsed_data = line.strip().split(',')
        result = my_final_grade_calculation(parsed_data)
        summary_results.update(result)

print(summary_results)
