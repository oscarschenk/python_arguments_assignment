# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name = 'piet', greeting_template = 'Hello, <name>!'):
    return greeting_template.replace('<name>', name)

def force(mass=0, body='earth'):

    bodies = {
        'sun': 274,
        'mercury': 3.7,
        'venus': 9.8,
        'earth': 9.798,
        'moon': 1.62,
        'mars': 3.71,
        'jupiter': 24.92,
        'saturn': 10.44,
        'neptune': 11.15,
        'uranus': 8.87,
        'pluto': 0.58
    }  # body: surface gravity

    return round(mass * bodies[body], 1)

def pull(m1, m2, d):
    G = 6.674 * (10 ** -11) 
    return G * ((m1 * m2) / (d ** 2)) 
