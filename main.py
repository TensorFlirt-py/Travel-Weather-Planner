distance_mi = 8
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

# Conditional logic to check whether commuting is possible
if not distance_mi:  # Checking falsy value (0 or 0.0)
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
