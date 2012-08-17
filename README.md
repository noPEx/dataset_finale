dataset_finale
==============

This is the dataset that is going to be used for interoperability analysis. Can be found in Data/august_data.

This files tells you the details
./command.sh :
	some command
./common_files.txt :
	The files that are common in each directory. In here the strings that are common in each file that are passed as argument to our script.

./intersection.py :
	Given a set of files returns the strings that are common in each file

./Phase1/Futronic_files.txt :
	The files that are from Futronic device.
	From Phase1
./Phase1/Lumidigm_files.txt
	The files that are from Futronic device.
	From Phase1
./Phase1/Secugen_files.txt
	The files that are from Futronic device.
	From Phase1
./Phase2
./Phase2/Futronic_files.txt
	The files that are from Futronic device.
	From Phase2
./Phase2/Lumidigm_files.txt
	The files that are from Futronic device.
	From Phase2
./Phase2/Secugen_files.txt
	The files that are from Futronic device.
	From Phase2

./test_data.txt :
	100 or so files that are to be used for testing.

src_files/ :
	Contain the files that are consistent across each device and each phase. The files are named accordingly
src_files/Fut_phase1
src_files/Fut_phase2
src_files/Lum_phase1
src_files/Lum_phase2
src_files/Sec_phase1
src_files/Sec_phase2
src_files/test_data.txt

./scores/ 
	: The scores could be found here
./scores/lumi_vs_sec_august_imposter_scores_sec.txt
	: Lumidigm vs Secugen imposter scores using sec's matcher. Inputs in Lum_phase1 vs Sec_phase1_reverse

./scores/fut_vs_sec_august_genuine_scores_lum.txt 
	: Futronic vs Secugen  genuine scores using Lumidigm's matcher. Inputs in Fut_phase1 vs Sec_phase1

./scores/fut_vs_sec_august_genuine_scores_sec.txt 
	: Futronic vs Secugen  genuine scores using Secugen's matcher. Inputs in Fut_phase1 vs Sec_phase1

./scores/fut_vs_sec_august_imposter_scores_lum.txt 
	: Futronic vs Secugen  imposter scores using Secugen's matcher. Inputs in Fut_phase1 vs Sec_phase1_reverse


./scores/fut_vs_sec_august_imposter_scores_sec.txt 
	: Futronic vs Secugen  imposter scores using Secugen's matcher. Inputs in  Fut_phase1 vs Sec_phase1_reverse 


./scores/lumi_vs_fut_august_genuine_scores_lum.txt  
	: Lumidigm vs Futronic  genuine scores using Lumidigm's matcher. Inputs in Lum_phase1 vs Fut_phase1


./scores/lumi_vs_fut_august_genuine_scores_sec.txt 
	: Lumidigm vs Futronic  genuine scores using Secugen's matcher. Inputs in Lum_phase1 vs Fut_phase1


./scores/lumi_vs_fut_august_imposter_scores_lum.txt 
	: Lumidigm vs Futronic imposter scores using Lumidigm's matcher. Inputs in Lum_phase1 vs Fut_phase1_reverse



./scores/lumi_vs_fut_august_imposter_scores_sec.txt 
	: Lumidigm vs Futronic imposter scores using Secugen's matcher. Inputs in Lum_phase1 vs Fut_phase1_reverse


./scores/lumi_vs_sec_august_genuine_scores_lum.txt
	: Lumidigm vs Secugen   genuine scores using Lumidigm's matcher. Inputs in  Lum_phase1 vs Sec_phase1


./scores/lumi_vs_sec_august_genuine_scores_sec.txt
	: Lumidigm vs Secugen   genuine scores using Secugen's matcher. Inputs in   Lum_phase1 vs Sec_phase1

./scores/lumi_vs_sec_august_imposter_scores_lum.txt
	: Lumidigm vs Secugen  imposter scores using Lumidigm's matcher. Inputs in   Lum_phase1 vs Sec_phase1_reverse


./scores/scores_matching_fut_vs_fut_genuine_via_lumi.txt 
	: Futronic vs Futronic  genuine scores using Lumidigm's matcher. Inputs in  Fut_phase1 vs Fut_phase2


./scores/scores_matching_fut_vs_fut_genuine_via_secu.txt 
	: Futronic vs Futronic  genuine scores using Secugen's matcher. Inputs in  Fut_phase1 vs Fut_phase2


./scores/scores_matching_fut_vs_fut_imposter_via_lumi.txt 
	: Futronic vs Futronic imposter scores using Lumidigm's matcher. Inputs in  Fut_phase1 vs Fut_phase2_reverse



./scores/scores_matching_fut_vs_fut_imposter_via_secu.txt 
	: Futronic vs Futronic imposter scores using Secugen's matcher. Inputs in  Fut_phase1 vs Fut_phase2_reverse


./scores/scores_matching_genuine_lum_vs_lum_via_lumi.txt 
	: Lumidigm vs Lumidigm  genuine scores using Lumidigm's matcher. Inputs in Lum_phase1 vs Lum_Phase2


./scores/scores_matching_genuine_lum_vs_lum_via_secu.txt
	: Lumidigm vs Lumidigm   genuine scores using Secugen's matcher. Inputs in  Lum_phase1 vs Lum_phase2

./scores/scores_matching_imposter_lum_vs_lum_via_lumi.txt 
	: Lumidigm vs Lumidigm imposter scores using Lumidigm's matcher. Inputs in Lum_phase1 vs Lum_phase2_reverse



./scores/scores_matching_imposter_lum_vs_lum_via_secu.txt 
	: Lumidigm vs Lumidigm imposter scores using Secugen's matcher. Inputs in Lum_phase1 vs Lum_phase2_reverse


./scores/scores_matching_sec_vs_sec_august_genuine_lumi.txt 
	: Secugen vs Secugen genuine scores using  Lumidigm's matcher. Inputs in Sec_phase1 vs   Sec_phase2 

./scores/scores_matching_sec_vs_sec_august_genuine_secu.txt 
	: Secugen vs Secugen  genuine scores using Secugen's matcher. Inputs in Sec_phase1 vs    Sec_phase2


./scores/scores_sec_vs_sec_august_imposter_lumi.txt 
	: Secugen vs Secugen imposter scores using Lumidigm's matcher. Inputs in Sec_phase1 vs    Sec_phase2_reverse


./scores/scores_sec_vs_sec_august_imposter_secu.txt 
	: Secugen vs Secugen imposter scores using Secugen's matcher. Inputs in Sec_phase1 vs   Sec_phase2_reverse

