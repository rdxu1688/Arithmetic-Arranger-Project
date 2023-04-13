def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems"

    first_number = []
    second_number = []
    operation = []
    length = []
    
    for s in problems:
        s_list = s.split(' ')

        if s_list[1] == "+" or s_list[1] == "-":
            filler = True # != didn't work but this did :/
        else:
            return "Error: Operator must be '+' or '-'."
        if s_list[0].isdigit() == False or s_list[2].isdigit() == False:
            return "Error: Numbers must only contain digits."

        first_number.append(s_list[0])
        operation.append(s_list[1])
        second_number.append(s_list[2])
        
        if len(s_list[0]) > 4 or len(s_list[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if len(s_list[0]) > len(s_list[2]):
            length.append(len(s_list[0]))
        else:
            length.append(len(s_list[2]))

    row_1 = ''
    row_2 = ''
    row_3 = ''

    for i in range(len(problems)):
        row_1 += ' ' * (length[i] - len(first_number[i]) + 2) + first_number[i] + '    '
        row_2 += operation[i] + ' ' * (length[i] - len(second_number[i]) + 1) + second_number[i] + '    '
        row_3 += '-'* (length[i]+2) + '    '

    row_1 += '\n'
    row_2 += '\n'
    arranged_problems = row_1 + row_2 + row_3 
    return arranged_problems