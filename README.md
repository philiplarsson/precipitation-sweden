# Precipitation

Check if there is any precipitation for specified hours forward (8 is default).
Note that the longitude and latitude needs to be in a [valid geographic area](http://opendata.smhi.se/apidocs/metfcst/geographic_area.html).
Use [this](http://opendata.smhi.se/apidocs/metfcst/demo_point.html) link to get correct latitude and longitude: 
Change using `--latitude` and `--longitude` to get correct geographic area. Default is Lund Sweden.
See more using `-h` or `--help`.

Using API from SMHI Open Data.
Read more here: [http://opendata.smhi.se/apidocs/](http://opendata.smhi.se/apidocs/).

## Example Usage

Grant execution permisson to file owner: `chmod u+x precipitation.py`.

### Check if there is any precipitation in the next 8 hours:
```terminal
$ ./precipitation.py
```

### Check if there is any precipitation in the next 48 hours:

```terminal
$ ./precipitation.py -hours 48
```

### Check if there is any precipitation in the next 12 hours in Stockholm:
```terminal
./precipitation.py --latitude 59.23 --longitude 18.15 --hours 12

```


