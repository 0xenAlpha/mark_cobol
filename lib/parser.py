



from lib.utils import format_dev, list_from_file, log_w, workspace_path_join
from lib.excel_lib import add_row_to_excel_file, excel_file_init, save_excel_file
from lib.translation_templates import GCUS

class Parser():

	def __init__(self,files_to_process) -> None:	
		self.wb,self.ws = excel_file_init(list(GCUS.detail_record_a.keys()))
		self.headers=list(GCUS.detail_record_a.keys())
		# for header in self.headers:			
		# 	GCUS.header_record[header]["position"][-1]=GCUS.header_record[header]["position"][-1]+1
		# log_w(workspace_path_join("output/header_record"),str(GCUS.detail_record_a))
		# exit()
		self.files_to_process=files_to_process

	def run(self):
		for file in self.files_to_process:
			self.file_path = workspace_path_join(file)
			self.output_file_path = workspace_path_join("output/"+file.split("/")[-1])			
			print(self.file_path,self.output_file_path)
			self.translate()

	def translate(self):
		self.raw_file_lines = list_from_file(self.file_path)
		for line in self.raw_file_lines[2:]:
			# line='GCA00000002JVD0010061F8586HW23    F8586HW23FR  T01JVESUSD2019012520190125000000024000000000+000000024000000000+000000024000000000+000000000000000000+000000000000000000+000000000000000000+000000000000000000+000000000000000000+000000000000000000+000000000000000000+000000000000000000+000000000000000000+000000000000000000+000000000000000000+000000000000000000+000000000024282432+000000000024282432+000000000004856486+000000000000000000+F8586HW23510529 000000000000000000+20220110000000000000000000000000000000000000IBARRAALBE50050056000006SOCIETE GENERALE    MEDIUM TERM NOTES   LKD TO MFPWAAE LX   ISIN#XS1864658064    0.000% 01/10/22 REGDTD 10/30/18           NUSD000000000242824320+0000000000+000000010000000000+000000000242824320+USDIXS1864658064 X'
			row=[]
			for header in self.headers:
				position = GCUS.detail_record_a[header]["position"]
				type =GCUS.detail_record_a[header]["type"]
				operation = GCUS.detail_record_a[header]["operation"]
				# print(position,type,operation)				
				data=line[position[0]:position[1]]
				if operation:
					if "div" in operation and data.replace("+","").replace(" ","").strip():
						dev_by = int(operation.split(" ")[-1])
						dev_by  = format_dev(dev_by)		
						try:										
							data_o=float(data.replace("+","").replace(" ","").strip())/dev_by
							data=data_o
						except:
							pass
				row.append(data)
			add_row_to_excel_file(self.ws,row)
			save_excel_file(self.wb,self.output_file_path)								





	