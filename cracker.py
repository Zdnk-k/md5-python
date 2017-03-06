import hashlib
import os
import sys
import time
import string


def is_hex(hsh):
    """check if hex number"""
    return all(c in string.hexdigits for c in hsh)

def get_input_hash():
    """retrieves hash from input"""
    inputHash =  input("Hash to compare: ")
    while not check_correct_hash(inputHash):
        inputHash = input('Try again: ')
    return inputHash.rstrip()


def check_correct_hash(inputHash):
    """checks hash length (must be 32)"""
    if not len(inputHash) == 32:
        print('Incorect hash length')
        return False
    elif not is_hex(inputHash):
        print('Incorect hash format: Not a hex checksum')
        return False
    else:
        return True


def get_dictionary():
    """retrieves path to dictionary from input"""
    path = input("Path to dictionary: ")
    while not check_correct_file(path):
        path = input("Try again: ")
    return path.rstrip()



def check_correct_file(path):
    """checks if there is a file in given path"""
    try:
        if not os.path.isfile(path):
            print('Not a File')
            return False

        if not path.endswith('.txt'):
            print('Bad file type')
            return False
        # TODO: DOESNT WORK RIGHT!!!
        print('File opened succesfully.')
        return True
    except IOError as e:
        errno, strerror = e.args
        print('I/O error({0}): {1}'.format(errno, strerror))
        # print(e)
        return False


def hash_word(word):
    """Creates md5 hash of the world"""
    try:
        wordHash = hashlib.md5(word).hexdigest()
        return wordHash
    except Exception as e:
        print(e)


def compare_hashes(inputHash, wordHash):
    """Compares two hashes"""
    return inputHash == wordHash


def read_n_compare(filename, inputHash):
    """opens file, reads it line by line and calls compare_hashes()"""
    try:
        f = open(filename, 'r')
        for line in f:
            line = line.encode('utf-8').rstrip()
            if compare_hashes(inputHash, hash_word(line)):
                print("Found it! Password: {}".format(line.decode('utf-8')))
                return True
        print('\nNO MATCH FOUND\n')
        return False
    except IOError as e:
        errno, strerror = e.args
        print('I/O error({0}): {1}'.format(errno, strerror))
    except ValueError as ve:
        print(ve)
    except Exception as ge:
        print(ge)
    else:
        f.close()


def wanna_end():
    """ask user whether to end/continue"""
    answer = input("Do you wish to try again? (Yes/No)")
    while True:
        if answer in ('Yes', 'yes', 'y', 'YES', 'yep', 'yarp', 'aye'):
            return False
        elif answer in ('No', 'no', 'n', 'nope', 'NO', 'nay'):
            return True
        else:
            print("The ability to type propely is certainly a nice thing to have, ain\'t it?")
            answer = input("Do you wish to try again? (Yes/No) ")



def cracker():
    end = False
    print('WELCOME!!!')
    while not end:
        # get hash from user
        inputHash = get_input_hash()
        # get path to dictionary (dictionary name)
        path = get_dictionary()

        read_n_compare(path, inputHash)
        end = wanna_end()
    print('Exiting.')
    time.sleep(3)
    sys.exit()


cracker()
# TODO: replace latters
# TODO: variations
# TODO: check corect file, does it exist
# TODO: yes no lambda
# TODO: TRY
