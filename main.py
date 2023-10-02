from datetime import datetime

current_time = datetime.utcnow()

readme = f"""
⏰ Updated on {current_time.strftime("%a, %d %b %Y %H:%M:%S UTC")}
"""

print(readme)
