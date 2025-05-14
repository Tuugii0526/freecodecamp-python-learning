# Бид одоо camelCase болон pascalCase аар бичсэн текстийг snakeCase болгох зорилготой . Бид үүний хажуугаар list comprehension хэмээх ойлголтыг харая даа . 
def pascalOrCamelCaseToSnakeCase(text:str):
    letters=[]
    for char in text:
        if char.isupper():
            letters.append('_'+char.lower())
        else:
            letters.append(char)
    underscoredLetters=''.join(letters)
    print(f'result: {underscoredLetters.strip('_')}')
def pascalOrCamelCaseToSnakeCaseUsingListComprehension(text:str):
    letters=['_'+char.lower() if char.isupper() else char for char in text]
    underscoredLetters=''.join(letters)
    print(f'result: {underscoredLetters.strip('_')}')
    return underscoredLetters.strip('_')
def main():
    pascalOrCamelCaseToSnakeCaseUsingListComprehension('hiHow')
main()