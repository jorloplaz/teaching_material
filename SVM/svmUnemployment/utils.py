###### Imports #######
import pandas as pd
import geopandas as gpd
import folium
import numpy as np

###### Constants ######

# Alternative names for communities
COM_EQUIVS = {
    'Asturias, Principado de': 'Asturias',
    'Balears, Illes': 'Islas Baleares',
    'Castilla y León': 'Castilla León',
    'Castilla - La Mancha': 'Castilla La Mancha',
    'Cataluña': 'Catalunya',
    'Comunitat Valenciana': 'Valencia',
    'Madrid, Comunidad de': 'Madrid',
    'Murcia, Región de': 'Murcia',
    'Navarra, Comunidad Foral de': 'Navarra',
    'Rioja, La': 'La Rioja'
}

# Alternative names for provinces
PROV_EQUIVS = {
    'Coruña, A': 'A Coruña',
    'Balears, Illes': 'Illes Balears',
    'Palmas, Las': 'Las Palmas',
    'Rioja, La': 'La Rioja',
    'Araba/Álava': 'Álava',
    'Gipuzkoa': 'Guipúzcoa',
    'Bizkaia': 'Vizcaya',
    'Valencia/Valéncia': 'Valencia/València'
}

# Alternative names for columns
MONTH_FIELD = 'mes' ; YEAR_FIELD = 'año' ; COM_FIELD = 'com_aut' ; PROV_FIELD = 'prov' ; MUN_FIELD = 'mun' ; UNEMPL_FIELD = 'parados'
COL_EQUIVS = {
    'Código mes ': MONTH_FIELD, 
    'Comunidad Autónoma': COM_FIELD,
    'Provincia': PROV_FIELD,
    ' Municipio': MUN_FIELD,
    'total Paro Registrado': UNEMPL_FIELD
}
LAT_FIELD = 'lat' ; LON_FIELD = 'lon' ; ALT_FIELD = 'alt' ; POPUL_FIELD = 'habitantes'
COL_EQUIVS2 = {
    'Comunidad': COM_FIELD,
    'Provincia': PROV_FIELD,
    'Población': MUN_FIELD,
    'Latitud': LAT_FIELD,
    'Longitud': LON_FIELD,
    'Altitud': ALT_FIELD,
    'Habitantes': POPUL_FIELD
}

# Geographic representation
CRS = {'init': 'epsg:4326'} ; TILES = 'cartodbpositron'

###### Functions ######

def read_unemployment(f, csv_params={'sep': ';', 'encoding': 'iso-8859-1', 'header': 1, 'usecols': list(COL_EQUIVS.keys())}):
    """
    Reads unemployment data from the file specified

    @param f: file to read
    @param csv_params: dictionary of parameters passed literally to pandas read_csv() function

    @return DataFrame with unemployment data
    """
    # Read unemployment data
    unemployment = pd.read_csv(f, **csv_params)
    # Rename columns
    unemployment.rename(columns=COL_EQUIVS, inplace=True)
    # Standardise community
    for k, v in COM_EQUIVS.items():
        ind = (unemployment[COM_FIELD].str.strip() == k)
        unemployment.loc[ind, COM_FIELD] = v
    # Standardise province
    for k, v in PROV_EQUIVS.items():
        ind = (unemployment[PROV_FIELD].str.strip() == k)
        unemployment.loc[ind, PROV_FIELD] = v
    # Obtain timestamps
    aux = pd.to_datetime(unemployment[MONTH_FIELD], format='%Y%m').dt     # strings have year (4 chars) and month (2 chars)
    # Split in month and year
    unemployment.loc[:, MONTH_FIELD] = aux.month ; unemployment.loc[:, YEAR_FIELD] = aux.year
    # Set index to (community, province, municipality), sort by columns and done
    return unemployment.set_index([COM_FIELD, PROV_FIELD, MUN_FIELD]).sort_index(axis=1)

def read_population(f, csv_params={'sep': ';', 'decimal': ',', 'header': 2, 'usecols': list(COL_EQUIVS2.keys())}):
    """
    Reads population data from the file specified

    @param f: file to read
    @param csv_params: dictionary of parameters passed literally to pandas read_csv() function

    @return DataFrame with population data
    """
    # Read population data
    pop = pd.read_csv(f, **csv_params)
    # Rename columns
    pop.rename(columns=COL_EQUIVS2, inplace=True)
    # Standardise municipalities: change towns like Ejido (El) to Ejido, El
    pop.loc[:, MUN_FIELD] = pop[MUN_FIELD].str.replace(' \(', ', ').str.replace('\)', '')
    # Set index to (community, province, municipality) and done
    return pop.set_index([COM_FIELD, PROV_FIELD, MUN_FIELD])

