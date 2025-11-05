from prac_06.programming_language import ProgrammingLangauge


def main():

    python = ProgrammingLangauge("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLangauge("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLangauge("Ruby", "Dynamic", True, 1995)

    # print(python)
    # print(visual_basic)
    # print(ruby)

    languages = [ruby, python, visual_basic]

    print(languages)

    print("The dynamically typed languages are: ")
    dynamic_language = [language.name for language in languages if language.is_dynamic()]
    print(dynamic_language)
    for language in dynamic_language:
        print(language)


    # print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)



main()




