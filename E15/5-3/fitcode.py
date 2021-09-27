"""
CURVE_FIT functie voor practicum natuurkunde

Auteur: 	Bob Stienen
Datum:		16 februari 2019

--------------------------------------------------------------------------------

De functie in dit script kun je gebruiken om een formule aan je data te
fitten, waarbij je rekening houdt met zowel de onzekerheid in de x- als in de
y-coordinaat. Om de functie te laten werken moet je de volgende waardes sowieso
opgeven in de functie bij het aanroepen

	fit_function: function
		De functie je die wil fitten. Deze functie moet parameters aannemen
		in de vorm f(parameters, x), waarbij 'parameters' een 1-d array of lijst
		is van parameters die je wil fitten. Voor een polynoom van orde 1 zou
		dit bijvoorbeeld zijn:

			def func(params, x):
				return params[0]*x + params[1]

	x: numpy.ndarray
		Array met daarin de x-coordinaten van de punten waaraan je de functie
		wil fitten.

	y: numpy.ndarray
		Array met daarin de y-coordinaten van de punten waaraan je de functie
		wil fitten. Moet dezelfde lengte hebben als die je voor 'x' hebt
		opgegeven.

	sigma_x: numpy.ndarray
		Array met daarin de onzekerheden (1-sigma) op de x-coordinaten. Deze
		array moet daarom dezelfde lengte hebben als de array die je voor 'x'
		hebt opgegeven.

	sigma_y: numpy.ndarray
		Array met daarin de onzekerheden (1-sigma) op de y-coordinaten. Deze
		array moet daarom dezelfde lengte hebben als de array die je voor 'y'
		hebt opgegeven.

	estimate: list
		Lijst met dezelfde lengte als het aantal vrije parameters ('params' in
		de functie hierboven). De entries in deze lijst zijn je initiele gok
		voor de waardes van de vrije parameters.


Daarnaast heeft de functie ook een aantal optionele parameters:

	maxit: integer[default=10000]
		De fit-methode die hier wordt gebruikt is iteratief: het probeert de
		beste waardes voor je vrije parameters meer en meer te benaderen. Om
		oneindige lussen te voorkomen, kun je de maximale iteraties om te
		proberen instellen. Als dit maximum is bereikt stopt het zoeken sowieso.

	print_result: boolean[default=False]
		Als je deze op True zet, wordt fit informatie weergegeven in je shell


De functie voert drie variabelen uit:

	optimaal: np.ndarray
		De beste waardes die uit de fit zijn gekomen voor je vrije parameters

	sigma: np.ndarray
		Standaard deviaties op de beste fit waardes

	geconvergeerd: boolean
		Boolean die aangeeft of de fit is geconvergeerd. Als dit False is,
		overweeg van of je estimate bij te stellen, of om maxit te verhogen.

--------------------------------------------------------------------------------

Om dit script te kunnen gebruiken moet je het in dezelfde map plaatsen als de
code waarin je het wil gebruiken. Vervolgens voeg je de volgende regel bovenaan
je eigen code toe:

	from fitcode import curve_fit

Nu kun je de curve_fit functie hieronder in je eigen code gebruiken! Een
voorbeeld code zou bijvoorbeeld zijn (ervan uit gaande dat de arrays x, y,
dx en dy zijn gedefinieerd in het stuk code aangegeven met ..., net zoals
de functie f die je wil fitten):

	from fitcode import curve_fit
	import matplotlib.pyplot as plt
	import numpy as np

	...

	# Fit functie aan data
	param, param_sigma, conv = curve_fit(f, x, y, dx, dy, [0,0])

	# Controleer of fit is geconvergeerd
	if not conv:
		# Geen convergentie, print foutmelding zodat ik weet dat ik dingen moet
		# bijstellen
		print("!!! Fit is niet geconvergeerd !!!")

	# Maak plot van fit
	curve_x = np.linspace(np.amin(x), np.amax(x), 1000)
	plt.errorbar(x, y, xerr=dx, yerr=dy, fmt='o')
	plt.plot(curve_x, f(param, curve_x))
	plt.show()

--------------------------------------------------------------------------------

De code die het werkelijke fitten doet is niet door ons geschreven, maar is
beschikbaar via scipy. Mocht je dus NOG meer functionaliteiten nodig hebben dan
beschikbaar is via de parameters van de curve_fit functie hieronder, dan kun
je altijd in de documentatie kijken

	https://docs.scipy.org/doc/scipy/reference/odr.html

of Google / Duckduckgo erop na slaan. """

from scipy import odr

def curve_fit(fit_function, x, y, sigma_x, sigma_y, estimate,
			  maxit=10000, print_result=False):
	# Definieer een model om te fitten op basis van je functie
	model = odr.Model(fit_function)
	# Definieer een dataset, welke automatisch op de juiste manier zal worden
	# gewogen op basis van de onzekerheden die je hebt gegeven
	data = odr.RealData(x, y, sigma_x, sigma_y)
	# Creeer de analyse met het model en data. Hier moet ook een schatting
	# worden gegeven voor de vrije parameters en het aantal iteraties dat
	# maximaal moet worden doorlopen om een goede fit te vinden
	analyse = odr.ODR(data, model, beta0=estimate, maxit=maxit)
	# Draai de analyse om de beste fit waardes te vinden
	resultaat = analyse.run()
	# Controleren waarom de fit stopte. Als er iets onverwachts gebeurde of
	# de fit is niet geconvergeerd, stop het script en output een foutmelding
	if resultaat.info <= 3:
		# De fit is goed geconvergeerd
		pass
	elif resultaat.info > 4:
		# Resultaten worden betwijfeld of fatale fouten
		raise Exception("De fit is mislukt omdat de resultaten betwijfeld "
						"worden or omdat er fatale fouten optraden. Controleer "
						"je code op fouten.")
	# Print het resultaat als de gebruiker daarom heeft gevraagd
	if print_result:
		resultaat.pprint()
	# Return de beste fitwaardes en de standaard deviaties op deze waardes
	return resultaat.beta, resultaat.sd_beta, resultaat.info != 4
