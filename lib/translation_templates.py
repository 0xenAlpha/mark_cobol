class GCUS:

	detail_record_A={		
		'''TRANSACTION CODE; values include:
“GC” = GCUS (Brokerage)
“M1” = GCS1 (Bank Custody)''':{
			"position":[0,2],
			"type":"X",
			"operation":"",
		},
		'''TRADE DATE QUANTITY; number of shares traded, but not
yet settled (add Pending/Split Quantity in Record A, 283-300, to
this field to equal the T/D Quantity in NetX360)''':{
			"position":[73,91],
			"type":"9",
			"operation":"div 5",
		},

	}


