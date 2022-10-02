
current_pos = 0
input_exp = "11+(22-20)"

def main():
	res = expr()
	print(res)

def expr():
	global current_pos
	global input_exp
	res = factor()
	while(current_pos < len(input_exp) ):
		if (input_exp[current_pos] == "+"):
			next()
			res += factor()
			continue
		elif (input_exp[current_pos] == "-"):
			next()
			res -= factor()
			continue
		return res
	return res

def factor():
	global current_pos
	global input_exp
	if (input_exp[current_pos] == "("):
		next()
		res = expr()
		if (input_exp[current_pos] == ")"):
			next()
		return res
	return number()

def number():
	global current_pos
	global input_exp
	res = ""
	while( current_pos < len(input_exp) and input_exp[current_pos].isdigit()):
		res += input_exp[current_pos]
		next()
	if (res == ""):
		return 0
	return int(res)

def next():
	global current_pos
	global input_exp
	current_pos += 1
	if (len(input_exp) >= current_pos):
		return None
	return input_exp[current_pos]

main()