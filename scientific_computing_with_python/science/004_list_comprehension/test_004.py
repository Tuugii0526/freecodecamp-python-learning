from mainY import pascalOrCamelCaseToSnakeCaseUsingListComprehension;
def test_pascal_camel_case_convertor():
    assert pascalOrCamelCaseToSnakeCaseUsingListComprehension('HiHow') == 'hi_how'

    assert pascalOrCamelCaseToSnakeCaseUsingListComprehension('hiHowAreYou') == 'hi_how_are_you'