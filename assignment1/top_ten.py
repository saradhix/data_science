import sys
import json

def main():
    stop_words = ['is','it','has','a','an','the']
    tweet_file = open(sys.argv[1])
    tag_frequency={} #create a new dictionary
    count =0
    for line in tweet_file:
      try:
        json_obj = json.loads(line.rstrip())
      #print json_obj
      #print "-"*60
        hashtags = json_obj["entities"]["hashtags"]
        for hashtag in hashtags:
          tag = hashtag["text"]
          if tag not in tag_frequency:
            tag_frequency[tag]=0
          tag_frequency[tag] += 1
      except:
        continue
    count =0
    for tag in sorted(tag_frequency, key=tag_frequency.get, reverse=True):
      print tag, tag_frequency[tag]
      count +=1
      if count ==10:
        break
    #for key, value in term_frequency.items():
     # print key, round(float(value)/count,4)
if __name__ == '__main__':
    main()
