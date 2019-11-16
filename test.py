import airbnb
import json
import re

NEGATIVE_RATING_COMMENTS=["terrible", "awful", "never again"]

api = airbnb.Api()
#json_data = json.dumps(api.get_homes("Boston, Massachusetts", offset=8, items_per_grid=8), indent=2)

with open("output.json", "r") as read_file:
    json_data = json.load(read_file)

for tab in json_data["explore_tabs"]:
  for section in tab["sections"]:
    for listing in section["listings"]:
      for key, value in listing.items():
        if key == "listing":
          print("Listing ID: {0} Review Count: {1}".format(value["id"], value["reviews_count"]))
          json_reviews = api.get_reviews(value["id"], offset=0, limit=20)
          for review in json_reviews["reviews"]:
            for pattern in NEGATIVE_RATING_COMMENTS:
              if re.search(pattern, review["comments"].lower()):
                print("Comment: {0}".format(review["comments"]))
                quit()
