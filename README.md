#Adjust API
Django API - Adjust data set

A single API endpoint - '/api/v1/metrics/' to handle all client requests for adjust dataset.

Operations supported:
    * Filtering based on column values
    * Group By and Aggregation
    * Sort by multiple columns
    * Derived metric - CPI
    
## Setup and Dependencies
    -Python3, Django, djangorestframework and default Sqlite.
    
    -Steps: 
        1. Clone the repository
        2. pip install -r requirements.txt
    
        Start the server by executing manage.py from the root directory
        ~/adjust$ python manage.py runserver 0.0.0.0:8000
        
        Use browser and submit requests:
        *Parameters:
            fields:     A comma separated list of column names to be returned
            date_from:  date based filtering, start of the range(eg.2017-05-21)
            date_to:    date based filtering, End of the range
            group_by:   Comma separated list of column names to group
            sum_fields: Comma separated list of column names to aggregate over
            sort_by:    Comma separated list of comuns names for sorting. Precede with - for descending(e.g: -spend)
            
            any valid "column=value" can be given for filtering as well
            
            Example Requests:
            1. http://localhost:8000/api/v1/metrics/custom?fields=channel,country&date_to=2017-06-1&group_by=channel,country&sum_fields=impressions,clicks&sort_by=-clicks
            
Sample Output:
```            
GET /api/v1/metrics/custom?fields=channel,country&date_to=2017-06-1&group_by=channel,country&sum_fields=impressions,clicks&sort_by=-clicks
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "channel": "adcolony",
        "country": "US",
        "aggr_impressions": 552495,
        "aggr_clicks": 13583
    },
    {
        "channel": "apple_search_ads",
        "country": "US",
        "aggr_impressions": 369993,
        "aggr_clicks": 11457
    },
    {
        "channel": "vungle",
        "country": "GB",
        "aggr_impressions": 266470,
        "aggr_clicks": 9430
    },
    .
    .
    .
  ```  
    
    
    
    
    
    
