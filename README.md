# SpiralGeneratorRect
Rectangular spiral generator for embroidered speaker coils.

### Prerequisites

You need svgpathtools to run this script. Install it via pip using this command:  
pip install svgpathtools

### Usage:
./spiral_generator_rect.py [-h] -oh <float> -ow <float> -iw <float> -t <int> [-r] [-smin <float>] [-smax <float>] [-s]

### Example:
./spiral_generator_rect.py -t 10 -oh 80 -ow 40 -iw 20 -s


### Optional arguments:
|  -h, --help  show help message  
|  -t          number of turns <int>  
|  -oh         outer height <float>  
|  -ow         outer width <float>  
|  -iw         inner width <float>  
|  -smin       min stitch length, default = 2 <float>  
|  -smax       max stitch length, default = 2 <float>  
|  -r          reverse path direction from outward to inward  
|  -s          save to svg  
  
### Contact:
michael.reiter@fh-hagenberg.at

Based on spiral-generator by thomas.preindl(at)fh-hagenberg.at

