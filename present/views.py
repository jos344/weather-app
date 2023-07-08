from django.shortcuts import render

def home(request):
    import json
    import requests
    

    #grab data
    api_request = requests.get("https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.676757/lat/59.37351/data.json")
    
    try:
        #parse into json
        api = json.loads(api_request.content)
        
    except Exception as e:
        api = "Error..."

    #Air temprature - t
    t = api['timeSeries'][0]['parameters'][0]['values'][0]
    
    #pcat - precipitation category
    pcat = api['timeSeries'][0]['parameters'][15]['values'][0]

    #weather symbol - wsyb2
    wsymb2 = api['timeSeries'][0]['parameters'][18]['values'][0]

    #check the precipitation category parameter
    if pcat == 0:
        pcat = 'No precipitation'
    elif pcat == 1:
        pcat = 'Snow'
    elif pcat == 2:
        pcat = 'Snow and rain'
    elif pcat == 3:
        pcat = 'Rain'
    elif pcat == 4:
        pcat = 'Drizzle'
    elif pcat == 5:
        pcat = 'Freezing rain'
    elif pcat == 6:
        pcat = 'Freezing drizzle'

    
    #check the Weather Symbol
    if wsymb2 == 1:
        wsymb2 = 'Clear Sky'
    elif wsymb2 == 2:
        wsymb2 = 'Nearly clear sky'
    elif wsymb2 == 3:
        wsymb2 = 'Variable clodiness'
    elif wsymb2 == 4:
        wsymb2 = 'Halfclear sky'
    elif wsymb2 == 5:
        wsymb2 = 'Cloudy sky'
    elif wsymb2 == 6:
        wsymb2 = 'Overcast'
    elif wsymb2 == 7:
        wsymb2 = 'Fog'
    elif wsymb2 == 8:
        wsymb2 = 'Light rain showers'
    elif wsymb2 == 9:
        wsymb2 = 'Moderate rain showers' 
    elif wsymb2 == 10:
        wsymb2 = 'Heavy rain showers'
    elif wsymb2 == 11:
        wsymb2 = 'Thunderstorm'
    elif wsymb2 == 12:
        wsymb2 = 'Light sleet showers'
    elif wsymb2 == 13:
        wsymb2 = 'Moderate sleet showers'
    elif wsymb2 == 14:
        wsymb2 = 'Heavy sleet showers'
    elif wsymb2 == 15:
        wsymb2 = 'Light snow showers'
    elif wsymb2 == 16:
        wsymb2 = 'Moderate snow showers'
    elif wsymb2 == 17:
        wsymb2 = 'Heavy snow showers'
    elif wsymb2 == 18:
        wsymb2 = 'Light rain'
    elif wsymb2 == 19:
        wsymb2 = 'Moderate rain'
    elif wsymb2 == 20:
        wsymb2 = 'Heavy rain'
    elif wsymb2 == 21:
        wsymb2 = 'Thunder'
    elif wsymb2 == 22:
        wsymb2 = 'Light sleet'
    elif wsymb2 == 23:
        wsymb2 = 'Moderate sleet'
    elif wsymb2 == 24:
        wsymb2 = 'Heavy sleet'
    elif wsymb2 == 25:
        wsymb2 = 'Light snowfall'
    elif wsymb2 == 26:
        wsymb2 = 'Moderate snowfall'
    elif wsymb2 == 27:
        wsymb2 = 'Heavy snowfall'




    return render(request, 'home.html', {
                                        'api': api,
                                        't': t, 
                                        'wsymb2': wsymb2,
                                        'pcat': pcat,
                                        })