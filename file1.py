#temp, rainfall, humidity---------------
kanto = [73,67,43]
johto = [91,88,64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]

#received particular number  to determine if a region is well suited for growing apples
parameter = [0.3,0.2,0.5]


def crop_yield(region,parameter):
    result = 0
    for c,p in zip(region,parameter):
        result += c*p
    return result

kant_crop = crop_yield(kanto,parameter)
("The expected yield of apples in Kanto region is {} tons per hectare.".format(kant_crop))