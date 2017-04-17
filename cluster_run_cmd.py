##############################################################################################
#                                                                                            #                                                                               
# File          : cluster_run_cmd.py                                                         #
# Author        : Shubham - shubham.git@gmail.com                                            #
# Description   : This script takes list of hosts as arguments and then prompts user to      #
#		  give command to be executed on all hosts. Then script prints the output    #
# Usage         : python cluster_run_cmd.py <hostname1,hostname2>                            #
##############################################################################################

#! /usr/bin/python
import os
import sys

''' This function splits the hostnames string and returns a list contaings hosts'''
def get_hostnames(host_names) :
	return host_names.split(',')

''' Get the command that will be executed on each host'''
def get_cmd() :
	return raw_input("[%s $:] " % (os.getlogin()))

''' Run command on each host and print the output'''
def run_cmd(host_list, cmd) :
	print "cmd: \"%s\" will be executed on given hosts." % (cmd) 
	for host in host_list:
		print "Host : %s " % (host)
		print "---------------------------------------------------"
		print "[output]"
		run_cmd = "ssh " + host + " " + cmd
		os.system(run_cmd)
		print "---------------------------------------------------\n\n"

''' Show the help for this script '''
def show_help() :
	print "\nUsage: python cluster_run_cmd.py <hostname1,hostname2> \n"

''' main function '''
if __name__ == '__main__':
	if len(sys.argv) != 2 :
		print "1 arguements required, %d given " % (len(sys.argv)-1)
		show_help()
	else :
		host_list = get_hostnames(sys.argv[1])
		cmd = get_cmd()
		run_cmd(host_list, cmd)
