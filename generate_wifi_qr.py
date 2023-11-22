import wifi_qrcode_generator

from utils.cmd_color_codes import *
from utils.wifi_info import get_wifi_list, get_wifi_password


def get_qr(wifi_profile, wifi_password):
    try:
        print(f"\n{SUCCESS}{BOLD}Generating WIFI QR Code ...{END}")
        # generate Qr code
        qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
            ssid=wifi_profile,
            hidden=False,
            authentication_type="WPA",
            password=wifi_password,
        )
        qr_code.print_ascii()
        qr_code.make_image().save("wifi_qr.png")
        print(f"{SUCCESS}WIFI Name: {END}", wifi_profile)
        print(f"{SUCCESS}WIFI PASSWORD: {END}", wifi_password)

        print(f"\n{SUCCESS}-------------------------")
        print(f"[+] {BOLD}QR CODE GENERATED !!")
        print(f"-------------------------{END}")
    except Exception as e:
        print(f"\n{FAILURE}-------------------------")
        print(f"[+] {BOLD}QR GENERATION FAILED !!", e)
        print(f"-------------------------{END}")


def generate_qr_for_already_connected_network(wifi_profile):
    print(f"{SUCCESS}WIFI Name: {END}", wifi_profile)
    wifi_password = get_wifi_password(wifi_profile)
    print(f"{SUCCESS}WIFI PASSWORD: {END}", wifi_password)

    if wifi_password == "":
        print(f"\n{FAILURE}WIFI seem to have no password !{END}")
        wifi_password = input(
            f"{SUCCESS}{BOLD}Please enter a password for the WIFI - '{wifi_profile}' : {END}"
        )
    get_qr(wifi_profile, wifi_password)


def generate_qr_for_new_network():
    wifi_profile = input(f"{SUCCESS} Enter WIFI Name: {END}")
    wifi_password = input(f"{SUCCESS} Enter WIFI Password: {END}")
    get_qr(wifi_profile, wifi_password)


def main():
    print(
        f"""{SUCCESS}{BOLD}
=============================
----- WIFI QR GENERATOR -----
============================={END}"""
    )
    wifi_list = get_wifi_list()
    wifi_list.append("Generate QR for a new WIFI Network.")

    if len(wifi_list) != 0:
        print(f"\n{SUCCESS} Available WIFI:{END}")
        for i in range(len(wifi_list)):
            print(f"  {i+1} - {wifi_list[i]}")
        user_input = int(
            input(f"\n{SUCCESS}Choose a WIFI network to genrate QR :{END} ")
        )

        if user_input == len(wifi_list):
            generate_qr_for_new_network()
        else:
            generate_qr_for_already_connected_network(wifi_list[user_input - 1])
    else:
        generate_qr_for_new_network()
    print("")


if __name__ == "__main__":
    main()
