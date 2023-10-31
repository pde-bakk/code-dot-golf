import sys
from collections import defaultdict

states=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
abbrevs=['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE','DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


# d={}
# for name in states:
# 	val=int(name.replace(' ',''),36)%393%333%291%244%76
# 	print(name, val)
# 	d[val]=name
# s='DJ:DC.AAZ.ILV.SLAR:DIETHCCV:AT:NAY::LNOO.T.RY.NEMX.HE:K:::.I.A.AIK'.replace(':','..')
# for k, v in sorted(d.items()):
# 	print(k, v, v[0] + s[k])

def find_mod_chain(sets, iterations: int = 2, limit=None) -> list:

	m = max([max(x) for x in sets])
	if iterations == 0:
		return [m, ]
	if limit is None:
		limit = m
	best_chain = [limit, ]

	for i in range(len(sets), limit):
		n = [{k%i for k in x} for x in sets]
		if len(set.union(*n)) == sum(len(x) for x in n):
			r = find_mod_chain(n, iterations - 1)
			if r[-1] < best_chain[-1]:
				best_chain = [i, ] + r
	return best_chain



def display_mod_chain(chain: list[int]) -> None:
	*c, m = chain
	print('x', *c, sep='%')
	print(f'Highest remaining value is {m}')



def get_hash(s: str, start: int = 0):
	return int(s[start:].replace(' ',''),36)


def write_to_file(start_index: int, indexinator: str, modulos: list[int]):
	lines = [
		'import sys\n',
		f'for s in sys.argv[1:]:print(s[0]+{indexinator}[int(s.replace(" ",""),36)%{"%".join(map(str, modulos))}])'
	]
	with open(f'united-states-{start_index}.py', 'w') as f:
		f.writelines(lines)


def go_fuck_some_bitches():
	shortest = min([len(state) for state in states])

	for start_idx in range(shortest):
		numbers_by_abbrevs = defaultdict(set)
		for name, ab in zip(states, abbrevs):
			val = get_hash(name, start=start_idx)
			numbers_by_abbrevs[ab[1]].add(val)
		s = list(numbers_by_abbrevs.values())
	# print(numbers_by_abbrevs)
	# print(s)
		print(f'{start_idx=} gives')
		result = find_mod_chain(s, 5, 500)
		display_mod_chain(result)
		*chain, highest = result
		l = ['.' for _ in range(highest+1)]
		for n, state in enumerate(states):
			ab = abbrevs[n]
			val = get_hash(state, start=start_idx)
			# print(f'{state=}, {ab=}, {val=}')
			for mod in chain:
				val %= mod
			assert l[val] == '.' or l[val] == ab[1]
			l[val] = ab[1]
			# print(f'{l=}')
		print(''.join(l))
		write_to_file(start_idx, ''.join(l), chain)



go_fuck_some_bitches()
