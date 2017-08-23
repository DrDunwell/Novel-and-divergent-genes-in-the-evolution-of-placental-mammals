# Novel-and-divergent-genes-in-the-evolution-of-placental-mammals

The scripts in this repository were used in data processing for the papar Novel and divergent genes in the evolution of placental mammals. Dunwell et al. 2017

Homology_Group_Frequency_Counting.py

This script is used on the output of MCL. It counts how many proteins are present in each Homology Group (HG) from each species used in the analysis. The output is a tab delimited table of counts which can be examined and filtered in suitable programs like R, or even excel for those who want an easy interface.

Adding_HG_ID_to_MCL_input.py

In order to examine the blast interactions between HGs the HG ID for the query and subject are first appended to the end of the output file from mcxdeblast, which inturn takes its input as the output of the reciprocal BlastP results. Depending on the total number of BlastP comparisoins this file can be very big. As anoutput it takes the three column file from mcxdeblast and adds two additional columns coresponding to the HG ID for the query and subject.

Homology_Group_Frequency_Counting.py

This scripts counts up how blast interactions each individual protein has, for example 1 protein in a HG might blast 13 other HG, whereas another protein might only hit its own HG. The input of this script are the output of the two previous scripts. You also need to tell it which HG you want to examine from the output of MCL/Homology_Group_Frequency_Counting.py. Each HG in the output files of the MCL/Homology_Group_Frequency_Counting.py is represented on a single line, so the first line is HG 1, the second HG 2...etc. The output of this script is a tab delimited table of counts. The row headers are the HG you asked the script to examine, the column headers are all of the clusters which were found during the blast interaction checks. This table can be examined and filtered in suitable programs like R, or even excel for those who want an easy interface.
