from PIL import Image, ImageDraw

w, h = 3000, 1000
shape = [(40, 40), (w - 40, h - 40)]

# creating new Image object
img = Image.new("RGB", (w, h))

# create rectangle image
img1 = ImageDraw.Draw(img)
img1.rectangle(shape, fill="#FFFFFF", outline="black")

b_size = (w - 150)/106

data = [[0 for j in range(106)] for i in range(17)]

row = 0
col = 0


def f(x, y):
    return int(((y // 17) // (1 << (17 * x + (y % 17)))) % 2)


for j in range(106):
    row = 16
    k = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719
    for i in range(17):
        # temp = int( ( int(k // 17) * int(2**(-17 * j - k % 17) ) ) % 2 ) - пачиму не рабоатишь!
        pixel_var = f(j, k)
        b = (1/2) < pixel_var

        try:
            data[row][col] = 1 if b else 0
        except IndexError:
            print('{} {}'.format(row, col))

        row -= 1
        k += 1
    col += 1

col, row = 105, 16
for i in range(len(data)):
    col = 105
    for j in range(len(data[i])):

        y = (h / 2 - (b_size * 17 / 2)) + b_size * i
        x = 40 + b_size + b_size * j
        xy = [(x, y), (x + b_size, y + b_size)]

        block = ImageDraw.Draw(img)
        block.rectangle(
            xy, fill="#FFFFFF" if data[row][col] == 0 else "#000000", outline="black")
        col -= 1
    row -= 1
img.show()
