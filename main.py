import sys
from pprint import pprint
from geopy.distance import great_circle as GC

from geocoder import get_coords
from map import get_img, show_map
from find_business import find_biz


def main():
    toponym_to_find = ' '.join(sys.argv[1:])
    if toponym_to_find:
        lat, lon = get_coords(toponym_to_find)
        res_find = find_biz(','.join((lat, lon)),
                 '0.005',
                 'Аптека')
        rast = GC(tuple(map(float, (lat, lon))), res_find[0]).m
        pprint(res_find)
        show_map(get_img(res_find[0], (lat, lon)), str(round(rast)), res_find[1], res_find[2], res_find[3])


if __name__ == '__main__':
    main()
