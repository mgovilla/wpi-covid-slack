import requests as r
import json

if __name__ == "__main__":
    savepng()

def savepng():
    out = open("out.png", "wb")
    img = r.get("https://public.tableau.com/static/images/WP/WPICommunityDashboard/DailyReport/1.png?height=727&width=1000&deviceScaleFactor=1")
    out.write(img.content)
    out.close()