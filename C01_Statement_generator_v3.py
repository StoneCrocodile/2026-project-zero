def make_statement(statement, decoration, lines):
    """Creates headings (3 lines), subheadings (2 lines) and
    emphasised text / mini-headings (1line). Only use emoji for
    single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines ==1:
        print(middle)
    elif lines ==2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)

make_statement(statement="programming is fun!", decoration="=", lines= 3)
make_statement(statement="programming is still fun!", decoration="*", lines= 2)
make_statement(statement="Emoji in Action", decoration="👍", lines=1)