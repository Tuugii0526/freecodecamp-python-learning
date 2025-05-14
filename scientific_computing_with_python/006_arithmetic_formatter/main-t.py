def checkProblem(problem):
    problem_destructured=problem.split(' ')
    if problem_destructured[1]!='+' and problem_destructured[1]!='-':
        raise ValueError("Error: Operator must be '+' or '-'.")
    for number_check_index in [0,2]:
        if not problem_destructured[number_check_index].isdigit():
            raise ValueError('Error: Numbers must only contain digits.')
        if len(problem_destructured[number_check_index])>4:
            raise ValueError('Error: Numbers cannot be more than four digits.')
        problem_destructured[number_check_index]=problem_destructured[number_check_index]
    problem_destructured.append(max(len(problem_destructured[0]),len(problem_destructured[2])))
    return problem_destructured
def putOperandToRight(spaceCount:int,operand:str):
    operandLength=len(operand) 
    fillSpaceCount=spaceCount-operandLength
    fillSpace=''
    while fillSpaceCount>0:
        fillSpace+=' '
        fillSpaceCount-=1
    return fillSpace+operand
def putOperatorAndOperand(spaceCount:int,operand:str,operator:str):
    operandLength=len(operand) 
    fillSpaceCount=spaceCount-operandLength-1
    fillSpace=''
    while fillSpaceCount>0:
        fillSpace+=' '
        fillSpaceCount-=1
    return operator+fillSpace+operand
def generateDash(max):
    dash_list_string=''.join(['_' for i in range(max)])
    return dash_list_string
def putResult(spaceCount:int,strInt:str,strInt2:str,operator:str):
    result=0
    if(operator=='+'):
        result=int(strInt)+int(strInt2)
    else:
        result=int(strInt)-int(strInt2)
    return putOperandToRight(spaceCount,str(result))
def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        raise ValueError('Error: Too many problems.')
    problems_destructured=[]
    for problem in problems:
        problem_destructured=checkProblem(problem)
        problems_destructured.append(problem_destructured)
    rowStrings=['' for _ in range(4)]
    for problem in problems_destructured:
        rowStrings[0]+=putOperandToRight(problem[3]+2,problem[0])+'    '
        rowStrings[1]+=putOperatorAndOperand(problem[3]+2,problem[2],problem[1])+'    '
        rowStrings[2]+=generateDash(problem[3]+2)+'    '
        rowStrings[3]+=putResult(problem[3],problem[0],problem[2],problem[1])+'    '
    fix_array=map(lambda rowString:rowString.strip(' '),rowStrings)
    return '\n'.join(rowStrings)
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')