def get_int_in_range(prompt, lo, hi):
        s = input(prompt).strip()
        x = int(s)
        if not (lo <= x <= hi):
            raise ValueError(f"{x} not in range {lo}-{hi}")
        return x

def _validate_range(x, lo, hi):
      return lo <= x <= hi

assert _validate_range(3, 0, 5) == True
assert _validate_range(99, 0, 5) == False

while True:
      try:
            choice = get_int_in_range("Choose 0-2, ", 0, 2)
            break
      except ValueError:
            print("Invalid input, try again.")


#Nested menu with helper functions, validator core logic with asserts at the end

def get_int_in_range(prompt, lo, hi):
     while True:
          s= input(prompt).strip()
          try:
               x = int(s)
               if lo <= x <= hi:
                    return x
               else:
                    print(f"Enter a number in [{lo}-{hi}].")
          except ValueError:
               print("Enter a valid integer.")

def main_choice():
      print("1. Math functions")
      print("2. Greetings")
      print("0. Exit")
      return get_int_in_range("Choose (0-2): ", 0, 2)

def math_choice():
     print("1. Square a number.")
     print("2. Get the factorial of a number.")
     print("0. Return to previous menu.")
     return get_int_in_range("Choose (0-2): ", 0, 2)

def square_number():
          x = get_int_in_range("Enter a number to get the square of it: ", -10**9, 10**9)
          total = x * x
          print(f"The square of {x} is {total}.")

def factorial():
          x = get_int_in_range("Enter a non-negative integer from 0-100: ", 0, 100)
          total = 1
          for i in range(1, x+1):
               total *= i
          print(f"The factorial of {x} is {total}.")

def greet_choice():
     print("\nGreetings:")
     print("1. Say Hello")
     print("2. Say Goodbye")
     print("0. Return to previous menu")
     return get_int_in_range("Choose (0-2): ", 0, 2)

def say_hello():
     print("Hello!")

def say_goodbye():
     print("Goodbye!")

while True:
      m = main_choice()
      if m == 1:
            while True:
                  mm = math_choice()
                  if mm == 0: break
                  elif mm == 1: square_number()
                  elif mm == 2: factorial()
      elif m == 2:
          while True:
                gm = greet_choice()
                if gm == 0 : break
                elif gm == 1: say_hello()
                elif gm == 2: say_goodbye()
      elif m == 0:
          print("Exiting")
          break
    
#validator core of get_int_in_range
def _validate_range(x, lo, hi): return lo <= x <= hi
assert _validate_range(2, 0, 3) is True
assert _validate_range(5, 0, 3) is False

#validator core of factorial()
def factorial_core(n):
      total = 1
      for i in range(1, n+1):
            total *= i
      return total
assert factorial_core(5) == 120


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