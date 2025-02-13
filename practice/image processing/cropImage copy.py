from PIL import Image
import pprint

img = Image.open("./design1.jpeg").convert("L")

w,h = img.size

chunkWidth = 10

# def crop():

section = img.crop((0, 0, 20, h))
section2 = img.crop((20, 0, 40, h))
section3 = img.crop((int(w/2), 0, int(w/2) + 20, h))

pixels = section.getdata()
average = sum(pixels)/len(pixels)
minVal = min(pixels)
maxVal = max(pixels)
range = maxVal - minVal

print("average:", average)
print("min:", minVal)
print("max:", maxVal)
print("range:",range)

pixels2 = section2.getdata()
average2 = sum(pixels2)/len(pixels2)
minVal2 = min(pixels2)
maxVal2 = max(pixels2)
range2 = maxVal2 - minVal2

print("average2:", average2)
print("min2:", minVal2)
print("max2:", maxVal2)
print("range2:",range2)


pixels3 = section3.getdata()
average3 = sum(pixels3)/len(pixels3)
minVal3 = min(pixels3)
maxVal3 = max(pixels3)
range3 = maxVal3 - minVal3

print("average3:", average3)
print("min3:", minVal3)
print("max3:", maxVal3)
print("range3:",range3)




# def getVariance(slice : list):


# def findChunkWidth(image_length) -> int:
#     max_divisible_number = 10
#     start = 5
#     chunk_size = image_length
#     for i in range(start, max_divisible_number):
#         if((image_length % i) == 0):
#             chunk_size = image_length / i
#         else:
#             start = max_divisible_number
#             max_divisible_number = max_divisible_number * 2
#     # if(chunk_size > 20):

#     print('chunk_size:', chunk_size)
        
# findChunkWidth(w)

# img.show()

# print("height:", h, "width:", w)