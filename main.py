from astropy import units as u
from astropy.coordinates import get_body_barycentric, get_body, get_moon
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.time import Time
from datetime import datetime, timedelta
import arrow

start = Time.now()
print(start)
# end = start.shift(years=1)

loc = EarthLocation.from_geodetic(60.79574, 10.69155)
bodies = [
	"Moon",
	"Sun",
	"Mercury",
	"Venus",
	"Mars",
	"Jupiter",
	"Saturn",
	"Uranus",
	"Neptune",
	"Pluto",
]

with solar_system_ephemeris.set("de432s"):
	for body_name in bodies:
		body = get_body(body_name, start, loc)
		# print(f"{body_name}: {body.distance}")
		distance_in_light_years = (body.distance).to(u.lightyear).value
		lm = (1 * u.year).to(u.minute).value
		distance_in_light_minutes = distance_in_light_years * lm

		print(f"{body_name}: {distance_in_light_minutes} light minutes")


# for r in arrow.Arrow.span_range("day", start, end):
# 	print(r)

# print(start)
# print(end)
