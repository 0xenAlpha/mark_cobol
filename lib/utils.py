import os
from pathlib import Path

def workspace_path_join(filepath):    
	return os.path.join(Path(__file__).parents[1],filepath)   


def eval_file(filename):
	with open(filename,"r") as f:
		return eval(f.read())    	


def list_from_file(filename):
	try:
		with open(filename) as f:    	
			return [x.strip() for x in f.readlines()]			
	except:
		print("file not found : %s"%filename)
		return []			


def log_w(log_file,data):
	if "/"==log_file[0]:
		log_file=log_file[1:]
	with open(log_file,"w") as f:
		f.write(data)		

def format_dev(dev_by):	
	d=10
	l=1
	for _ in range(dev_by):
		l*=10
	return l