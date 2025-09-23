
# wordfreq.py
import re
import csv
#first time seeing the import function, please do an introduction


def _read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
#this is a definition function, but haven't seen some parts. why use _ before naming the function?
#also what is the with function, and the open function? 
#path correlates to the inputted argument, what is "r", and encoding? is it also just passing
#arguments?

def _tokenize(text):
    # lowercase, then grab sequences of letters a-z
    return re.findall(r"[a-z]+", text.lower())
#same thing here, why _before the name?
#what is re.findall?

def _count(tokens):
    counts = {}
    for w in tokens:
        counts[w] = counts.get(w, 0) + 1
    return counts
#for this function, a local variable counts is listed as a dictionary
#what is counts[w]? it takes whats in the passed argument, breaks it into dictionary, but break it down for me
#returns a dictionary, that part i understand

def _top_items(counts, n):
    # list of (word, count) sorted by count desc
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]
#this one uses a few things i havent seen before. first is the sort() function
#also what is items()? break down everything in this part for me, none of it makes sense
#all i can understand is that sorted() is taking arguments in order to know how to parse, from context clues


def _write_csv(rows, out_path):
    # rows is iterable of (word,count)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        writer.writerows(rows)
#first time seeing "writer" as well, and writer() and writerow() and writerows(). break down everything here

def main():
    in_path  = "sample.txt"
    out_path = "top_20.csv"
    top_n    = 20

    text = _read_text(in_path)
    tokens = _tokenize(text)
    counts = _count(tokens)

    assert sum(counts.values()) == len(tokens)

    top_rows = _top_items(counts, top_n)
    _write_csv(top_rows, out_path)

    print(f"Wrote top {top_n} words to {out_path}")

def _run_smoke_tests():
    assert _tokenize("Hello, hello!") == ["hello", "hello"]
    assert _count(["a","b","a"]) == {"a": 2, "b": 1}                       # Count
    assert _top_items({"x":1,"y":3,"z":2}, 2) == [("y",3), ("z",2)] 
_run_smoke_tests()

main()

import re
import csv

def _read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
#function of this: take a file, turn it into a long string to process in python
#some things just "are", like open() and read(). 
#once opened with open(), it must be assigned in order to further process it
#i dont know what "r" is, and what encoding is. are these just functions of open() i must read up on?



def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)
#this step is to create "tokens", separating all words and removing special characters
#so you have a huge text string, and you must separate words from spaces and special letters
#'r' comes back here...what does it mean? in this case, is text=f, defined in the main function later?
#what does the + after [a-z] mean? does it mean for spaces? it feels like another thing that just 'is'. like theres no understanding it by reading it, i need to understand it by knowing the meaning of the syntax, since its not clear



def _count(tokens):
    counts = {}
    for w in tokens:
        counts[w] = counts.get(w, 0) + 1
    return counts
#so this step...you have a big list of tokens. findall() probably returns a list right? another gap in knowledge
#now you want to create a dictionary, where identical tokens are added together rather than being separate
#so for w in tokens: means to go down every entry from the findall() list, correct?
#this step... i get what the end result is, but having trouble understanding the transformation process
#counts[w] corresponds to the position in the list correct?
#.get() is a new function, i dont understand the key, default thing. and what is +1 for?
#at the end of this step, you should have a dictionary, not a list, of all the unique words, combined with how many times they show up in the string, yes?



def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    return pairs_sorted[:n]
#this step sorts the dictionary by first converting to a list which makes it sortable with sorted() correct?
#n here... is how many entries you want. for top 20, would n be 20? or did i misunderstand here
#since this step uses lambda, im not familiar with it. i also dont know hwat kv: kv[1] is
#what is pairs_sorted[:n]? is it up to n? in that case n at 20 would get 0-19, which is 20 entries correct?


def _top_items_longform(counts, n):
    pairs = list(counts.items())
    
    def by_count(pair):
        return pair[1]
    pairs_sorted = sorted(pairs, key=by_count, reverse=True)

    top = []
    i = 0
    for p in pairs_sorted:
        if i>= n:
            break
        top.append(p)
        i += 1
#the non lambda form of the top_items.
#pairs is a local variable assigned for the function
#list() converts into a list. dict.items(), why was it needed? why wasnt it list(counts)?
#what is by_count()? is it just a special syntax you need to memorize? seems self explanatory but is also a part of an existing hidden function
#return pair[1], that means return the second part of the pair? which is the number of times the word shows up
#maybe by_count is a variable, and its telling key=variable to sort by those numbers?
#top = [] seems to be the final printable list, controlled by n to say "how many are on the final list"
#once it reaches n, incrementing by 1, it will stop using an if statement


def _write_csv(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])
#this is definitely the most complex part of the code for me. probably because all these functions are new
#please break it down as if i know nothing about anything in this section

