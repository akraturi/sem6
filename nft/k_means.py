from random import shuffle
import math 

def distance(a,b):
    x1,y1 = a
    x2,y2 = b
    return round(math.sqrt((x1-x2)**2+(y1-y2)**2),3)

def update_centroids(clusters):
    #print(clusters.keys())
    result = dict()
    for elem in clusters.keys():
        #print(clusters[elem])
        new_centroid = mean(clusters[elem])
        result[new_centroid] = []
    return result 

def mean(tupple_list):
    x_avg = 0
    y_avg = 0
    for tupple in tupple_list:
        x,y = tupple
        x_avg += x
        y_avg += y
    total =  len(tupple_list)
    x_avg = round(x_avg,3)
    y_avg = round(y_avg,3)
    return (x_avg/total,y_avg/total)

def sse(centroids,patterns):
    result = 0
    for center in centroids:
        for pattern in patterns:
            result += (distance(center,pattern))**2
    return result

patterns = []

with open("k_means_inp","r") as inp:
     for line in inp:
         x,y = list(map(int,line.split()))
         patterns.append((x,y))

#print(patterns)
k = int(input("No. of clusters:"))

shuffle(patterns)

k_centers = patterns[0:k]

clusters = dict()
for center in k_centers:
    clusters[center] = []

print(clusters)

last_sse = -1
current_sse = 0

while True:
    for pattern in patterns:
        min_dist = 100000000000
        min_center = None
        for center in k_centers:
            curr_dist = distance(pattern,center)
            if min_dist > curr_dist:
               min_dist = curr_dist
               min_center = center

        clusters[min_center].append(pattern)     
    
    print(clusters)
    clusters=update_centroids(clusters)
    print(clusters)

    current_sse=sse(clusters.keys(),patterns)
    if last_sse == current_sse:
       break
    last_sse = current_sse

