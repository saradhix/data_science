import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def load_sentiment_scores(afinnfile):
  scores = {} # initialize an empty dictionary
  for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.

  #print scores.items() # Print every (term, score) pair in the dictionary
  return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = load_sentiment_scores(sent_file)
    #lines(sent_file)
    #lines(tweet_file)
    for line in tweet_file:
      try:
        json_obj = json.loads(line.rstrip())
      #print json_obj
      #print "-"*60
        text = json_obj["text"]
        terms = text.split()
        #print "Terms=",terms
        tweet_score =0
        for term in terms:
          if term in scores:
            tweet_score += scores[term]
        print tweet_score
      except:
        print 0
        continue

if __name__ == '__main__':
    main()