def main():
    in_path = "sample.txt"
    out_path = "top_20.csv"
    top_n = 20
    
    text = _read_text(in_path)
    tokens = _tokenize(text)
    counts = _count(tokens)

    assert sum(counts.values()) == len(tokens)

    top_rows = _top_items(counts, top_n)
    _write_csv(top_rows, out_path)

    print(f"Wrote top {top_n} words to {out_path}")

def _run_smoke_tests():
    assert _tokenize("Hello, hello!") == ["hello", "hello"]                # Normalize+Tokenize
    assert _count(["a","b","a"]) == {"a": 2, "b": 1}                       # Count
    assert _top_items({"x":1,"y":3,"z":2}, 2) == [("y",3), ("z",2)]        # Sort
_run_smoke_tests()
#finally, the main program.
#input path is defined, and so is output, as well as how many items are to be printed
#the pipeline is established: use _read_text(), then keep the result in a variable
#then tokenize that variable "text" with _tokenize()
#count and process into dictionary that list with _count
#sanity check here, making sure counts is as long as tokens. what i dont get here is, at this point shouldnt counts be a dictionary, and tokens is a list? their size should be different
#sort and get the top wanted amount, which is 20 in this case. when it reaches 20, stop and return that final list
#finally print it out using _write_csv, to the output path
#print a message telling the user the task has been completed, and where the result is

#finally some asserts testing each function




#retyped and understood each part from day 8 csv writer
import re
import csv

def _readfile(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)
#take out the + to transform into counting letters instead of words

def _count(tokens):
    counts = {}
    for w in tokens:
        counts[w] = counts.get(w,0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda kv:kv[1], reverse=True)
    return pairs_sorted[:n]
#to change the way it is sorted, change the key or remove the reverse

def _write_csv(rows, out_path):
    with open(out_path, "w", newline="", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top20.csv"
    top_n = 20

    text = _readfile(in_path)
    token = _tokenize(text)
    count = _count(token)

    assert sum(count.values) == len(token)

    top_rows = _top_items(count, top_n)
    _write_csv(top_rows, out_path)
    
    print(f"Top {top_n} words written to {out_path}.")

def smoke_tests():
    assert _tokenize("Hello! Hello, Hello!!!") == ["hello", "hello", "hello"]
    assert _count(["a","b","a"]) == {"a": 2, "b": 1}                       # Count
    assert _top_items({"x":1,"y":3,"z":2}, 2) == [("y",3), ("z",2)]        # Sort

smoke_tests()


#transformed word count, ascending order, with flag to choose between text file or multistring
import re
import csv

def _readfile(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)
#take out the + to transform into counting letters instead of words

def _count(tokens):
    counts = {}
    for w in tokens:
        counts[w] = counts.get(w,0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda kv:kv[1])
    return pairs_sorted[:n]
#to change the way it is sorted, change the key or remove the reverse

def _write_csv(rows, out_path):
    with open(out_path, "w", newline="", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top20.csv"
    top_n = 20


    USE_FILE = True
    text = _readfile(in_path) if USE_FILE else """your multiline string..."""
    token = _tokenize(text)
    count = _count(token)

    assert sum(count.values()) == len(token)

    top_rows = _top_items(count, top_n)
    _write_csv(top_rows, out_path)
    
    print(f"Top {top_n} words written to {out_path}.")

def smoke_tests():
    assert _tokenize("Hello! Hello, Hello!!!") == ["hello", "hello", "hello"]
    assert _count(["a","b","a"]) == {"a": 2, "b": 1}                       # Count
    assert _top_items({"x":1,"y":3,"z":2}, 2) == [("x",1), ("z",2)]        # Sort

smoke_tests()

main()

#modified version with letters, dictionary seeds all 26

import re
import csv
import string

def _read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
#now you have a bigasss string, next tokenize it and normalize it

def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]", text)

#a list of all letters has been created, all normalized as lowercase

def _counts(tokens):
    count = {letter: 0 for letter in string.ascii_lowercase}
    for w in tokens:
        count[w] = count.get(w, 0) + 1
    return count

def _top_items(count):
    pairs_sorted = sorted(count.items(), key=lambda kv: kv[1], reverse=True)
    return pairs_sorted

def _write_csv(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["letter", "count"])
        for letter, count in rows:
            writer.writerow([letter,count])

def main():

    stringinput = False
    inpath = "sample.txt" if not stringinput else "insert hardcode string here"
    outpath = "letters_sorted.csv"

    text = _read_text(inpath)
    token = _tokenize(text)
    count = _counts(token)

    assert sum(count.values()) == len(token)

    sortedlist = _top_items(count)
    _write_csv(sortedlist, outpath)

    print(f"List of number of times letters occured printed to {outpath}")

main()

def smoke_tests():
    assert _tokenize("Asshole") == ["a","s","s","h","o","l","e"]
    counts = _counts(["a","s","s","h","o","l","e"])
    assert counts["a"] == 1
    assert sum(counts.values()) == len("asshole")

smoke_tests()
