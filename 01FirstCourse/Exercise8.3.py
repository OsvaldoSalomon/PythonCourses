prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter not in 'OQ':
        print(letter + suffix)
    else:
        print(letter + 'u' + suffix)

# Jack
# Kack
# Lack
# Mack
# Nack
# Ouack
# Pack
# Quack
name = 'OsvaldoSalomon'
name[:7]
'Osvaldo'
name[7:]
'Salomon'
name[0:-5]
'OsvaldoSa'
name[0:-7]
'Osvaldo'
