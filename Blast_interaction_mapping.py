# -*- coding: utf-8 -*-
"""
Python 2.7
Thomas Dunwell, University of Oxford, 2016.
"""

#This script was used in a paper titled "Novel and divergent genes in the evolution of placental mammals" Dunwell et al., In press

#The final output of this script is a tab delimited text file with row headers for each of the Core Ancestral HG, and row readers for each HG any protein
#in the Core group has a blast hit with.

def Mapping_and_counting_blast_interactions()
	#adjust file names based on the outputs of the previous scripts
	MCL2_file_HG_ID_added = open("MCL2_file_HG_ID_added","r") #name of the output file from mcxdeblast after running Adding_HG_ID_to_MCL_input.py
	Parsed_MCL2_file_out = open("parsed_MCL2_files","w") #This is an output file which is a subset of "MCL2_file_HG_ID_added"
	Blast_count_output_file = open("Blast_count_output_file","w")

	#After taking the output of Homology_Group_Frequency_Counting.py and filtering the data in a suitable way, (e.g. R/command line). The Core Ancestral 
	#HG were identified, and they added into the list below, a total of 87 are present

	Core_HG_List = [] # this list needs to be populated with a list of homology group IDs for which you want to generate blast interaction data

	Core_HG_Dic = {}
	for i in Core_HG_List:
		Core_HG_Dic.update({i:"N"})
		
	#The next step is to take the file created by running Adding_HG_ID_to_MCL_input.py and pull out of it all rows where the queery 
	#belongs to a Core Ancestral HG for reference later
	#As we do this we probe all the data and generate a list of all clusters hit by any of the Ancerstral Core HG
	#And also generate a list of all the HG hit by individual proteins.

	List_Of_blast_hits = []
	Dic_for_mapping_blast_interactions = {}
	#this bit maps all the interactions and stores
	for line in MCL2_file_HG_ID_added:
		line_split = line.split()
		line_split = [line_split[0],line_split[1],line_split[2],int(line_split[3]),int(line_split[4])]
		if line_split[3] in Core_HG_Dic:
			Parsed_MCL2_file_out.write(line)
			if line_split[0] in Dic_for_mapping_blast_interactions:
				if line_split[4] in Dic_for_mapping_blast_interactions[line_split[0]][line_split[3]]:
					pass
				else:
					Dic_for_mapping_blast_interactions[line_split[0]][line_split[3]].append(line_split[4])
			else:
				Dic_for_mapping_blast_interactions.update({line_split[0]:{line_split[3]:[line_split[4]]}})
			if line_split[4] not in List_Of_blast_hits:
				List_Of_blast_hits.append(line_split[4])

	#This section sums up how many times a protein in an HG has a blast interaction to any protein in another HG, for example, 100% of the proteins
	#in on HG will hit the same HG.

	Dic_for_summing_blast_interactions = {}
	for key in Dic_for_mapping_blast_interactions:
		cluster_ID = Dic_for_mapping_blast_interactions[key].keys()[0]
		hit_clusters = Dic_for_mapping_blast_interactions[key][cluster_ID]
		if cluster_ID in Dic_for_summing_blast_interactions:
			for hit_cluster_ID in hit_clusters:
				if hit_cluster_ID in Dic_for_summing_blast_interactions[cluster_ID]:
					Dic_for_summing_blast_interactions[cluster_ID][hit_cluster_ID] = Dic_for_summing_blast_interactions[cluster_ID][hit_cluster_ID] + 1
				else:
					Dic_for_summing_blast_interactions[cluster_ID].update({hit_cluster_ID:1})
		else:
			temp_dic = {cluster_ID:{}}
			for ID in hit_clusters:
				temp_dic[cluster_ID].update({ID:1})
			Dic_for_summing_blast_interactions.update(temp_dic)
			
	#Sorting the list of hits is important to ensure we can guantee the order of the output
	Sorted_List_Of_blast_hits = sorted(List_Of_blast_hits)

	#write cluster ID headers to file
	Blast_count_output_file.write("\t")
	for ID in Sorted_List_Of_blast_hits:
		Blast_count_output_file.write(str(ID) + "\t")
	Blast_count_output_file.write("\n")

	#write blast count frequencies
	for ID in Core_HG_List:
		Blast_count_output_file.write(str(ID) + "\t")
		for ID_2 in Sorted_List_Of_blast_hits:
			if ID_2 in Dic_for_summing_blast_interactions[ID]:
				Blast_count_output_file.write(str(Dic_for_summing_blast_interactions[ID][ID_2]) + "\t")
			else:
				Blast_count_output_file.write("0" + "\t")
		Blast_count_output_file.write("\n")

	#close all files
	MCL2_file_HG_ID_added.close()
	Parsed_MCL2_file_out.close()
	Blast_count_output_file.close()

if __name__ == "__main__":
	Mapping_and_counting_blast_interactions()