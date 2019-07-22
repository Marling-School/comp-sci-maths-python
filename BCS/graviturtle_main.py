from turtle import done
from BCS.graviturtle import GraviTurtle, create_planet


moon = create_planet(color='grey')
earth = create_planet(color='blue')
sun = create_planet(color='orange')

gravity = GraviTurtle()
gravity.setup_orbit(sun, earth, radius=150)
gravity.setup_orbit(earth, moon, radius=30, frequency=4)

gravity.run()

done()
