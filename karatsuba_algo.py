import sys, math

# shift bits to the right and count number of times
# this gives the number of bits we have
def lg_flr(n):

	r = 0
	while n > 0:
		n >>= 1
		r += 1
	return r



def mult_ceil_01(x, y, C):

    
	lx = lg_flr(x) # number of bits for the first number
	ly = lg_flr(y) # number of bits for the second number
	
	n = min(lx, ly) # minimum of the 2 numbers , basically the bit 
	
	ns = (n >> 1) + (n % 2) # divide by 2 and add the remainder 
	
	assert(ns == math.ceil(n/2)) # confirm the bit method above works to get the ceil 
	
	if (x <= 1) or (y <= 1):
		# for a simplistic case where both are less than 1 we just mutliply simply
		return x * y
	
	xl = x % (1 << ns) 
	xh = x >> ns
	yl = y % (1 << ns)
	yh = y >> ns
	# add lower and higher parts 
	xc = xl + xh
	yc = yl + yh
	
    
	zc = mult_ceil_01(xc, yc, C)
	zh = mult_ceil_01(xh, yh, C)
	zl = mult_ceil_01(xl, yl, C)
	#print(str(ns) +',' + str(xh) +',' + str(xl) +',' + str(yh) +',' + str(yl) +',' + str(zh) +',' + str(zc) +',' + str(zl))
	C.append(str(ns) +',' + str(xh) +',' + str(xl) +',' + str(yh) +',' + str(yl) +',' + str(zh) +',' + str(zc) +',' + str(zl) + '\n')
    

    # [value] << steps : move value steps number of times to the left 
    # [value] >> steps : move value steps number of times to the right

    
	return (zh << (ns << 1)) + (zc << ns) - ((zh + zl) << ns) + zl




try:
	input_file = open(sys.argv[1], 'r')
except:
	print('HW1_Pass: Could not open input file\n')
	exit()
Input_Lines = input_file.readlines()
input_file.close()

x = int(Input_Lines[0])
y = int(Input_Lines[1])

C = []

z = mult_ceil_01(x, y, C)

output_file = open('output.txt', 'w')
output_file.writelines(C)
output_file.close()
