#Pure pythonic implementation gold status achieved here in this case. 

#Rotate the matrix in the clockwise direction by 90 o
#--> The way you do that is go ahead and transpose the matrx and reverse each row. 

#Rotate the matrix in the anti-clockwise direction by 90 o
#--> The way you do that is go ahead and transpose the matrix and reerse each column

#Rotate the matrix by 180o : Rotate by +90 twice. Reverse each row and then reverse each column. 
temp = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

#Pure python gold for rotation by 90 degrees. 

rotated = zip(*temp[::-1])
print rotated


#Pure python gold for rotation by -90 degrees. (Anti clockwise 90 degrees)
rotated = zip(*temp)[::-1]
print rotated
