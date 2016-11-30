INPUT nOrder

b <- []
c <- []

CREATE_ARRAY ()
	count <- 0
count2 <- 0
	x <- []
	array <- []
	WHILE count < nOrder
		count1 <- 0
		WHILE count1 < nOrder
			INPUT in1
			x.append(in1)
			INCREMENT count1
		END WHILE
		array.append(x)
	END WHILE
	RETURN array

ADD_MATRICES (mat1, mat2)
	added <- []
	row <- []
	FOR x = 0 to nOrder
		FOR y = 0 to nOrder
			temp <- mat1[x][y] + mat2[x][y]
			row.append(temp)
		END FOR 
		added.append(row)
	END FOR
	RETURN added

SUBTRACT_MATRICES (mat1, mat2)
	sub <- []
	row <- []
	FOR x = 0 to nOrder
		FOR y = 0 to nOrder
			temp <- mat1[x][y] - mat2[x][y]
row.append(temp)
		END FOR
sub.append(row)
		
	END FOR
	RETURN sub

MULTIPLY_MATRICES (mat1, mat2)
	mult <- []
	temp2 <- 0
	count <- 0
	FOR y = 0 to nOrder
		FOR x = 0 to nOrder
			FOR z = 0 to nOrder
				temp <- mat1[z][y] * mat2[x][z]
				temp2 <- temp2 + temp
			END FOR
			row.append(temp2)
		END FOR
		mult.append(row)
	END FOR
	RETURN mult

MULTIPLY_MAT_CONST(mat1, const)
FOR i = 0 to nOrder
		FOR j = 0 to nOrder
			mat1[i][j] <- mat1[i][j] * const
		END FOR
	END FOR
	RETURN mat1
	
tmp1 <- MULTIPLY_MATRICES(b,c)
tmp2 <- ADD_MATRICES(b,c)
tmp3 <- MULTIPLY_MAT_CONST(tmp2, 2)
ans <- SUBTRACT_MATRICES(tmp1, tmp3)
OUTPUT ans
