import time
from datetime import datetime

# Get the current time in seconds since January 1, 1970
current_time_seconds = time.time()

# Format the time in the required format
formatted_time = datetime.utcfromtimestamp(current_time_seconds).strftime('%b %d %Y')
scientific_notation = f"{current_time_seconds:.4e}"

# Print the results
print(f"Seconds since January 1, 1970: {current_time_seconds:,.4f} or in scientific notation: {scientific_notation}")
print(formatted_time)
