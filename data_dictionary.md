### Data Dictionary
Name - First and last name of the contestants TYPE: String
Season - Specifies which season the contestant appeared on 
Gender - Male/Female 
Age - Age at the time of entry
Height - Contestant height in inches
Race - White/Black/Asian/MENAT
Hair Color - Hair color at time of show Black/Brown/Blone/Red
Eye Color - Contestants eye color
Hometown - Contestants hometown
Region - Region of UK the contestants hometown is in
Day Entered - Day the contestant entered the villa
Day Dumped - Day the contestant exited the villa
Length Of Stay - Day Dumped minus Day Entered
Original Cast - Was the contestant a Day One cast member? T/F
Casa Amor Addition - Was the contestant a Casa Amor entry? T/F
Status - Did the islander place in the top 4 or were they dumped before the finale.
Unique Partners - How many distinct couples was the islander in while on the show.
Loyalty Score - Unique Partners divided by Length of Stay

## Data Sources
Contestant data relating to the show were taken from Love Island wiki pages:
General Info: https://loveisland.fandom.com/wiki/Love_Island
Season 1: https://loveisland.fandom.com/wiki/Love_Island_(Season_1)
Season 2: https://loveisland.fandom.com/wiki/Love_Island_(Season_2)
Season 3: https://loveisland.fandom.com/wiki/Love_Island_(Season_3)
Season 4: https://loveisland.fandom.com/wiki/Love_Island_(Season_4)
Season 5: https://loveisland.fandom.com/wiki/Love_Island_(Season_5)
Season 6: https://loveisland.fandom.com/wiki/Love_Island_(Season_6)
Season 7: https://loveisland.fandom.com/wiki/Love_Island_(Season_7)
Season 8: https://loveisland.fandom.com/wiki/Love_Island_(Season_8)
Season 9: https://loveisland.fandom.com/wiki/Love_Island_(Season_9)



# Data Type
Name - Object
Season - Int
Gender - Categorical
Age - Int
Height - Int
Race - Categorical
Hair Color - Categorical
Eye Color - Categorical
Hometown - Object
Region - Categorical
Day Entered - Int
Day Dumped - Int
Length Of Stay - Int
Original Cast - Categorical
Casa Amor Addition - Categorical
Status - Categorical
Unique Partners - Int
Loyalty Score - Int


Gathering Physical Attributes:
- Physically-oriented data (Gender, Hair Color, Eye Color) was collected manually by referencing photos at the time of contestants' entry into the villa.
- Height data was especially challenging to gather due to dispersed sources. Efforts were made to obtain accurate heights from various sources, including contestants' social media, online modeling profiles, and community input from the official Love Island Reddit.
- For missing heights, estimation was performed based on known heights to achieve the closest approximation possible. Any height minor inaccuracies for a small subset of contestants should have a negligible effect on this model.

# Data Dictionary

Data Dictionary

|Term  | Definition                       | Type   |
|------|----------------------------------|--------|
|Name  | Contestants Name                 | Object |
|Age   | Contesants age on day of entry   | Int    |
|      |                                  |        |
|      |                                  |        |
