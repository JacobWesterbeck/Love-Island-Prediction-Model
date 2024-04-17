# Data Dictionary

The table below contains all data elements used in this project - note that only a handful of these were used for modeling, but all were used at some point in processing/analysis.

 
|      Term         |     Type     |                Definition                |
|-------------------|--------------|------------------------------------------|
|Name               |string        |   Contestants Name                       |
|Season             |category      |   Season Contestant Appears On           |
|Gender             |bool          |   Male Or Female Contestant              |        
|Age                |int64         |   Age Of Contestant Upon Entry           |        
|Height             |int64         |   Height Of Contestant In Inches         |        
|Ethnicity          |category      |   Contestant Ethnicity                   |        
|Hair               |category      |   Contestant Hair Color                  |        
|Eye                |category      |   Contestant Eye Color                   |        
|Hometown           |category      |   Name Of Contestants Hometown           |        
|Region             |category      |   Name Of Contestants Country            |       
|Entered            |int64         |   Day Contestant Enters Villa            |       
|Dumped             |int64         |   Day Contestant Leaves Villa            |      
|Stay               |int64         |   (Day Dumped - Day Entered)             |
|OG                 |category      |   Was Contestant An Original Cast Member |
|Casa               |category      |   Was Contestant A Casa Amor Entry       |
|Status             |category      |   A Candidates Placement 1-4 or Dumped   |
|Finalist           |bool          |   Did Candidate Reach Finale             |
|Unique Partners    |int64         |   Number Of Distinct Partners            |
|Loyalty Score      |float64       |   (Unique Partners / Length Of Stay)     |


## Data Sources
Contestant data relating to the show were taken from Love Island wiki pages: <br>
General Info: https://loveisland.fandom.com/wiki/Love_Island <br>
Season 1: https://loveisland.fandom.com/wiki/Love_Island_(Season_1) <br>
Season 2: https://loveisland.fandom.com/wiki/Love_Island_(Season_2) <br>
Season 3: https://loveisland.fandom.com/wiki/Love_Island_(Season_3) <br>
Season 4: https://loveisland.fandom.com/wiki/Love_Island_(Season_4) <br>
Season 5: https://loveisland.fandom.com/wiki/Love_Island_(Season_5) <br>
Season 6: https://loveisland.fandom.com/wiki/Love_Island_(Season_6) <br>
Season 7: https://loveisland.fandom.com/wiki/Love_Island_(Season_7) <br>
Season 8: https://loveisland.fandom.com/wiki/Love_Island_(Season_8) <br>
Season 9: https://loveisland.fandom.com/wiki/Love_Island_(Season_9) <br>



## Gathering of Physical Attributes:
- Hair Color and Eye Color were collected manually by referencing photos at the time of contestants' entry into the villa.
- Contestants were sorted into 4 categories identified by the UK Census Bureau.
- Height data was especially challenging to gather due to dispersed sources. 
    - Some contestant heights were revealed during the show itself. 
    - Other contestant heights were pulled from various sources including contestants' social media and online modeling profiles, as well as community input from the official Love Island Reddit.