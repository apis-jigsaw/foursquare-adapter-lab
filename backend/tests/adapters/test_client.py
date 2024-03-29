from api.adapters.client import Client

# Here we'll test our Client class.  This class is responsible for making a 
# request to the foursquare api.  It has the following features.

# 1. Class variables of CLIENT_ID, CLIENT_SECRET, 
# DATE (for the version required in the api), and URL for the root url.

# The first set of tests below check for this.  Get them passing.

def test_client_created_with_client_id():
    client = Client()
    assert isinstance(client.CLIENT_ID, str) == True, 'CLIENT_ID is not a string'

def test_client_created_with_client_secret():
    client = Client()
    assert isinstance(client.CLIENT_SECRET, str) == True, 'CLIENT_SECRET is not a string'

def test_client_created_with_date():
    client = Client()
    assert isinstance(client.DATE, str) == True, 'DATE is not a string'

def test_client_created_with_url():
    client = Client()
    assert client.URL == "https://api.foursquare.com/v2/venues/search"


# 2. Then lets work towards combining this authentication data in a dictionary.  
# Write a function called auth_params() that returns a dictionary 
# with keys of `client_id`, `client_secret`, and `v`, and values of
# the client_id defined as a class variable, the client secret, and `v` 
# can correspond to a date eg. '20190407'
# Reference the class variables in doing so.

def test_auth_params_returns_dictionary_of_client_id_secret_and_v():
    client = Client()
    assert list(client.auth_params().keys()) == ['client_id', 'client_secret', 'v']
    assert list(client.auth_params().values())[:2] == ['ALECV5CBBEHRRKTIQ5ZV143YEXOH3SBLAMU54SPHKGZI1ZKE', '3JX3NRGRS2P0KE0NSKPTMCOZOY4MWUU4M3G33BO4XTRJ15SM']


# 3. Now we want to combine these auth_params with our query params so that we can search the api
# Write a function called full params that can be passed some query params, and combine these query params
# With the auth_params.  For example, notice in the test below that we combine the auth_params from above.

def test_full_params_returns_dictionary_of_auth_params_combined_with_additional_query_params():
    client = Client()
    assert list(client.full_params(query_params = {'ll': '40.7,-74', 'query': 'tacos'}).keys()) == ['client_id', 'client_secret', 'v', 'll', 'query']

# 4. Then, we should be able to use these full params to make a request
# to the api.  Below we check that we get back the correct json, by checking that our 
# keys from the first dictionary match what is returned from the api.

def test_request_venues_makes_request_to_foursquare_api_with_url_and_full_params():
    client = Client()
    first_venue_returned = client.request_venues()[0]
    sorted_venue_keys = list(sorted(list(first_venue_returned.keys())))
    assert sorted_venue_keys == ['categories', 'createdAt', 'delivery', 'id', 'location', 'name']
                                 

# 5. Now it turns out that we can get even more information on a venue if we access the show route of 
# /venues/venue_id.  And we get the list of venue ids once we request all of the venues like we did above.

# So now, write a function called `request_venue` that takes in a venue_id 
# and returns the data about that particular venue by querying 
# the show route: /venues/venue_id.  
# Make sure to pass in the authentication params with your request
# A sample venue id is the following: '5b2932a0f5e9d70039787cf2'
def test_request_venue():
    client = Client()
    venue_id = '5b2932a0f5e9d70039787cf2'
    venue_details = client.request_venue(venue_id)
    sorted_venue_detail_keys = list(sorted(list(venue_details.keys())))
    
    sorted_venue_detail_keys == ['allowMenuUrlEdit', 'attributes', 'beenHere',
                           'bestPhoto', 'canonicalUrl', 'categories',
                             'contact', 'createdAt', 'defaultHours',
                               'delivery', 'dislike', 'hereNow', 'hours',
                           'id', 'inbox', 'likes', 'listed',
                             'location', 'name', 'ok', 'pageUpdates',
                               'photos', 'phrases', 'popular', 'price',
                                 'rating', 'ratingColor', 'ratingSignals',
                                   'reasons', 'seasonalHours', 'shortUrl',
                                     'stats', 'timeZone', 'tips', 'url', 'verified']