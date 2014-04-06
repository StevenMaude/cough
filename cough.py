#!/usr/bin/env python
# encoding: utf-8
import random
import sys

def wraparound_list_index(index, a_list):
    """
    Wraparound list indexes that are out of range for list.

    Take index as int and list; return a (wrapped around) index as int.
    
    >>> wraparound_list_index(4, [0, 1, 2])
    1
    >>> wraparound_list_index(0, [0, 1, 2])
    0
    >>> wraparound_list_index(3, [0, 1, 2])
    0
    >>> wraparound_list_index(-1, [0, 1, 2])
    2
    >>> wraparound_list_index(-5, [0, 1, 2])
    1
    """
    # http://stackoverflow.com/questions/8951020/pythonic-circular-list
    return index % len(a_list)


def create_keys():
    """
    Return a list of tuples corresponding to major and minor keys.
    
    >>> create_keys()[0]
    ('C', 'Am')
    >>> create_keys()[-1]
    ('F', 'Dm')
    """
    major_keys = ['C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb',
                  'Db', 'Ab', 'Eb', 'Bb', 'F']
    minor_keys = ['Am', 'Em', 'Bm', 'F#m', 'C#m', 'G#m', 'Ebm/D#m',
                  'Bbm', 'Fm', 'Cm', 'Gm', 'Dm']
    return zip(major_keys, minor_keys)


def get_incremented_key(key_signature_index, key_increment, major_minor_pairs):
    """
    Return the major/minor keys shifted by some key_increment of sharps.

    Increment can be negative.
    """
    return major_minor_pairs[wraparound_list_index(
        key_signature_index + key_increment, major_minor_pairs)]


def main():
    major_minor_pairs = create_keys()
    print major_minor_pairs
    chosen_key_signature = random.randint(0, len(major_minor_pairs) - 1)
    key_type = random.randint(0, 1)  # 0 for major, 1 for minor
    print "major_minor_pairs"
    print "Chosen key is", major_minor_pairs[chosen_key_signature][key_type]
    raw_input("Press ENTER when ready for answers.")
    print "The relative key is", \
        major_minor_pairs[chosen_key_signature][key_type - 1]

    for increment in ['+1', '-1', '+2', '-2', '+7', '-7']:
        incremented_key = get_incremented_key(chosen_key_signature,
                                              int(increment),
                                              major_minor_pairs)
        print "Keys with {0} sharp(s): {1}, {2}".format(increment,
                                                        incremented_key[0],
                                                        incremented_key[1])

if __name__ == '__main__':
    main()
