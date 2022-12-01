<?php
$current_pos = 0;
$input_text  = "11+1-(2*31)";

function expr() {
	global $input_text;
	global $current_pos;
	$res = term();
	while ($current_pos < strlen($input_text)) {
		if ($input_text[$current_pos] == "+") {
			next_pos();
			$res += term();
			continue;
		} elseif ($input_text[$current_pos] == "-") {
			next_pos();
			$res -= term();
			continue;
		} else {
			break;
		}
	}
	return $res;
}

function term() {
	global $input_text;
	global $current_pos;
	$res = factor();
	while ($current_pos < strlen($input_text)) {
		if ($input_text[$current_pos] == "*") {
			next_pos();
			$res *= factor();
			continue;
		} elseif ($input_text[$current_pos] == "/") {
			next_pos();
			$res /= factor();
			continue;
		} else {
			break;
		}
	}
	return $res;
}

function factor() {
	global $input_text;
	global $current_pos;
	if ($input_text[$current_pos] == "(") {
		next_pos();
		$res = expr();
		if ($input_text[$current_pos] == ")") {
			next_pos();
		}
		return $res;
	}
	return number();
}

function number() {
	global $current_pos;
	global $input_text;
	$res = "";
	while ($current_pos < strlen($input_text) && is_number($input_text[$current_pos])) {
		$res = $res.$input_text[$current_pos];
		next_pos();
	}
	if ($res == "") {
		return 0;
	}
	return (int) $res;
}

function is_number($num_string): bool {
	if ($num_string == "0") {
		return true;
	}
	$is_number = (int) $num_string;
	return $is_number == 0 ? false : true;
}

function next_pos() {
	global $current_pos;
	global $input_text;
	$current_pos = $current_pos + 1;
	if (strlen($input_text) <= $current_pos) {
		return null;
	}
	return $input_text[$current_pos];
}

$res = expr();
echo $res;