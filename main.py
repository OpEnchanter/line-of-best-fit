import json
points = json.loads(input("Points: "))
yInter = json.loads(input("Y-Intercept: "))
output = 0
for x in range (len(points)):
    output+=(points[x][1]-yInter)/(points[x][0])
output/=len(points)
print(f"Line of best fit slope: {output}")