from environs import Env

env = Env()
env.read_env()

# ENDPOINTS
V_1_0_API_BASE = env("FORMALOO_API_BASE", 'https://api.formaloo.net/v1.0/')

V_1_0_AUTHORIZATION_TOKEN_ENDPOINT = '%soauth2/authorization-token/' % V_1_0_API_BASE

V_1_0_CREATE_ACTIVITY_ENDPOINT = '%sactivities/' % V_1_0_API_BASE
V_1_0_ACTIVITY_BATCH_ENDPOINT = '%sactivities/batch/' % V_1_0_API_BASE

V_1_0_CREATE_CUSTOMER_ENDPOINT = '%scustomers/' % V_1_0_API_BASE
V_1_0_CUSTOMER_BATCH_ENDPOINT = '%scustomers/batch/' % V_1_0_API_BASE

# HEADERS
APPLICATION_HEADER = 'x-api-key'
AUTHORIZATION_HEADER = 'Authorization'
AUTHORIZATION_BEARER = 'JWT'
CREDENTIAL_BEARER = 'Basic'
CREDENTIAL_GRAT_TYPE = 'client_credentials'

# Settings
AUTHORIZATION_TOKEN_TIMEOUT = 5*60
