# https://qiita.com/kRysTasis/items/77a4b4e6214646a079ed を参考にしました

current_pos = 0
input_exp = "11+(22*2)"

def main():
	res = expr()
	print(res)

def expr():
	global current_pos
	global input_exp
	res = term()
	while(current_pos < len(input_exp) ):
		if (input_exp[current_pos] == "+"):
			next()
			res += term()
			continue
		elif (input_exp[current_pos] == "-"):
			next()
			res -= term()
			continue
		return res
	return res

def term():
	global current_pos
	global input_exp
	res = factor()
	while(current_pos < len(input_exp)):
		if (input_exp[current_pos] == "*"):
			next()
			res *= factor()
			continue
		elif (input_exp[current_pos] == "/"):
			next()
			res /= factor()
			continue
		else:
			break
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