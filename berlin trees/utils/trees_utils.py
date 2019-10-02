# helper functions to explore the Berlin trees api data
from treesapiwrapper import treesWrapper

# I probably need to instantiate the api object



# pull all trees into a geodataframe 
def allTreesToGDF():

    # set starting page 
    page = 26865

    # create empty arrays to be used to create dataframe   
    ids = []
    age = []
    borough = []
    circumference = []
    genus = []
    height = []
    species = []
    year = []
    lat = []
    long = []

    print("Retrieving all trees from endpoint and inserting into dataframe")

    # loop over all pages in the endpoint and append values to arrays
    while True:
        this_page = api.get_trees(page=page).json()
        next_page = this_page["next"]
        for row in range(len(this_page['features'])):
            ids.append(this_page['features'][row]['id'])
            age.append(this_page['features'][row]['properties']['age'])
            borough.append(this_page['features'][row]['properties']['borough'])
            circumference.append(this_page['features'][row]['properties']['circumference'])
            genus.append(this_page['features'][row]['properties']['genus'])
            height.append(this_page['features'][row]['properties']['height'])
            species.append(this_page['features'][row]['properties']['species'])
            year.append(this_page['features'][row]['properties']['year'])        
            lat.append(this_page['features'][row]['geometry']['coordinates'][0])
            long.append(this_page['features'][row]['geometry']['coordinates'][1])        
            
        page = page + 1

        # for debugging, can be removed at some point
        print(page)
        
        if(next_page) is None:
            break

    # create dataframe from resulting arrays       
    df = pd.DataFrame(
        {'id': ids,
        'age' : age,
        'borough' : borough,
        'circumference' : circumference,
        'genus' : genus,
        'height' : height,
        'species' : species,
        'year': year,
        'Latitude': lat,
        'Longitude': long})
    
    # convert to geodataframe
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude)) 

    return(gdf)