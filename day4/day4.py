with open("input.txt") as f:
    counter = 0
    id_sections = []
    original_password = {}
    passport_fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]  # "cid"

    eye_color_ok = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for idx, line in enumerate(f.readlines()):

        if line == "\n":
            print(original_password)
            counter += 1
            for passport_field in passport_fields:
                if passport_field not in id_sections:
                    print("wow")
                    print(id_sections)
                    counter -=1
                    break

            id_sections = []
            original_password = {}


        sections = line.split(" ")
        for section in sections:
            if section != "\n":
                field = section.split(":")[0]
                value = section.split(":")[1]

                original_password[field] = value
                id_sections.append(section.split(":")[0])



counter += 1
print(id_sections)
for passport_field in passport_fields:
    print(counter)
    if passport_field not in id_sections:
        print("wow")
        print(id_sections)
        counter -=1
        break

print(counter)
