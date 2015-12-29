import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[0] + '-' + record[1], 1)
    mr.emit_intermediate(record[1] + '-' + record[0], 1)

def reducer(key, list_of_values):
    if len(list_of_values) is 1:
        pair = key.split('-')
        mr.emit((pair[0], pair[1]))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
