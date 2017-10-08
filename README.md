# Novel-and-divergent-genes-in-the-evolution-of-placental-mammals

The scripts in this repository were used in data processing for the paper Novel and divergent genes in the evolution of placental mammals. Dunwell et al. Proceedings of the Royal Society B, 2017.

If any of these scripts, or pipeline, or parts there of, are used please cite the following

Dunwell TL, Paps J, Holland PWH. Novel and divergent genes in the evolution of placental mammals. Proc Biol Sci. 2017 Oct 11;284(1864). pii: 20171357. doi:10.1098/rspb.2017.1357. PubMed PMID: 28978728.

Homology_Group_Frequency_Counting.py

This script is used on the output of MCL. It counts how many proteins are present in each Homology Group (HG) from each species used in the analysis. The output is a tab delimited table of counts which can be examined and filtered in suitable programs like R, or even excel for those who want an easy interface.

Adding_HG_ID_to_MCL_input.py

In order to examine the blast interactions between HGs the HG ID for the query and subject are first appended to the end of the output file from mcxdeblast, which in turn takes its input as the output of the reciprocal BlastP results. Depending on the total number of BlastP comparisons this file can be very big. As an output it takes the three column file from mcxdeblast and adds two additional columns corresponding to the HG ID for the query and subject.

Blast_interaction_mapping.py

This scripts counts up how blast interactions each individual protein has, for example 1 protein in a HG might blast 13 other HG, whereas another protein might only hit its own HG. The input of this script are the output of the two previous scripts. You also need to tell it which HG you want to examine from the output of MCL/Homology_Group_Frequency_Counting.py. Each HG in the output files of the MCL/Homology_Group_Frequency_Counting.py is represented on a single line, so the first line is HG 1, the second HG 2...etc. The output of this script is a tab delimited table of counts. The row headers are the HG you asked the script to examine, the column headers are all of the clusters which were found during the blast interaction checks. This table can be examined and filtered in suitable programs like R, or even excel for those who want an easy interface.


Overview of pipeline for identification of Novel Homology Groups, for more information please see Novel and divergent genes in the evolution of placental mammals. Dunwell et al. Proceedings of the Royal Society B, 2017.

1 - Taxon samples should be decided upon to include a distribution of IN and OUT groups so comparisons between them can be confidently interpreted.

2 - Canonical proteins for all species should be obtained, potential sources include Ensembl and NCBI protein repositories. For ease of handling a species identifier should be added to each protein from each species, for example a header starting with ">HOMO.." for human proteins

3 - A blast DB should be generated containing all of the proteins for all of the selected species. [makeblastdb -in total_protein_fasta_file -dbtype prot -out database_name -parse_seqids] -parse_seqids is useful as it allows you to extract protein sequences from the DB at a later date, for example to pull out all protein sequences in a specific Homolgy Group.

4 - All of the proteins in the blast DB should then be compared against the DB using BLASTP. [blastp -query input_protein_sequences -db name_of_generated_DB -evalue 0.00005 -outfmt 6 -out out_put_file_name]

5 - The results of the BLASTP searches should be processed with mcxdeblast for compatibility with MCL. [mcxdeblast --m9 --line-mode=abc --out=out_put_file_name input_file_name]

6 - The results of step 6 should be passed to MCL for Homology Group identification. The result will be the generation of a series of Homology Groups. [mcl out_put_file_of_mcxdeblast --abc -I 2 -o out_put_file_name]

7 - The results of steps 5 and 6 are then used as inputs for Adding_HG_ID_to_MCL_input.py File names need to be added manually into the script

8 - The results of step 6 are used as the input for Homology_Group_Frequency_Counting.py. A comma separated list of species identifies needs to be added manually to the script, file names are added in command line after runnning the script. The output of this is used to examine the evolutionary relationships for all identified Homology Groups.

9 - To generate a base examination for the blast interactions between the identified Homology Groups identified in step 8 and all other clusters, the output of steps 7 and a series of homology group IDs selected from step 8 are used as inputs for Blast_interaction_mapping.py file names need to be added into the script manually
