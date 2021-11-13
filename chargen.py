#!/usr/bin/python3
import scipy.stats
import random
import sys

def percent():
    return round(scipy.stats.truncnorm.rvs((0 - 50) / 34, (100 - 50) / 34, loc=50, scale=34, size=1)[0])

races = ['Charr', 'Human', 'Norn', 'Asura', 'Sylvari']
race = races[random.randint(0, len(races) - 1)]
if len(sys.argv) >= 2 and sys.argv[1] in races:
    race = sys.argv[1]
print("Race:", race)

genders = ['Male', 'Female']
gender = genders[random.randint(0, len(genders) - 1)]
if len(sys.argv) >= 3 and sys.argv[2] in genders:
    gender = sys.argv[2]
print("Gender:", gender)

professions = [
    'Warrior', 'Guardian', 'Revenant',
    'Ranger', 'Thief', 'Engineer',
    'Necromancer', 'Elementalist', 'Mesmer',
]
profession = professions[random.randint(0, len(professions) - 1)]
if len(sys.argv) >= 4 and sys.argv[3] in professions:
    profession = sys.argv[3]
print("Profession:", profession)

print("Height:", percent())
if race == races[0]: # Charr
    print("Build:", random.randint(1, 8 if gender == genders[0] else 7))
    print("Coat:", random.randint(1, 14 if gender == genders[0] else 16))
    print("Color:", random.randint(1, 35))
    print("Pattern Color:", random.randint(1, 35))

    print("Hair:", random.randint(1, 9 if gender == genders[0] else 10))
    print("Hair Color:", random.randint(1, 35))
    print("Accessory Color:", random.randint(1, 21))
    print("Face:", random.randint(1, 9))
    print("Horns:", random.randint(1, 23))
    print("Horn Length:", percent())

    print("Eye angle:", percent())
    print("Eye openness:", percent())
    print("Eye separation:", percent())
    if gender == genders[0]:
        print("Iris size:", percent())
        print("Eye size:", percent())
    else:
        print("Eye size:", percent())
        print("Iris size:", percent())
    print("Eyebrow position:", percent())
    print("Eyebrow angle:", percent())
    print("Eyebrow thickness:", percent())
    print("Eye color:", random.randint(1, 43))

    print("Nose bridge width:", percent())
    print("Nose point width:", percent())
    print("Nose bridge height:", percent())
    print("Tooth size:", percent())
    print("Lower jaw angle:", percent())
    print("Upper jaw angle:", percent())

    print("Ear length:", percent())
    print("Ear size:", percent())
    print("Head size:", percent())
elif race == races[1]: # Human
    print("Build:", random.randint(1, 7 if gender == genders[0] else 10))
    print("Skintone:", random.randint(1, 36))

    print("Face:", random.randint(1, 20 if gender == genders[0] else 27))
    print("Hair:", random.randint(1, 41))
    print("Hair Color:", random.randint(1, 46))
    print("Accessory Color:", random.randint(1, 21))
    if gender == genders[0]:
          print("Facial Hair:", random.randint(1, 17))

    print("Eye angle:", percent())
    print("Iris size:", percent())
    print("Eye openness:", percent())
    print("Eyebrow thickness:", percent())
    print("Eyebrow height:", percent())
    print("Eyebrow angle:", percent())
    print("Eye width:", percent())
    print("Eye color:", random.randint(1, 31))

    print("Nose length:", percent())
    print("Nose base width:", percent())
    print("Nose bridge width:", percent())
    print("Nose point height:", percent())
    print("Nose bridge height:", percent())

    print("Upper lip size:", percent())
    print("Lower lip size:", percent())
    print("Mouth width", percent())

    print("Chin length:", percent())
    print("Jaw width:", percent())
    if gender == genders[1]:
        print("Underbite?:", percent())
        print("Cheeks:", percent())
    print("Head size:", percent())
    print("Head width:", percent())
elif race == races[2]: # Norn
    print("Build:", random.randint(1, 5 if gender == genders[0] else 6))
    print("Skintone:", random.randint(1, 36))
    print("Tattoos:", random.randint(1, 25 if gender == genders[0] else 22))
    print("Tattoo color:", random.randint(1, 14))

    print("Face:", random.randint(1, 9 if gender == genders[0] else 11))
    print("Hair:", random.randint(1, 16 if gender == genders[0] else 20))
    print("Hair Color:", random.randint(1, 46))
    print("Accessory Color:", random.randint(1, 21))
    if gender == genders[0]:
          print("Facial Hair:", random.randint(1, 14))

    print("Eye angle:", percent())
    print("Iris size:", percent())
    print("Eye openness:", percent())
    print("Eyebrow thickness:", percent())
    print("Eyebrow height:", percent())
    print("Eyebrow angle:", percent())
    print("Eye width:", percent())
    print("Eye color:", random.randint(1, 31))

    print("Nose length:", percent())
    print("Nose base width:", percent())
    print("Nose bridge width:", percent())
    print("Nose point height:", percent())
    print("Nose bridge height:", percent())

    print("Upper lip size:", percent())
    print("Lower lip size:", percent())
    print("Mouth width", percent())

    print("Chin length:", percent())
    print("Jaw width:", percent())
    if gender == genders[1]:
        print("Underbite?:", percent())
        print("Cheeks:", percent())
    print("Head size:", percent())
    print("Head width:", percent())
