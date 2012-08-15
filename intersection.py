#! /usr/bin/python
import sys
"""
	Given a set of text files where each file contains name of files linewise
	gives the intersection back. i.e the strings which are in every file
"""


if __name__ == "__main__" :
	num_files = len( sys.argv ) - 1

	fs = [ open( sys.argv[i] ) for i in range( 1,num_files+1 ) ] #f's
	#print fs
	fs_lines = [ f.readlines() for f in fs ]

	#print fs_lines

	common_files = set( fs_lines[0] )	

	for files in fs_lines :
		common_files = common_files & set( files ) 
	
	common_files = list( common_files )
	common_files.sort()
	print "".join( common_files )
	#print "".join( list(common_files).sort() )
