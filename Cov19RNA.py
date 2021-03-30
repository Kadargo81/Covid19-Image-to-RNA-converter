from PIL import Image

# This Program takes the RGB image representing a COV-19
# RNA sequence sourced from 
# https://www.reddit.com/r/dataisbeautiful/comments/mg1cxr/oc_entire_genome_of_covid_virus_sarscov2/
# and turns the pixel data back into the original RNA sequence
#  and outputs the string to a file.
# A - red
# C - yellow
# G - green
# T - blue

pic = Image.open("Covid19ColorMap.png")


def pixelToColor(im):
    color = im.getpixel((0 ,0))
    red = (239, 71, 111)
    green = (6, 214, 160)
    blue = (17, 138, 178)
    yellow = (255, 209, 102)
    rna = ""
    myFile = open("Cov19RNA.txt", "w")

    for h in range(im.height):
        if h % 3 == 0:
            if h != 0:
                rna += "\n"
            for w in range(im.width):
                if w % 3 == 0:
                    color = im.getpixel((w, h))
                    if color == red:
                        rna += "A"
                    if color == green:
                        rna += "G"
                    if color == blue:
                        rna += "T"
                    if color == yellow:
                        rna += "C"
    #print(rna)
    myFile.write(rna)

pixelToColor(pic)