elif race == races[3]: # Asura
    print("Build:", random.randint(1, 8))
    print("Skintone:", random.randint(1, 36))
    print("Skin markings:", random.randint(1, 8))
    print("Markings color:", random.randint(1, 36))

    print("Hair:", random.randint(1, 9))
    print("Hair Color:", random.randint(1, 46))
    print("Accessory Color:", random.randint(1, 21))
    print("Face:", random.randint(1, 8 if gender == genders[0] else 9))

    print("Ears:", random.randint(1, 7 if gender == genders[0] else 6))
    print("Ear point height:", percent())
    print("Ear thickness:", percent())
    print("Ear length:", percent())

    print("Eyebrow position:", percent())
    print("Eyebrow angle:", percent())
    print("Eyebrow thickness:", percent())
    print("Iris size:", percent())
    print("Eye openness:", percent())
    print("Eye angle:", percent())
    print("Eye size:", percent())
    print("Eye separation:", percent())
    print("Lower eyelid:", percent())
    print("Eye color:", random.randint(1, 43))

    print("Nose length:", percent())
    print("Nose base width:", percent())
    print("Nose bridge width:", percent())
    print("Nose point height:", percent())
    print("Nose bridge height:", percent())

    print("Upper lip size:", percent())
    print("Lower lip size:", percent())
    print("Mouth width", percent())
    print("Cheeks", percent())

    print("Jaw width:", percent())
    print("Jaw position:", percent())
    print("Chin length:", percent())
    print("Chin width:", percent())

    print("Head size:", percent())
elif race == races[4]: # Slyvari
    print("Build:", random.randint(1, 10 if gender == genders[0] else 12))
    print("Skintone:", random.randint(1, 96))
    print("Skin pattern:", random.randint(1, 7 if gender == genders[0] else 8))
    print("Pattern color:", random.randint(1, 64))
    print("Pattern light color:", random.randint(1, 40))
    print("Pattern brightness:", percent())

    print("Hair:", random.randint(1, 11 if gender == genders[0] else 12))
    print("Hair Color:", random.randint(1, 76))
    print("Face:", random.randint(1, 9 if gender == genders[0] else 10))

    print("Ears:", random.randint(1, 8))
    print("Ear length:", percent())
    print("Ear point height:", percent())

    print("Eyebrow height:", percent())
    print("Eyebrow angle:", percent())
    print("Eyebrow size:", percent())
    print("Iris size:", percent())
    print("Eye angle:", percent())
    print("Eye openness:", percent())
    print("Eye width:", percent())
    print("Eye size:", percent())
    print("Eye color:", random.randint(1, 38))

    print("Nose length:", percent())
    print("Nose base width:", percent())
    print("Nose bridge width:", percent())
    print("Nose point height:", percent())
    print("Nose bridge height:", percent())

    print("Upper lip size:", percent())
    print("Lower lip size:", percent())
    print("Mouth width", percent())

    if gender == genders[1]:
        print("Cheeks:", percent())
    print("Jaw width:", percent())
    print("Chin length:", percent())
    print("Head width:", percent())
    print("Head size:", percent())

# Just pick 3 colors, same on all armor
print("Clothing color 1:", random.randint(1, 21))
print("Clothing color 2:", random.randint(1, 21))
print("Clothing color 3:", random.randint(1, 21))

# Warrior - 3 - helms or shoulders, Guardian - 3 kinds of shoulders, Ranger - 3 pets
# Thief - 3 hat types, Engi - 3 - hat or back item, Necro - 3 facemasks, Ele - 4 Hats
# Mesmer - 3 hats, Rev - 3 hats
print("Professional Accessory:", random.randint(1, 4 if profession == professions[7] else 3))
print("Emotion:", ["Charm", "Nobility", "Might"][random.randint(0, 2)])

# Charr: 3 legions, 5 warbandmates, 3 sires
# Sylvari: 3 visions, 3 teachings, 4 cycles
# Asura: 3 colleges, 3 inventions, 4 mentors
# Norn: 3 strengths, 3 pasts, 4 spirits
# Human: 3 backgrounds, 3 regrets, 6 gods
print("Racial option 1:", random.randint(1, 3))
print("Racial option 2:", random.randint(1, 5 if race == races[0] else 3))
print("Racial option 3:", random.randint(1, 3 if race == races[0] else 6 if race == races[1] else 4))
