import math, argparse, sys
from svgpathtools import Line, Path, wsvg

"""

Archimedean spiral generator for embroidered speaker coils.
You need svgpathtools to run this script. Install it via pip using this command:
pip install svgpathtools

Usage:
./spiral_generator.py [-h] -o <float> -i <float> -t <int> [-r] [-smin <float>] [-smax <float>] [-s]

Example:
./spiral_generator.py -t 78 -o 50 -i 11 -smin 2 -smax 4 -r -s


Optional arguments:
  -h, --help  show help message
  -t          number of turns <int>
  -oh         outer height <float>
  -ow         outer width <float>
  -iw         inner width <float>
  -smin       min stitch length, default = 2 <float>
  -smax       max stitch length, default = 2 <float>
  -r          reverse path direction from outward to inward
  -s          save to svg

Improvement suggestions:
thomas.preindl(at)fh-hagenberg.at

More:
http://mi-lab.org/sonoflex-embroidered-speakers/

"""


def spiral(OH, OW, IW, turns, reverse=False):
    distX = IW / 2  # current distance from center
    spacing = (OW / 2 - distX) / turns  # radius increase per full revolution
    IH = OH - 2 * turns * spacing
    distY = IH / 2  # spiral radius
    print("turns:\t\t", turns)
    print("outer width:\t", OW, "mm")
    print("outer height:\t", OH, "mm")
    print("inner width:\t", IW, "mm")
    print("inner height:\t", IH, "mm")
    print("turn spacing:\t", round(spacing, 4), "mm")

    coords = []
    # thetas = [0, math.pi/2, math.pi, 3*math.pi/2]
    thetas = [math.pi / 4, 3 * math.pi / 4, 5 * math.pi / 4, 7 * math.pi / 4]

    for i in range(turns):

        for theta in thetas:
            cord = [distX * math.cos(theta) / math.sin(math.pi / 4), distY * math.sin(theta) / math.sin(math.pi / 4)]
            coords.append(cord)

            distX += spacing * math.cos(theta)**2
            distY += spacing * math.sin(theta)**2

    # pack points into continuous path
    p = Path(*[Line(complex(*coords[i - 1]), complex(*coords[i])) for i in range(1, len(coords))])

    if reverse:
        p = p.reversed()

    # clackson scroll formula for estimating yarn length
    # print("estimated path length: ", round(math.pi * spacing * turns * turns), "mm")
    print("path length:\t", round(p.length()), "mm")
    print("points:\t\t", len(coords))

    return p


def main(argv):
    parser = argparse.ArgumentParser(description='Tool for generating stitching paths for embroidered coils.')
    parser.add_argument('-oh', help='outer height <float>', type=float, required=True, dest="oh")
    parser.add_argument('-ow', help='outer width <float>', type=float, required=True, dest="ow")
    parser.add_argument('-iw', help='inner width <float>', type=float, required=True, dest="iw")
    parser.add_argument('-t', help='number of turns <int>', type=int, required=True, dest="turns")
    parser.add_argument('-r', help='reverse path direction from outward to inward', action="store_true", dest="reverse")
    parser.add_argument('-s', help='save to svg', action="store_true", dest="save")
    args = parser.parse_args()

    print("generating path ...")
    s = spiral(args.oh, args.ow, args.iw, args.turns, args.reverse)

    if args.save:
        print("saving path ...")
        name = "rect_coil_{}t_{}oh_{}ow_{}iw".format(args.turns, round(args.oh), round(args.ow), round(args.iw))
        if args.reverse:
            name += "_r"
        name += ".svg"
        d = "{}mm".format(args.oh * 1.2)
        wsvg(s, dimensions=(d, d), margin_size=0.1, filename=name)
        print(name)


if __name__ == "__main__":
    main(sys.argv[1:])
