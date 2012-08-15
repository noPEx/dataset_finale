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
