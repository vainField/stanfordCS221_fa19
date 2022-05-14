import collections
import math
import re
import sys

############################################################
# Problem 3a

def findAlphabeticallyLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return max(re.sub("[^\w\s]", "", text).split())
    # END_YOUR_CODE

############################################################
# Problem 3b

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)
    # END_YOUR_CODE

############################################################
# Problem 3c

def mutateSentences(sentence):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the orignal sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """
    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    words = re.sub("[^\w\s]", "", sentence).split()
    words_dict = {}
    for i in range(len(words)-1):
        if words[i] in words_dict:
            words_dict[words[i]].add(words[i + 1])
        else:
            words_dict[words[i]] = {words[i + 1]}

    def _mutateSentences(n):
        if n == 1:
            return [[word] for word in words_dict]
        result = []
        for _mutateSentence in _mutateSentences(n-1):
            if _mutateSentence[-1] in words_dict:
                for word in words_dict[_mutateSentence[-1]]:
                    result.append(_mutateSentence + [word])
        return result

    return [' '.join(s) for s in _mutateSentences(len(words))]
    # END_YOUR_CODE

############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    result = 0
    for key, value in v1.items():
        if key in v2:
            result += value * v2[key]
    return result
    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for key, value in v2.items():
        v1[key] = v1.get(key, 0) + value * scale
    # END_YOUR_CODE

############################################################
# Problem 3f

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    words_count = collections.defaultdict(int)
    for word in re.sub("[^\w\s]", "", text).split():
        words_count[word] = words_count.get(word, 0) + 1
    return {word for word in words_count if words_count[word] == 1}
    # END_YOUR_CODE

############################################################
# Problem 3g

def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (our solution is 19 lines of code, but don't worry if you deviate from this)
    memo = {}

    def isPalindrome(t):
        for i in range(len(t) // 2):
            if t[i] != t[-1-i]:
                return False
        return True

    def r(t):
        if t in memo:
            return memo[t]
        elif isPalindrome(t):
            memo[t] = len(t)
        else:
            memo[t] = max([r(_) for _ in [t[0:i] + t[i+1:len(t)] for i in range(len(t))]])
        return memo[t]

    sys.setrecursionlimit(10000)
    return r(text)
    # END_YOUR_CODE
