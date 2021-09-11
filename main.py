import phonenumbers
from phone_track import number
from phonenumbers import geocoder
from phonenumbers import carrier


def NumberServiceProvider():
    # get number || "CH" -> Country + History of number"
    get_number = phonenumbers.parse(number, "CH")

    # get country of number || "en" -> english language
    get_country_num = geocoder.description_for_number(get_number, "en")
    print("Country of Number : ", get_country_num)

    # get service provider of number || "RO" service provider
    get_service_provider = phonenumbers.parse(number, "RO")

    service_provider = carrier.name_for_number(get_service_provider, "en")
    print("Service Provider : ", service_provider)


def Main():
    NumberServiceProvider()
    print("Running")


if __name__ == "__main__":

    Main()
