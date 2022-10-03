$input_word = "11+22-50"
$current_pos = 0

def expr
	res = factor
	while $input_word[$current_pos] != nil do
		if $input_word[$current_pos] == "+"
			next_pos
			res += factor
			next
		elsif $input_word[$current_pos] == "-"
			next_pos
			res -= factor
			next
		end
		return res
	end
	return res
end

def factor
	res = ""
	if $input_word[$current_pos] == "("
		next_pos
		res = factor
		if $input_word[$current_pos] == ")"
			next_pos
		end
		return res
	end
	return number
end

def number
	res = ""
	while is_number?($input_word[$current_pos]) && $input_word[$current_pos] != nil do
		res += $input_word[$current_pos]
		next_pos
	end
	return res.to_i
end

def is_number?(str)
	return nil != (str =~ /\A[0-9]+\z/)
end

def next_pos
	$current_pos += 1
	if $input_word[$current_pos] == nil
		return nil
	end
	return $input_word[$current_pos]
end

result = expr
print result