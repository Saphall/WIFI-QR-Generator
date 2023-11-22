import subprocess

from utils.cmd_color_codes import *


def get_wifi_list():
    """
    Returns list of already connected WIFI networks in device. Else returns empty list.
    """
    wifi_list = []
    try:
        wifi_profiles = (
            subprocess.check_output(["netsh", "wlan", "show", "profiles"])
            .decode("utf-8")
            .split("User profiles")[1]
            .split("All User Profile")
        )

        for wifi in wifi_profiles:
            wifi_list.append(wifi.replace(":", "").strip())
        wifi_list.pop(0)

    except Exception as e:
        print(f"{FAILURE}Something went wrong ...{END}", e)

    return wifi_list


def get_wifi_password(wifi_profile):
    """
    Returns WIFI password for wifi_profile already connected in device. Else return empty string.
    """
    wifi_password = ""
    try:
        wifi_password_info = (
            subprocess.check_output(
                ["netsh", "wlan", "show", "profile", wifi_profile, "key=clear"]
            )
            .decode("utf-8")
            .split("\n")
        )
        wifi_password = str(
            [b.split(":")[1][1:-1] for b in wifi_password_info if "Key Content" in b]
        )[2:-2]
    except:
        print(f"{FAILURE}WIFI may not be connected in device.{END}")

    return wifi_password
