import file_operations
import random
import os
from faker import Faker


SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар"
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]

ALF = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}

FAKE = Faker("ru_RU")


def do_this():
    runic_skills = []
    for skill in SKILLS:
        lis = list(skill)
        for let in lis:
            key = ALF[let]
            skill = skill.replace(let, key)
        runic_skills.append(skill)
    return runic_skills


def main():
    runic_skills = do_this()
    for number in range(10):
        skill_end = random.sample(runic_skills, 3)
        context = {
            "first_name": FAKE.first_name(),
            "last_name": FAKE.last_name(),
            "job": FAKE.job(),
            "town": FAKE.city(),
            "strength": random.randint(1, 100),
            "agility": random.randint(1, 100),
            "endurance": random.randint(1, 100),
            "intelligence": random.randint(1, 100),
            "luck": random.randint(1, 100),
            "skill_1": skill_end[0],
            "skill_2": skill_end[1],
            "skill_3": skill_end[2]
        }

        os.makedirs("output/svg", exist_ok=True)

        num = "output/svg/charsheet-{}.svg".format(number)
        file_operations.render_template("src/charsheet.svg", num, context)


if __name__ == '__main__':
    main()


