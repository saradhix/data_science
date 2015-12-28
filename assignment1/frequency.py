import sys
import json

def main():
    stop_words = ['is','it','has','a','an','the']
    tweet_file = open(sys.argv[1])
    term_frequency={} #create a new dictionary
    count =0
    for line in tweet_file:
      try:
        json_obj = json.loads(line.rstrip())
      #print json_obj
      #print "-"*60
        text = json_obj["text"]
        text = text.encode('utf-8')
        terms = text.split()
        for term in terms:
          if not term.isalpha():
            continue
          if term.startswith('@'):
            continue
          if term.startswith('#'):
            continue
          if term.startswith('http'):
            continue
          if term in stop_words:
            continue
          if term not in term_frequency:
            term_frequency[term]=0
          term_frequency[term] += 1
          count += 1
      except:
        continue
    print count
    for key, value in term_frequency.items():
      print key, round(float(value)/count,4)

if __name__ == '__main__':
    main()
