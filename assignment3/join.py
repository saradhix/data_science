import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    for order in list_of_values:
        if order[0] != 'order':
            continue
        for line_item in list_of_values:
            if line_item[0] != 'line_item':
                continue
            mr.emit(order + line_item)

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
