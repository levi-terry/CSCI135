triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
triangle_str = ''

print('')
for i in range(triangle_height):
    triangle_str = triangle_str + triangle_char
    print('%s' % triangle_str)
