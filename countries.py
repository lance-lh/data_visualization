# from pygal.i18n import COUNTRIES # module has been renamed
from pygal_maps_world.i18n import COUNTRIES
'''
COUNTRIES is a dict, which includes keys and values.
key: country code
value: country name
'''


for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])