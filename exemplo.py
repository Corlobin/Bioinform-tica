import os
from urllib import request
	

def get_base_counts(dna):
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in dna:
        counts[base] += 1
    return counts

def get_base_frequencies(dna):
    return {base: dna.count(base)/float(len(dna)) for base in 'ATGC'}
	
def format_frequencies(frequencies):
    return ', '.join(['%s: %.2f' % (base, frequencies[base])
                      for base in frequencies])

def read_dnafile(filename):
    dna = ''
    for line in open(filename, 'r'):
        dna += line.strip()
    return dna

urlbase = 'http://hplgit.github.com/bioinf-py/data/'
yeast_file = 'yeast_chr1.txt'

if not os.path.isfile(yeast_file):
    url = urlbase + yeast_file
    request.urlretrieve(url, filename=yeast_file)
					  

dna = read_dnafile(yeast_file)					  
frequencies = get_base_frequencies(dna)

print ("Base frequencies of yeast DNA (length %d) \n%s" % \
      (len(dna), format_frequencies(frequencies)))



