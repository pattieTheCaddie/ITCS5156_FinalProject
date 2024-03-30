from homeharvest import scrape_property
from datetime import datetime

current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#filename = f"HomeHarvest_{current_timestamp}.csv"
filename = "HomeHarvest_2023_10_Miles_From_Home.csv"

properties = scrape_property(
  location="701 Royal Ct,Apt 304,Charlotte,NC",
  radius=10,
  #location="Charlotte, NC",  

  listing_type="sold",  # or (for_sale, for_rent, pending)
  #past_days=10,  # sold in last 30 days - listed in last 30 days if (for_sale, for_rent)
  
  date_from="2020-01-01", # alternative to past_days 
  date_to="2020-12-31", 
  foreclosure=False
  
  # mls_only=True,  # only fetch MLS listings
)
print(f"Number of properties: {len(properties)}")

properties.to_csv(filename, index=False)
print(properties.head())