def read_communities(d):
    """
    Reads community shapes from the directory specified

    @param d: directory to read
    
    @return GeoDataFrame with community shapes
    """
    # Read communities
    coms = gpd.read_file(d).to_crs(CRS).rename(columns={'Texto_Alt': COM_FIELD})
    # Unify names
    for name1, name2 in [('Illes Balears', 'Islas Baleares'), ('Castilla y León', 'Castilla León'), 
                         ('Castilla - La Mancha', 'Castilla La Mancha'), ('Comunitat Valenciana', 'Valencia'), 
                         ('Nafarroa', 'Navarra'), ('Euskadi', 'País Vasco')]:
        coms.loc[coms[COM_FIELD] == name1, COM_FIELD] = name2
    # Done 
    return coms

def read_provinces(d):
    """
    Reads province shapes from the directory specified

    @param d: directory to read
    
    @return GeoDataFrame with province shapes
    """
    # Read provinces
    provs = gpd.read_file(d).to_crs(CRS).rename(columns={'Texto_Alt': PROV_FIELD})
    # Unify names
    for name1, name2 in [('Alicante', 'Alicante/Alacant'), ('Valencia', 'Valencia/València'), ('Castellón', 'Castellón/Castelló'), 
                         ('Islas Baleares', 'Illes Balears'), ('Orense', 'Ourense'), ('La Coruña', 'A Coruña'), 
                         ('Gerona', 'Girona'), ('Lérida', 'Lleida')]:
        provs.loc[provs[PROV_FIELD] == name1, PROV_FIELD] = name2 
    # Done
    return provs

def _plot_dot(point, unemploy_map, lat_col, long_col, unemploy_col, cmap, index_cols, radius=3, weight=1, color='black'):
    """Adds a circle in the map where a point is located. Fill color is set to the unemployment value."""
    folium.CircleMarker(location=[point[lat_col], point[long_col]], radius=radius, weight=weight, 
                        color=color, fill=True, fill_color=cmap(point[unemploy_col]), fill_opacity=0.9,
                        popup=folium.Popup(point[index_cols[-1]], parse_html=True)).add_to(unemploy_map)

def generate_map(data, lat_col, long_col, unemploy_col, cmap, coms=None, provs=None, filename=None, svs=None):
    """
    Creates an unemployment map from the data specified

    @param data: DataFrame with unemployment data
    @lat_col: latitude column in data
    @long_col: longitude column in data
    @unemploy_col: unemployment column in data
    @cmap: colormap to use for plotting
    @param coms: communities GeoDataFrame (None not to plot)
    @param provs: provinces GeoDataFrame (None not to plot)
    @param filename: where to save the map (HTML file, None not to save)
    
    @return Folium Map object plotting the unemployment data
    """
    # Verify columns
    if (lat_col not in data) or (long_col not in data) or (unemploy_col not in data):
        raise ValueError('Coordinates and unemployment columns must be present in data')
    # Create map
    unemploy_map = folium.Map(tiles=TILES)
    # Add colors
    cmap.add_to(unemploy_map)
    # Add communities
    if coms is not None:
        folium.GeoJson(coms.to_json(), style_function=lambda x: {
            'fillColor': 'none',
            'color': 'black',
            'weight': 3
        }).add_to(unemploy_map)
    # Add provinces
    if provs is not None:
        folium.GeoJson(provs.to_json(), style_function=lambda x: {
            'fillColor': 'none',
            'color': 'black',
            'weight': 1.5,
            'dashArray': '5, 5'
        }).add_to(unemploy_map)
    # Add data
    index_cols = data.index.names
    data.reset_index().apply(_plot_dot, axis=1, args=(unemploy_map, lat_col, long_col, unemploy_col, cmap, index_cols))
    # Adjust bounds
    unemploy_map.fit_bounds(unemploy_map.get_bounds())
    # Save if needed
    if filename is not None:
        unemploy_map.save(filename)
    # Done
    return unemploy_map


