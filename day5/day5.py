with open("input.txt") as f:
    answerd_questions = 0
    part_two_answer = 0
    answerd_question_string = ""
    already_answered_questions = []
    part_two_question_list = []
    commen_list_of_questions = []
    for idx, line in enumerate(f.readlines()):

        if line == "\n":
            for question in answerd_question_string:
                if question not in already_answered_questions:
                    answerd_questions += 1
                    already_answered_questions.append(question)

            # part two
            print(part_two_question_list)
            shortest_list = ["a"]*10000
            for answer_list in part_two_question_list:
                if len(answer_list) > 0:
                    if len(answer_list) < len(shortest_list):
                        shortest_list = answer_list
            print(shortest_list)

            common_questions = [True]*len(shortest_list)
            for idx, question in enumerate(shortest_list):
                for questions in part_two_question_list[1:]:
                    print(question, questions)
                    if question not in questions:
                        common_questions[idx] = False
            print(common_questions)
            part_two_answer += sum(common_questions)
            answerd_question_string = ""
            already_answered_questions = []
            part_two_question_list = []
            print("\n")
        part_two_question_list.append(sorted(line.replace("\n", "")))
        answerd_question_string += line.replace("\n", "")

for question in answerd_question_string:
    if question not in already_answered_questions:
        answerd_questions += 1
        already_answered_questions.append(question)

# part two
print(part_two_question_list)

shortest_list = ["a"]*10000
for answer_list in part_two_question_list:
    if len(answer_list) > 0:
        if len(answer_list) < len(shortest_list):
            shortest_list = answer_list


common_questions = [True]*len(shortest_list)
for idx, question in enumerate(shortest_list):
    for questions in part_two_question_list[1:]:
        print(question, questions)
        if question not in questions:
            common_questions[idx] = False
print(common_questions)

part_two_answer += sum(common_questions)
print(part_two_answer)

answerd_question_string = ""
already_answered_questions = []