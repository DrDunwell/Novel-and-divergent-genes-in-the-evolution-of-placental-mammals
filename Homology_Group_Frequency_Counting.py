# -*- coding: utf-8 -*-
"""
Python 2.7
Thomas Dunwell, University of Oxford, 2016.
Homology_Group_Frequence_Counting.py
"""

#This script was used in a paper titled "Novel and divergent genes in the evolution of placental mammals" Dunwell et al., In press

#The input for this script is the output file from the MCL clustering which is a file with one homology group per line, 
#where each line is a list of all the protein IDs assigned to that homology group. 
#The original protein IDs used in the blast DB were appended with a four letter ID to denote the species, those IDs are the ones used to generate the species list.

#This script will generate a tab delimited text file containing the total number of times each species ID is present in each homology group.

#>BOSTgi45429986refNP_991354.1 retinoic acid early transcript 1G precursor [Bos taurus]
#MAKGEIGGPETRLGFLDLLLIVWFSGTPGDAHSLSFDFTVDPQPRPGHPWCEIQSQVDGKVFLSYDCGHAKIIIPTVLGE
#EVKTIKAWETQIETLRDIRDWIKDHMHDFTLEKHMPRDPRTLQARMTCHCEDDRHVSGSWQFGLNGQMSLHFDLENGHWR
#VGQPGGRWMKEKWENDRAVMEFLKKVSMGDCRGWLQDFMVRWKEILKTTASPTTVPPTVQPTAPPISHVTWIAPGVLVSF
#VIKGIVAWILYKKRRLCSQEAPDRCSVGLRTQCLLGCFCSPAFTLEPRDQTLGVSSLSTSYDDTVAAPSRVSCQI

import os

def Species_cluster_counting():
    correct_name = 0
	#This is a list of all the species identifers added to the headers for the proteins used in the blast DB and BlastP searches, an example is given above.
    species_list = ["HOMO","MUSM","ORYC","BOST","FELI","EQUU","SORE","LOXO","ECHI","DASY","MONO","ORNI","SARC","GALL","TAEN","ANOL","CHRY","XEON","OREO","DANI"]    
    while correct_name != 1:
        MCL2_out_put_file_name = raw_input("What is the name of the MCL output file? (it must be in the same folder you are running this script from): ")
        if os.path.isfile(MCL2_out_put_file_name):
            correct_name = 1
        else:
            print "\n" + "I'm sorry, but that file is not in the directory you ran this script from. Please try again." + "\n"
    MCL2_out_put_file = open(MCL2_out_put_file_name,"r")
    MCL2_out_put_file_counts = open(MCL2_out_put_file_name + "_counted_species","w")
    for species in species_list:
        MCL2_out_put_file_counts.write(species + "\t")
    MCL2_out_put_file_counts.write("\n")
    for line in MCL2_out_put_file:
        countlist = ""
        for species in species_list:
            if line.count(species) > 0:
                countlist = str(countlist) + str(line.count(species)) + "\t"
            else:
                countlist = countlist + "0" + "\t"
        countlist = countlist + "\n"
        MCL2_out_put_file_counts.write(countlist)

if __name__ == "__main__":
	Species_cluster_counting()