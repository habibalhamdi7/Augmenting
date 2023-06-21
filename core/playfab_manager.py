# playfab_manager.py
from playfab import PlayFabClientAPI
from playfab import PlayFabSettings

def get_playfab_client():
    title_id = '84061'
    secret_key = 'PRRDKWIFQKWNEUQ3UCSADCDPDUKY6OU8QFETMJTIDUJ78OWMG9'
    use_https = False  # Set False jika tidak menggunakan HTTPS

    PlayFabSettings.TitleId = title_id
    PlayFabSettings.DeveloperSecretKey = secret_key
    PlayFabSettings.RequestGetParams = {'SdkVersion': '0.0.1'}

    return PlayFabClientAPI()