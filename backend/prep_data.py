from re import sub
from json import dump

class Sentence:
    def __init__(self, text):
        text = sub("[',:;-]" , '', text)
        self.text = sub('[\.\?"!]',' ',text)
        self.lower = self.text.lower()
        self.sorted = sorted([i.lower() for i in self.text.split()])

def main():
    line_dict = {}
    delim = '&&'
    with open('archive/movie_lines.tsv', encoding="utf8") as f:
        for line in f:
            line_split = line.split('\t')
            line_dict[line_split[0]] = Sentence(line_split[-1])
            
    list_of_replies = []
    with open('archive/movie_conversations.tsv') as f:
        for line in f:
            # changes are made for debugging
            #line = f.readline()
            list_elem = sub(' ' , ',' , line.split('\t')[-1])
            list_of_replies.append(eval('list({})'.format(list_elem)))
    replies = {}

#    with open('debug.txt' , 'w', encoding="utf8") as f:
#        for sentence in list_of_replies:
#            for j in sentence:
#                f.write(line_dict[j].text)
#            f.write('\n')

    for sentence in list_of_replies:
        for i,curr in enumerate(sentence[:-1]):
            reply = replies
            for k in line_dict[curr].lower.split():
                if k not in reply:
                    reply[k] = {}
                reply = reply[k]
            reply[delim] = (line_dict[sentence[i+1]].text,
                    line_dict[curr].text)

    with open('langTree.json','w') as f:
        dump(replies,f)

if __name__ == "__main__":
    main()


