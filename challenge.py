from PIL import Image

img = Image.open("meteor_challenge_01.png")
matrix = img.load()
WIDTH, HEIGHT = img.size
STAR = (255, 255, 255, 255)
METEOR = (255, 0, 0, 255)
WATER = (0, 0, 255, 255)


def get_phrase(star_binary_phrase, meteor_binary_phrase):
    star_binary_phrase = "".join(star_binary_phrase)
    meteor_binary_phrase = "".join(meteor_binary_phrase)

    star_phrase = []
    for i in range(0, len(star_binary_phrase), 8):
        star_phrase.append(chr(int(star_binary_phrase[i : i + 8], 2)))

    meteor_phrase = []
    for i in range(0, len(meteor_binary_phrase), 8):
        meteor_phrase.append(chr(int(meteor_binary_phrase[i : i + 8], 2)))

    return "".join(star_phrase) + "".join(meteor_phrase)


stars = 0
meteors = 0
water_cols = set()
water_meteors = 0

star_binary_phrase = []
meteor_binary_phrase = []

for c in range(WIDTH):
    col_star_count = 0
    col_meteor_count = 0
    for r in reversed(range(HEIGHT)):
        pixel = matrix[c, r]
        if pixel == WATER and c not in water_cols:
            water_cols.add(c)
        elif pixel == STAR:
            stars += 1
            col_star_count += 1
        elif pixel == METEOR:
            meteors += 1
            col_meteor_count += 1
            if c in water_cols:
                water_meteors += 1

    star_binary_phrase.append(str(col_star_count))
    meteor_binary_phrase.append(str(col_meteor_count))

hidden_phrase = get_phrase(star_binary_phrase, meteor_binary_phrase)
print(
    f"Number of stars: {stars}\nNumber of meteors: {meteors}\nNumber of water meteors: {water_meteors}\nHidden phrase: {hidden_phrase}"
)
