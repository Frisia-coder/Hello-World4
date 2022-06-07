# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# part 1 Greet tamplate

def greet(name='stranger', template='Hello, <name>!'):
    return template.replace('<name>', name)

print(greet('Bob', 'What’s up, <name>!'))
print(greet('Bob'))
print(greet())

# part 2 Force

def force(mass=0, body='earth'):

    bodies = {
        'sun': 274,
        'mercury': 3.7,
        'venus': 8.9,
        'earth': 9.8,
        'moon': 1.6,
        'mars': 3.7,
        'jupiter': 24.9,
        'saturn': 10.4,
        'neptune': 11.2,
        'uranus': 8.9,
        'pluto' : 0.6,
        }

    return round(mass * bodies[body], 1)

print(force(10, 'mercury'))
print(force(0.123, 'pluto'))

# part 3 Gravity

def pull(m1, m2, d):
    G = 6.674 * (10 ** -11)
    pull = G * ((m1 * m2) / (d ** 2))
    return pull


if __name__ == '__main__':

  print(pull(0.1, 5.972*10**24, 6371))  