import sqlite3

class sql_con():
    def __init__(self):
        self.con = sqlite3.connect('./words/dictionary.db')

    def query(self, q):
        cur = self.con.execute(q)
        return cur.fetchall()

def get_word_type(t):
    con = sql_con()
    return [n[0] for n in con.query(f"select distinct word from entries where wordtype like '%{t}%'")]

def words():
    return get_word_type('')

def nouns(plural=None):
    if plural is None:
        return get_word_type('n.')
    if plural:
        return get_word_type('n. pl.')
    return get_word_type('n. sing.')

def verbs():
    return get_word_type('v.')

def adjectives():
    return get_word_type('a.')

def adverbs():
    return get_word_type('adv.')    

def preposition():
    return get_word_type('prep.')

def interjection():
    return get_word_type('interj.')


print(words())