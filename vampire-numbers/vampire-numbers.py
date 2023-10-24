import sys

def get_digits(num_1: int, num_2: int = 0) -> list[int]:
	l = []
	while num_1 > 0:
		remainder, num_1 = num_1 % 10, num_1 // 10
		l.append(remainder)
	while num_2 > 0:
		remainder, num_2 = num_2 % 10, num_2 // 10
		l.append(remainder)
	return sorted(l)


def check_fangs(fang_1: int, fang_2: int) -> bool:
	multiplied = fang_1 * fang_2
	if fang_1 * 10 <= fang_2 or fang_2 * 10 <= fang_1:
		return False
	vampire_digits = get_digits(multiplied)
	factor_digits = get_digits(fang_1, fang_2)
	return len(factor_digits)%2==0 and ((fang_1%10)or(fang_2%10)) and vampire_digits == factor_digits

def main():
	l = set()
	start, end = 10, 1000
	for i in range(start, end+1):
		for j in range(i, end+1):
			if check_fangs(i, j):
				print(f'{i*j}, {(i, j)}', file=sys.stderr)
				l.add(i*j)
	print(*sorted(l), sep='\n')


if __name__ == '__main__':
	main()
