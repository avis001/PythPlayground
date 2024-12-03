def check_mount_rental(time_used, time_puchased):
    if time_used > time_puchased:
        return "overtime charged"
    return "no charges yet"
