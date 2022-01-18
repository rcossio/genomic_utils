# This is a really small script to help me check primers of sequences
# Acumulated hours of work: 0.5   (update when developed)

# Known issues: 
#   * In the primer hits the very first/last part of the sequence, the software will report it is not a valid primer 
#   * RNA sequences with U will not report any warnings, this is the warning

# Desired features:
#   * I would like to create a FASTA object to keep the name of the sequence as header

import sys

def complementary(seq):
    '''Finds the complementary of a DNA sequence. 
    The returned string does not follow 5' or 3' writing rules,
    it is just returned in the order of the original string.'''

    compl=''
    for s in list(seq):
        if s=='A':  compl += 'T'
        if s=='T':  compl += 'A'
        if s=='C':  compl += 'G'
        if s=='G':  compl += 'C'
    return compl

def reverse(s):
    ''' Simple function to reverse a string. '''

    rev=''
    s=list(s)
    while len(s) > 0:
        rev += s.pop(-1)
    return rev
    

def read_fasta_file(filename):
    '''Reads a single sequence FASTA file. 
    The file can have a header and blank lines
    but must not contain multiple sequences as they will be read as one'''

    sequence=''
    for line in open(filename):
        if line.strip() == '': continue
        if line[0] == '>': continue
        
        sequence += line.strip()
    return sequence


# MAIN SCRIPT

#seq0=sys.argv[1] #Reads sequence from command line or it is declared as string
seq0='GGATGATTTGTATGTAGG'

fasta = read_fasta_file('hiv1.fasta')


seq = seq0
if len(fasta.split(seq)) == 2:
    print ("\nSecuencia directa: 5'-"+seq+"-3' encontrada")
    print('La secuencia '+seq0+' es un primer Fw que se pega a la cadena (-)')
    Li = len(fasta.split(seq)[0])
    Lp = len(seq)
    print('Pocisiones: '+str(Li+1)+' '+str(Li+Lp)+'\n')


seq = reverse(seq0)
if len(fasta.split(seq)) == 2:
    print ("\nSecuencia inversa: 5'-"+seq+"-3' encontrada")
    print ("El primer propuesto tiene un error\n")


seq = complementary(seq0)
if len(fasta.split(seq)) == 2:
    print ("\nSecuencia directa complementaria: 5'-"+seq+"-3' encontrada")
    print ("El primer propuesto tiene un error\n")


seq = complementary(reverse(seq0))
if len(fasta.split(seq)) == 2:
    print ("\nSecuencia inversa complementaria: 5'-"+seq+"-3' encontrada")
    print('La secuencia '+seq0+' es un primer Rv que se pega a la cadena (+)')
    Li = len(fasta.split(seq)[0])
    Lp = len(seq)
    print('Pocisiones: '+str(Li+1)+' '+str(Li+Lp)+'\n')

