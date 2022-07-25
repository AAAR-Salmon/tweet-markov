import MeCab
import json
from markovchain import SimpleMarkovChain


if __name__ == '__main__':
    with open('tweets.json', 'r') as fp:
        tweets = json.load(fp)
    # tweetのtokenize
    tokenizer = MeCab.Tagger('-Owakati')
    tokenized_tweets: list[list[str]] = [tokenizer.parse(tw).split() for tw in tweets]
    # tokenの辞書作成
    tokens = set().union(*tokenized_tweets)
    id2tok = list(tokens)
    tok2id = {tok: id for id, tok in enumerate(id2tok)}
    N = len(id2tok)
    # tokenizeされたtweetのid列化
    ided_tweets = [[tok2id[tok] for tok in tw] for tw in tokenized_tweets]

    mc = SimpleMarkovChain(N)
    mc.fit(ided_tweets)
    for _ in range(10):
        ided_sentence = mc.generate()
        print(''.join([id2tok[id] for id in ided_sentence]))
