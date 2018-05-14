#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:29:45 2018
Version 1. SAM to BED Exercise - output BED format with read
Version 2. SAM to BED Exercise - output BED format with fragment coordinates
           Fragment length (TLEN) + chromStart = coordinate of end of fragment.



1. Import file from public location (Lucy's SAM file)
2. Format: Datastructure representing the contents of BED file
   Map from one file format to the other:
       List of format changes required
       Define destination
       Write data from old file to new file
       File structures: https://genome.ucsc.edu/FAQ/FAQformat.html3. Required BED fields:
   1. chrom
   2. chromStart # coordinate of start of read from 5' end
   3. chromEnd # this is the end of the 3' read NOT the end of the fragment!4. Optional - to include for this exercise
   4. name
   5. score
   6. strand
   
5. Extra options
   7. coordinate of end of read: fragment end - chromStart + TLEN (9)File structure of SAM file:
SAM field names:
1. RNAME(3)
2. POS(4)
3. SEQ (length of) (10): apply length function +1 len(POS) (check coordinate system of each type of file)
4. QNAME (1)
5. MAPQ (5)
6. Use default: + (ATACSeq data)
7. Check how DNA is indexed from beginning of chromosome -> 0 in BED, 1 in SAM@author: Lagaanninja
"""
option = "Read"
previousname = ""with open ("BAMtoBEDtest.sam") as f :
   with open ("BED_output_V3_read.bed", 'w') as f_out : # write below to a new file
       f_out.write("chrom\tchromStart\tchromEnd\tName\tScore\tStrand\n") # to write in header in line 1
       for line in f :
           if line[0] != "@" : # if the line does not begin with @, the following function can be done
               #print (line)
               # python string split needs to be done to return the fields of interest
               fields = line.split ("\t")    # \t is a tab separator, function will return a list of strings
               #print (fields) # this returns a list of lines, each containing a list of a gene with its fields
               if option == "Fragment" :
                   
                   if fields[0] == previousname:
                       previousname = fields[0]
                       continue
               previousname = fields[0]        
               chrom = fields[2] # start from 2nd index -1 because of the differences in coordinate conventions
               chromStart = int(fields[3]) -1
               if option == 'Read' :
                   chromEnd = len(fields[9]) + chromStart
                   Score = fields[4]
               elif option == 'Fragment' :
                   chromEnd = int(fields[8]) + chromStart
                   Score = fields[8]
               Name = fields[0]
               Strand = '+'
               f_out.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(chrom, chromStart, chromEnd, Name, Score, Strand))    f_out.close() # closes file
   
   # write the whole for loop results out into a new file called BED_output.bed, using the write argument
   # between each field include a tab; \n is a new line
