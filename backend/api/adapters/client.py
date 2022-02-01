import requests
class Client:
    CLIENT_ID = "ALECV5CBBEHRRKTIQ5ZV143YEXOH3SBLAMU54SPHKGZI1ZKE"
    CLIENT_SECRET = "3JX3NRGRS2P0KE0NSKPTMCOZOY4MWUU4M3G33BO4XTRJ15SM"
    DATE = "20190407"
    URL = "https://api.foursquare.com/v2/venues/search"
    SHOW_URL = "https://api.foursquare.com/v2/venues"

    def auth_params(self):
        return {'client_id': self.CLIENT_ID,
                   'client_secret': self.CLIENT_SECRET,
                   'v': self.DATE}

    def full_params(self, query_params = {'ll': "40.7,-74", "query": "tacos"}):
        params = self.auth_params().copy()
        params.update(query_params)
        return params

    def request_venues(self):
        response = requests.get(self.URL, self.full_params())
        return response.json()['response']['venues']

    def request_venue(self, venue_id):
        response = requests.get(f"{self.SHOW_URL}/{venue_id}", self.auth_params())
        return response.json()['response']['venue']

# class RequestAndBuild:
#     def __init__(self):
#         self.client = adapters.Client()
#         self.builder = adapters.Builder()
#         self.conn = db.conn
#         self.cursor = self.conn.cursor()


#     def run(self, ll, query):
#         search_params = {'ll': f"{ll}", "query": query}
#         venues = self.client.request_venues(search_params)
#         venue_foursquare_ids = [venue['id'] for venue in venues]
#         venue_objs = []
#         for foursquare_id in venue_foursquare_ids:
#             venue_details = self.client.request_venue(foursquare_id)
#             venue_obj = self.builder.run(venue_details, self.conn, self.cursor)
#             venue_objs.append(venue_obj)
#         return venue_objs
