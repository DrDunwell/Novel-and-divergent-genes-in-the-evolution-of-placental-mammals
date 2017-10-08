# -*- coding: utf-8 -*-
"""
Python 2.7
Thomas Dunwell, University of Oxford, 2016.
Homology_Group_Frequence_Counting.py
"""

#This script was used in the following paper:

#cite the following paper
#Dunwell TL, Paps J, Holland PWH. Novel and divergent genes in the evolution of placental mammals. Proc Biol Sci. 2017 Oct 11;284(1864). pii: 20171357. doi:10.1098/rspb.2017.1357. PubMed PMID: 28978728.

#The input for this script is the output file from running the MCL clustering, this is a file with one homology group per line, where each line is a list of all the protein IDs assigned to that homology group. 

#The original protein IDs used in the blast DB were appended with a four letter ID to denote the species, those IDs are the ones used to generate the species list.

#This script will generate a tab delimited text file containing the total number of times each species ID is present in each homology group.

#An example of the protein annotation from the origional protein files is..
#>BOSTgi45429986refNP_991354.1 retinoic acid early transcript 1G precursor [Bos taurus]
#MAKGEIGGPETRLGFLDLLLIVWFSGTPGDAHSLSFDFTVDPQPRPGHPWCEIQSQVDGKVFLSYDCGHAKIIIPTVLGE
#EVKTIKAWETQIETLRDIRDWIKDHMHDFTLEKHMPRDPRTLQARMTCHCEDDRHVSGSWQFGLNGQMSLHFDLENGHWR
#VGQPGGRWMKEKWENDRAVMEFLKKVSMGDCRGWLQDFMVRWKEILKTTASPTTVPPTVQPTAPPISHVTWIAPGVLVSF
#VIKGIVAWILYKKRRLCSQEAPDRCSVGLRTQCLLGCFCSPAFTLEPRDQTLGVSSLSTSYDDTVAAPSRVSCQI

import os
import argparse

def check_file_is_valid(parser, file):
	if not os.path.exists(file):
		parser.error("The file %s does not exist! Please ensure you have spelled it correctly." % file)
	else:
		return file

def Species_cluster_counting(MCL2_out_put_file_name,output_file_name,species_list):
	correct_name = 0
	#This is a list of all the species identifers added to the headers for the proteins used in the blast DB and BlastP searches, an example is given above. This is also the order of the columns in the output file.
	MCL2_out_put_file = open(MCL2_out_put_file_name,"r")
	output_file = open(output_file_name,"w")
	for species in species_list:
		output_file.write(species + "\t")
	output_file.write("\n")
	for line in MCL2_out_put_file:
		countlist = ""
		for species in species_list:
			if line.count(species) > 0:
				countlist = str(countlist) + str(line.count(species)) + "\t"
			else:
				countlist = countlist + "0" + "\t"
		output_file.write(countlist+ "\n")

parser = argparse.ArgumentParser(description='This script is designed to take the output from MCL which has been used to generate clusters of similarity from BLASTP data. It counts the number of times a species ID is counted in each cluster and outputs as a tab delimited file. The species ID must be added in the origional collection of protein sequences.')

parser.add_argument("-f", action='store', dest="FileName", required=True, type=lambda x: check_file_is_valid(parser, x), help='The name of the input MCL output file.')
parser.add_argument("-o", action='store', dest="OutFileName", default="", required=False, type=str, help='The output file name.')
parser.add_argument("-i", action='store', dest="IDlist", default="", required=False, nargs='+', help='A list of species IDs to be used during counting.')

args = parser.parse_args()

#checks for the use of output file name in command line, if not used just appends _counted_species to the input file name
if args.OutFileName == "":
	output_file_name = str(args.FileName) + "_counted_species"
else:
	output_file_name = args.OutFileName

#This list can be manually populated if it is easier than typing them in the command line.
if args.IDlist == "":
	species_list = ["HOMO","MUSM","ORYC","BOST","FELI","EQUU","SORE","LOXO","ECHI","DASY","MONO","ORNI","SARC","GALL","TAEN","ANOL","CHRY","XEON","OREO","DANI"]
else:
	species_list = args.IDlist

if __name__ == "__main__":
	Species_cluster_counting(args.FileName,output_file_name,species_list)
