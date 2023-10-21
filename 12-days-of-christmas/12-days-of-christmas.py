D=['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Ninth','Tenth','Eleventh','Twelfth']
G=['Twelve Drummers Drumming,','Eleven Pipers Piping,','Ten Lords-a-Leaping,','Nine Ladies Dancing,','Eight Maids-a-Milking,','Seven Swans-a-Swimming,','Six Geese-a-Laying,','Five Gold Rings,','Four Calling Birds,','Three French Hens,','Two Turtle Doves, and','A Partridge in a Pear Tree.']
print(*['\n'.join([f'On the {D[i]} day of Christmas','My true love sent to me',*G[11-i:]])for i in range(12)],sep='\n\n')
