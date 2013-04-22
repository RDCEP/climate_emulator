import re
import numpy as np
from map import GEO_MAP, REGIONS, ANTARCTICA, anarctic_ocean1
from shapely.geometry import Polygon, MultiPolygon
from shapely.geometry.polygon import LinearRing
from shapely.geometry import mapping
from shapely.validation import explain_validity
from shapely.geometry import  shape
from shapely.ops import cascaded_union

countries = []
for feature in GEO_MAP['features']:
    name = feature['properties']['name']
    geometry = feature['geometry']
    thisshape = shape(geometry)
    try:
        thisshape = cascaded_union(thisshape)
    except TypeError:
        pass
    countries.append(thisshape)
MAP = cascaded_union(countries)

def make_region_box(minx, miny, maxx, maxy, p=False):
    print minx,miny,maxx,maxy
    X = list(np.arange(minx, maxx, 6))
    if X[len(X)-1] != maxx:
        X.append(maxx)
    polygon = []
    for x in X:
        polygon.append([x, miny])
    X.reverse()
    for x in X:
        polygon.append([x, maxy])
    return polygon

def write_map(map):
    with open('../static/js/geo.json', 'w') as f:
        f.write('{"type":"FeatureCollection","features":[\n')
        m = str(mapping(map))
        m = re.sub(r'\),\)', '))', m)
        m = re.sub(r'\)', ']', m)
        m = re.sub(r'\(', '[', m)
        m = re.sub(r'\'', '"', m)
        f.write('%s\n' % m)
        f.write(']}')

def ant_ocean(ocean,land):
    print ocean, land
    intersection = ocean.difference(land)
    return intersection

def write_regions():
    landregions = []
    with open('../static/js/geo.json', 'w') as f:
        f.write('{"type":"FeatureCollection","features":[\n')
        #    REGIONS = REGIONS[0:24]

        for i in range(len(REGIONS)):
            region = REGIONS[i]
            minx = region[2]
            miny = region[0]
            maxx = region[3]
            maxy = region[1]
            if minx == 0 and maxx == 360:
                minx = -180.
                maxx = 180.
            else:
                if minx > 180:
                    minx -= 360.
                if maxx > 180:
                    maxx -= 360.
                #            if i > 24 and miny == -90:
                #                if minx > maxx:
                #                    poly = make_region_box(minx, miny, maxx, maxy)
                #                print poly[0:-2]
                #                thisregion = Polygon(poly[0:-1])
                #                print thisregion.is_ring
                #                print explain_validity(thisregion)
                #            elif minx > maxx:
            if minx > maxx:
                poly1 = make_region_box(-180, miny, maxx, maxy)
                poly2 = make_region_box(minx, miny, 180, maxy)
                print poly1, poly2
                thisregion = MultiPolygon([
                    Polygon(poly1),
                    Polygon(poly2),
                    ])
            else:
                polygon = make_region_box(minx, miny, maxx, maxy)
                thisregion = Polygon(polygon)

            if i < 23:
                intersection = MAP.intersection(thisregion)
                try:
                    landregions.append(cascaded_union(intersection))
                except:
                    landregions.append(intersection)
            else:
                if i == 23:
                    landregions = cascaded_union(landregions)
                intersection = thisregion.difference(landregions)
                if i == 46:
                    intersection = MAP.intersection(thisregion)

            m = str(mapping(intersection))
            m = re.sub(r'\),\)', '))', m)
            m = re.sub(r'\)', ']', m)
            m = re.sub(r'\(', '[', m)
            m = re.sub(r'\'', '"', m)
            if i < 23 or i == 46:
                f.write('{"type":"Feature","properties":{"class":"land"},"geometry":')
            else:
                f.write('{"type":"Feature","properties":{"class":"water"},"geometry":')
            if i != len(REGIONS)-1:
                f.write('%s},\n' % m)
            else:
                f.write('%s}\n' % m)
            #                f.write('%s},\n' % m)
            #        m = str(mapping(ant_ocean(shape(anarctic_ocean1), landregions)))
            #        m = re.sub(r'\),\)', '))', m)
            #        m = re.sub(r'\)', ']', m)
            #        m = re.sub(r'\(', '[', m)
            #        m = re.sub(r'\'', '"', m)
            #        f.write('{"type":"Feature","properties":{"class":"water"},"geometry":')
            #        f.write('%s},\n' % m)
            #
            #        f.write('%s}\n' % m)
        f.write(']}')
    return landregions

lr = write_regions()
#write_map(lr)
#write_map(MAP)

#a = make_region_box(-180, -90, 180, -50)
#b = Polygon(a.reverse())
#print a
#print explain_validity(b), b
#print explain_validity(shape(ANTARCTICA))
#print b.intersection(shape(ANTARCTICA))