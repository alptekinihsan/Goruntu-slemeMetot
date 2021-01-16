import numpy
from PIL import Image
def mean_filter(veri, filtre):
    d = []
    index = filtre // 2
    son_veri = []
    son_veri = numpy.zeros((len(veri),len(veri[0])))
    for i in range(len(veri)):
        for j in range(len(veri[0])):
            for z in range(filtre):
                if i + z - index < 0 or i + z - index > len(veri) - 1:
                    for c in range(filtre):
                        d.append(0)
                else:
                    if j + z - index < 0 or j + index > len(veri[0]) - 1:
                        d.append(0)
                    else:
                        for k in range(filtre):
                            d.append(veri[i + z - index][j + k - index])
            d.sort()
            son_veri[i][j] = d[len(d) // 2]
            d = []
    return son_veri
def main():
    resim=Image.open("download.jpg")
    resim.show()
    img = Image.open("download.jpg").convert("L")
    arr = numpy.array(img)
    resim = mean_filter(arr, 3)
    img = Image.fromarray(resim)

    img.show()
main()
