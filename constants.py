# FlexMeasures constants

# This represents how often schedules should refresh. Keep at this setting.
FM_EVENT_RESOLUTION_IN_MINUTES = 5

# CONSTANTS for FM Url's
FM_BASE_URL = "https://flexmeasures.seita.nl/api/"
FM_API_VERSION = "v3_0"

# URL for authentication on FM
# https://flexmeasures.seita.nl/api/requestAuthToken
FM_AUTHENTICATION_URL = FM_BASE_URL + "requestAuthToken"

# URL for retreival of the schedules
# https://flexmeasures.seita.nl/api/v3_0/sensors/XX/schedules/trigger
# https://flexmeasures.seita.nl/api/v3_0/sensors/XX/schedules/SI
# Where XX is the sensor_id and SI is the schedule_id
FM_SCHEDULE_URL = FM_BASE_URL + FM_API_VERSION + "/sensors/"
FM_SCHEDULE_SLUG = "/schedules/"
FM_SCHEDULE_TRIGGER_SLUG = FM_SCHEDULE_SLUG + "trigger"

# URL for getting data for the chart:
# https://flexmeasures.seita.nl/api/dev/sensor/XX/chart_data/
# Where XX is the sensor_id
FM_GET_DATA_URL = FM_BASE_URL + "dev/sensor/"
FM_GET_DATA_SLUG = "/chart_data/"

# URL for sending metering data to FM:
# https://flexmeasures.seita.nl/api/v3_0/sensors/data
FM_SET_DATA_URL = FM_BASE_URL + FM_API_VERSION + "/sensors/data"

# Utility context
# The utility (or electricity provider) are represented by different sensor's.
# These sensor's determain to which signal the schedules are optimised.
# These are the also used for fetching data from FM to show in the graph.
# ToDo: change NextEnergy, EPEX NO and Emissions NO sensors
DEFAULT_UTILITY_CONTEXTS = {
    "nl_generic": {"consumption-sensor": 14, "production-sensor": 14, "emisions-sensor": 27, "display-name": "EPEX Day ahead NL"},
    "nl_anwb_energie": {"consumption-sensor": 60, "production-sensor": 71, "emisions-sensor": 27, "display-name": "ANWB Energie"},
    "nl_next_energy": {"consumption-sensor": 60, "production-sensor": 71, "emisions-sensor": 27, "display-name": "NextEnergy"},
    "nl_tibber": {"consumption-sensor": 58, "production-sensor": 70, "emisions-sensor": 27, "display-name": "Tibber"},
    "no_generic": {"consumption-sensor": 14, "production-sensor": 14, "emisions-sensor": 27,  "display-name": "EPEX Day ahead NO"}
}


# These are set by v2g_globals, should be moved there...
FM_PRICE_PRODUCTION_SENSOR_ID: int
FM_PRICE_CONSUMPTION_SENSOR_ID: int
FM_EMISSIONS_SENSOR_ID: int
UTILITY_CONTEXT_DISPLAY_NAME: str

# FM ACCOUNT CONSTANTS
# ToDo:
# These are set by v2g_globals, should be moved there...
# These don't have defaults. They should asap be over written by v2g_globals with value from secrets.yaml
FM_ACCOUNT_POWER_SENSOR_ID: int
FM_ACCOUNT_AVAILABILITY_SENSOR_ID: int
FM_ACCOUNT_SOC_SENSOR_ID: int


# CHARGER CONSTANTS
# ToDo:
# These are set by v2g_globals, should be moved there...
# Some have defaults here that should asap be over written by v2g_globals with value from secrets.yaml

# Defaults to 0.85
CHARGER_PLUS_CAR_ROUNDTRIP_EFFICIENCY: float = 0.85

# CAR CONSTANTS
# See remark for charger constants
# Defaults to 24 (to be safe)
CAR_MAX_CAPACITY_IN_KWH: int = 24
# For later PR
CAR_AVERAGE_WH_PER_KM: float = 174

# USER PREFRENCE CONSTANTS
# See remark for charger constants
# Defaults to 10 (to be safe)
CAR_MIN_SOC_IN_PERCENT: int = 10
# Defaults to 100 (to be safe)
CAR_MAX_SOC_IN_PERCENT: int = 100

OPTIMISATION_MODE: str = "price"
ELECTRICITY_PROVIDER: str = "nl_generic"