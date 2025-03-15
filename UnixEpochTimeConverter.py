from datetime import datetime, timezone, timedelta

def print_current_epoch_and_gmt_plus2():
    epoch_time = int(datetime.now().timestamp())  # Current epoch time
    gmt_plus2 = timezone(timedelta(hours=2))  # Define GMT+2 timezone
    converted_time = datetime.fromtimestamp(epoch_time, tz=gmt_plus2)  # Convert to GMT+2

    print(f"Current Epoch Time: {epoch_time}")
    print(f"Converted GMT+2 Time: {converted_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

print_current_epoch_and_gmt_plus2()