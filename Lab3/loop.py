#first
for i in range(-5, 5):
    #print(i)
    print(i, end = ' ')
    
#second
playListRating = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = playListRating[0]
while(i < len(playListRating) and rating >= 6) :
    print(f"{rating}")
    i += 1
    rating = playListRating[i]

#third
square = ['red', 'yellow', 'green', 'purple', 'blue']
for i in square: print(f"{i}", end=' ')