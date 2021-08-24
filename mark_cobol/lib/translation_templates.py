class GCUS:

	header_record={		
		'''Literally “BOF PERSHING ” (beginning of
Pershing file)''':{
			"position":[0,17],
			"type":"X",
			"operation":"",
		},
		'''Literally “GLOBAL CUST POS ”''':{
			"position":[18,35],
			"type":"X",
			"operation":"",
		},
		'''Literally “ DATA OF ”''':{
			"position":[36,45],
			"type":"X",
			"operation":"",
		},
		'''DATE OF DATA = “MM/DD/CCYY”''':{
			"position":[46,55],
			"type":"X",
			"operation":"",
		},
		'''Literally “ TO REMOTE ”''':{
			"position":[56,66],
			"type":"X",
			"operation":"",
		},
		'''REMOTE ID = “XXXX”''':{
			"position":[67,70],
			"type":"X",
			"operation":"",
		},
		'''Literally “ BEGINS HERE ”''':{
			"position":[71,84],
			"type":"X",
			"operation":"",
		},
		'''RUN DATE = “MM/DD/CCYY”''':{
			"position":[85,94],
			"type":"X",
			"operation":"",
		},
		'''Not Used''':{
			"position":[95,95],
			"type":"X",
			"operation":"",
		},
		'''RUN TIME = “HH:MM:SS”''':{
			"position":[96,103],
			"type":"X",
			"operation":"",
		},
		'''Not Used''':{
			"position":[104,117],
			"type":"X",
			"operation":"",
		},
		'''Indicates if the file is REFRESHED/UPDATED – literally
           “REFRESHED” or “UPDATED ”''':{
			"position":[118,126],
			"type":"X",
			"operation":"",
		},
		'''Not Used''':{
			"position":[127,748],
			"type":"X",
			"operation":"",
		},
		'''Literally “A”; indicates the end of the header record''':{
			"position":[749,749],
			"type":"X",
			"operation":"",
		},

	}

	detail_record_a = {
 		'''TRANSACTION CODE; values include:
        “GC” = GCUS (Brokerage)
        “M1” = GCS1 (Bank Custody)''':{
	        "position":[0,1],
			"type":"X",
			"operation":"",
        },
 		'''RECORD INDICATOR VALUE = “A”''':{
	        "position":[2,2],
			"type":"X",
			"operation":"",
        },
 		'''RECORD ID SEQUENCE NUMBER; begins with “00000001”''':{
	        "position":[3,10],
			"type":"9",
			"operation":"",
        },
 		'''ACCOUNT NUMBER, including Office (3), Base Account (5),
        Check Digit (1), Type (1); values for Type include:
        “0” = Cash on Delivery
        “1” = Cash/Principal Accounting for Bank Custody
        “2” = Margin
		“3” = Short
		“8” = Precious Metals
		“9” = Income/Income Accounting for Bank Custody''':{
	        "position":[11,20],
			"type":"X",
			"operation":"",
        },
 		'''CUSIP® NUMBER''':{
	        "position":[21,29],
			"type":"X",
			"operation":"",
        },
 		'''PORTFOLIO CURRENCY; populated only for Bank Custody
        accounts; for Brokerage accounts, this field will be spaces''':{
	        "position":[30,32],
			"type":"X",
			"operation":"",
        },
 		'''Not Used''':{
	        "position":[33,33],
			"type":"X",
			"operation":"",
        },
 		'''UNDERLYING CUSIP NUMBER''':{
	        "position":[34,42],
			"type":"X",
			"operation":"",
        },
 		'''COUNTRY CODE; see Appendix Q for values, effective early   
		3 rd Q, 2017
        For GCS1, this represents country where trade was executed;
        includes additional value:
		“X9” = Country unknown or unavailable
		For GCUS, this represents country of security’s issuance''':{
	        "position":[43,44],
			"type":"X",
			"operation":"",
        },
 		'''Not Used''':{
	        "position":[45,46],
			"type":"X",
			"operation":"",
        },
 		'''INVESTMENT PROFESSIONAL (IP) OF RECORD NUMBER''':{
	        "position":[47,49],
			"type":"X",
			"operation":"",
        },
 		'''INTRODUCING BROKER DEALER (IBD) NUMBER''':{
	        "position":[50,52],
			"type":"X",
			"operation":"",
        },
 		'''CURRENCY/SECURITY INDICATOR; values include:
		“C” = Currency Position
		“S” = Security Position''':{
	        "position":[53,53],
			"type":"X",
			"operation":"",
        },
 		'''ISSUE CURRENCY; see Appendix N, “Currency Codes”''':{
	        "position":[54,56],
			"type":"X",
			"operation":"",
        },
 		'''DATE STAMP/TRADE DATE, in CCYYMMDD format; the
        date the TRADE DATE quantity was last updated''':{
	        "position":[57,64],
			"type":"9",
			"operation":"",
        },
 		'''DATE STAMP/SETTLEMENT DATE, in CCYYMMDD
		format; the date the S/DATE quantity was last updated''':{
	        "position":[65,72],
			"type":"9",
			"operation":"",
        },
 		'''TRADE DATE QUANTITY; number of shares traded, but not
		yet settled (add Pending/Split Quantity in Record A, 283-300, to
		this field to equal the T/D Quantity in NetX360)''':{
	        "position":[73,90],
			"type":"9",
			"operation":"div 5",
        },
 		'''TRADE DATE QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable''':{
	        "position":[91,91],
			"type":"X",
			"operation":"",
        },
 		'''SETTLEMENT DATE QUANTITY; the books and records
		position (for instance, the position shown on your clients’
		brokerage statements); it reflects all securities that are received or
		delivered and all settled trades; it does not include pending trades
		(add Pending/Split Quantity in Record A, 283-300, to this field to
		equal the S/D Quantity in NetX360)''':{
	        "position":[92,109],
			"type":"9",
			"operation":"div 5",
        },
 		'''SETTLEMENT DATE QUANTITY SIGN: values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable''':{
	        "position":[110,110],
			"type":"X",
			"operation":"",
        },
 		'''SEG QUANTITY (MEMO); the securities held in street name''':{
	        "position":[111,128],
			"type":"9",
			"operation":"div 5",
        },
 		'''SEG QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable''':{
			"position":[129,129],
			"type":"X",
			"operation":"",
        },
 		'''SAFEKEEPING QUANTITY (MEMO); number of shares
		registered in the customer’s name
		''':{
			"position":[130,147],
			"type":"9",
			"operation":"div 5",
        },
 		'''SAFEKEEPING QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable
		''':{
			"position":[148,148],
			"type":"X",
			"operation":"",
        },
 		'''TRANSFER QUANTITY (MEMO); number of shares in the
		process of being registered in the customer’s name
		''':{
			"position":[149,166],
			"type":"9",
			"operation":"div 5",
        },
 		'''TRANSFER QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable
		''':{
			"position":[167,167],
			"type":"X",
			"operation":"",
        },
 		'''PENDING TRANSFER QUANTITY; the number of shares
		currently pending the transfer process
		''':{
			"position":[168,185],
			"type":"9",
			"operation":"div 5",
        },
 		'''PENDING TRANSFER QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable
		''':{
			"position":[186,186],
			"type":"X",
			"operation":"",
        },
 		'''LEGAL TRANSFER QUANTITY; the number of shares
        awaiting clearance at the transfer agent 
		''':{
			"position":[187,204],
			"type":"9",
			"operation":"div 5",
        },
 		'''LEGAL TRANSFER QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable 
		''':{
			"position":[205,205],
			"type":"X",
			"operation":"",
        },
 		'''TENDERED (REORG) QUANTITY (MEMO); number of
		shares submitted with instructions to participate in a corporate
		reorganization (e.g., exchange, tender, redemption, etc.)
		''':{
			"position":[206,223],
			"type":"9",
			"operation":"div 5",
        },
 		'''TENDERED QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable
		''':{
			"position":[224,224],
			"type":"X",
			"operation":"",
        },
 		'''PENDING PAPERS (MEMO); number of shares pending the
		receipt of documents to make them negotiable
		''':{
			"position":[225,242],
			"type":"9",
			"operation":"div 5",
        },
 		'''PENDING PAPERS SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable
		''':{
			"position":[243,243],
			"type":"X",
			"operation":"",
        },
 		'''SHORT AGAINST THE BOX QUANTITY (MEMO)''':{
			"position":[244,261],
			"type":"9",
			"operation":"div 5",
        },
 		'''SHORT AGAINST THE BOX QTY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable''':{
			"position":[262,262],
			"type":"X",
			"operation":"",
        },
 		'''NETWORKED QUANTITY (MEMO)''':{
			"position":[263,280],
			"type":"9",
			"operation":"div 5",
        },
 		'''NETWORKED QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable''':{
			"position":[281,281],
			"type":"X",
			"operation":"",
        },
 		'''PENDING SPLIT QUANTITY (MEMO); quantity of the
		security that is subject to a pending stock distribution''':{
			"position":[282,299],
			"type":"9",
			"operation":"div 5",
        },
 		'''PENDING SPLIT QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable''':{
			"position":[300,300],
			"type":"X",
			"operation":"",
        },
 		'''QUANTITY COVERING OPTIONS or COVERED QTY''':{
			"position":[301,318],
			"type":"9",
			"operation":"div 5",
        },
 		'''QUANTITY COVERING OPTIONS or COVERED
		QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable''':{
			"position":[319,319],
			"type":"X",
			"operation":"",
        },
 		'''TRADE DATE QUANTITY BOUGHT''':{
			"position":[320,337],
			"type":"9",
			"operation":"div 5",
        },
 		'''TRADE DATE QUANTITY BOUGHT SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicablee''':{
			"position":[338,338],
			"type":"X",
			"operation":"",
        },
 		'''TRADE DATE QUANTITY SOLD''':{
			"position":[339,356],
			"type":"9",
			"operation":"div 5",
        },
 		'''TRADE DATE QUANTITY SOLD SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable''':{
			"position":[357,357],
			"type":"X",
			"operation":"",
        },
 		'''FED (REG T) REQUIREMENT''':{
			"position":[358,375],
			"type":"9",
			"operation":"div 5",
        },
 		'''FED REQUIREMENT SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[376,376],
			"type":"X",
			"operation":"",
        },
 		'''HOUSE (PERSHING) MARGIN REQUIREMENT''':{
			"position":[377,394],
			"type":"9",
			"operation":"dev 5",
        },
 		'''HOUSE MARGIN REQUIREMENT SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[395,395],
			"type":"X",
			"operation":"",
        },
 		'''EXCHANGE (NYSE) REQUIREMENT''':{
			"position":[396,413],
			"type":"9",
			"operation":"div 5",
        },
 		'''EXCHANGE REQUIREMENT SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[414,414],
			"type":"X",
			"operation":"",
        },
 		'''EQUITY REQUIREMENT''':{
			"position":[415,432],
			"type":"9",
			"operation":"div 5",
        },
 		'''EQUITY REQUIREMENT SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[433,433],
			"type":"X",
			"operation":"",
        },
 		'''SECURITY SYMBOL''':{
			"position":[434,442],
			"type":"X",
			"operation":"",
        },
 		'''SECURITY TYPE; see Appendix B, “Security Code Matrix”''':{
			"position":[443,443],
			"type":"X",
			"operation":"",
        },
 		'''SECURITY MOD; see Appendix B, “Security Code Matrix”''':{
			"position":[444,444],
			"type":"X",
			"operation":"",
        },
 		'''SECURITY CALC; see Appendix B, “Security Code Matrix”''':{
			"position":[445,445],
			"type":"X",
			"operation":"",
        },
 		'''MINOR PRODUCT CODE; See Appendix B''':{
			"position":[446,448],
			"type":"X",
			"operation":"",
        },
 		'''NETWORK ELIGIBILITY INDICATOR''':{
			"position":[449,449],
			"type":"X",
			"operation":"",
        },
 		'''STRIKE PRICE''':{
			"position":[450,467],
			"type":"9",
			"operation":"div 9",
        },
 		'''STRIKE PRICE SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[468,468],
			"type":"X",
			"operation":"",
        },
 		'''EXPIRATION/MATURITY DATE, in CCYYMMDD''':{
			"position":[469,476],
			"type":"9",
			"operation":"",
        },
 		'''CONTRACT SIZE''':{
			"position":[477,494],
			"type":"9",
			"operation":"div 5",
        },
 		'''CONVERSION RATIO''':{
			"position":[495,512],
			"type":"9",
			"operation":"div 9",
        },
 		'''ACCOUNT SHORT NAME''':{
			"position":[513,522],
			"type":"X",
			"operation":"",
        },
 		'''STATE CODE''':{
			"position":[523,525],
			"type":"X",
			"operation":"",
        },
 		'''COUNTRY CODE (of account-level citizenship)''':{
			"position":[526,528],
			"type":"X",
			"operation":"",
        },
 		'''For Pershing Internal Use''':{
			"position":[529,532],
			"type":"X",
			"operation":"",
        },
 		'''NUMBER OF SECURITY DESCRIPTION LINES''':{
			"position":[533,536],
			"type":"9",
			"operation":"",
        },
 		'''SECURITY DESCRIPTION LINE 1''':{
			"position":[537,556],
			"type":"X",
			"operation":"",
        },
 		'''SECURITY DESCRIPTION LINE 2''':{
			"position":[556,576],
			"type":"X",
			"operation":"",
        },
 		'''SECURITY DESCRIPTION LINE 3''':{
			"position":[577,596],
			"type":"X",
			"operation":"",
        },
 		'''SECURITY DESCRIPTION LINE 4''':{
			"position":[597,616],
			"type":"X",
			"operation":"",
        },
 		'''SECURITY DESCRIPTION LINE 5''':{
			"position":[617,636],
			"type":"X",
			"operation":"",
        },
 		'''SECURITY DESCRIPTION LINE 6''':{
			"position":[637,656],
			"type":"X",
			"operation":"",
        },
 		'''DIVIDEND OPTION (applies to Equities and Mutual funds
		only); values include:
		“C” = Cash
		“R” = Reinvest
		“ ” = Not Applicable''':{
			"position":[657,657],
			"type":"X",
			"operation":"",
        },
 		'''LONG TERM CAPITAL GAINS OPTION (applies to Mutual
		Funds only); values include:
		“C” = Cash
		“R” = Reinvest
		“ ” = Not Applicable''':{
			"position":[658,658],
			"type":"X",
			"operation":"",
        },
 		'''SHORT TERM CAPITAL GAINS OPTION (applies to both
		Equities and Mutual Funds); values include:
		“C” = Cash
		“R” = Reinvest
		“ ” = Not Applicable''':{
			"position":[659,659],
			"type":"X",
			"operation":"",
        },
 		'''FIRM TRADING INDICATOR''':{
			"position":[660,660],
			"type":"X",
			"operation":"",
        },
 		'''POSITION CURRENCY''':{
			"position":[661,663],
			"type":"X",
			"operation":"",
        },
 		'''TRADE DATE LIQUIDATING VALUE (add Pending Split
		Quantity Liquidating Value in Record B, 454-471, to this field to
		equal the T/D Liquidating Value displayed on NetX360)
		''':{
			"position":[664,681],
			"type":"9",
			"operation":"div 3",
        },
 		'''TRADE DATE LIQUIDATING VALUE SIGN; values include:
		“+” = Long Market Value
		“-” = Short Market Value
		“ ” = Not Applicable
		''':{
			"position":[682,682],
			"type":"X",
			"operation":"",
        },
 		'''POOL FACTOR''':{
			"position":[683,692],
			"type":"9",
			"operation":"div 8",
        },
 		'''POOL FACTOR SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[693,693],
			"type":"X",
			"operation":"",
        },
 		'''EXCHANGE RATE''':{
			"position":[694,711],
			"type":"9",
			"operation":"div 10",
        },
 		'''EXCHANGE RATE SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[712,712],
			"type":"X",
			"operation":"",
        },
 		'''SETTLEMENT DATE LIQUIDATING VALUE (add Pending
		Split Quantity Liquidating Value in Record B, 454-471, to this
		field to equal the S/D Liquidating Value displayed on NetX360)''':{
			"position":[713,730],
			"type":"9",
			"operation":"div 3",
        },
 		'''SETTLEMENT DATE LIQUIDATING VALUE SIGN; values
		include:
		“+” = Long Market Value
		“-” = Short Market Value
		“ ” = Not Applicable''':{
			"position":[731,731],
			"type":"X",
			"operation":"",
        },
 		'''For Internal Pershing Use (Display Currency)''':{
			"position":[732,734],
			"type":"X",
			"operation":"",
        },
 		'''ALTERNATE SECURITY ID TYPE, value includes:
		“I” = ISIN''':{
			"position":[735,735],
			"type":"X",
			"operation":"",
        },
 		'''ALTERNATE SECURITY ID''':{
			"position":[736,747],
			"type":"X",
			"operation":"",
        },
 		'''For Pershing Internal Use Only''':{
			"position":[748,748],
			"type":"X",
			"operation":"",
        },
 		'''Literally “X”; indicates the end of detail record A''':{
			"position":[749,749],
			"type":"X",
			"operation":"",
        },

	}
	detail_record_b = {
 		'''TRANSACTION CODE; values include:
		“GC” = GCUS (Brokerage)
		“M1” = GCS1 (Bank Custody)''':{
	        "position":[0,1],
			"type":"X",
			"operation":"",
        },
 		'''RECORD INDICATOR VALUE = “B”''':{
	        "position":[2,2],
			"type":"X",
			"operation":"",
        },
 		'''RECORD ID SEQUENCE NUMBER; begins with “00000001”''':{
	        "position":[3,10],
			"type":"9",
			"operation":"",
        },
 		'''ACCOUNT NUMBER, including Office (3), Base Account (5),
        Check Digit (1), Type (1) (see A, pos. 021, for values for Type)''':{
	        "position":[11,20],
			"type":"X",
			"operation":"",
        },
 		'''CUSIP NUMBER''':{
	        "position":[21,29],
			"type":"X",
			"operation":"",
        },
 		'''PORTFOLIO CURRENCY; populated only for Bank Custody
		accounts; for Brokerage accounts, this field will be spaces''':{
	        "position":[30,32],
			"type":"X",
			"operation":"",
        },
 		'''Not Used''':{
	        "position":[33,33],
			"type":"X",
			"operation":"",
        },
 		'''UNDERLYING CUSIP NUMBER''':{
	        "position":[34,42],
			"type":"X",
			"operation":"",
        },
 		'''COUNTRY CODE; see Appendix Q for values, effective early
		3 rd Q, 2017, TBA:
		For GCS1, this represents country where trade was executed;
		includes additional value:
		“X9” = Country unknown or unavailable
		For GCUS, this represents country of security’s issuance''':{
	        "position":[43,44],
			"type":"X",
			"operation":"",
        },
 		'''Not Used''':{
	        "position":[45,46],
			"type":"X",
			"operation":"",
        },
 		'''INVESTMENT PROFESSIONAL (IP) OF RECORD NUMBER''':{
	        "position":[47,49],
			"type":"X",
			"operation":"",
        },
 		'''INTRODUCING BROKER DEALER (IBD) NUMBER''':{
	        "position":[50,52],
			"type":"X",
			"operation":"",
        },
 		'''FULLY PAID LENDING QUANTITY''':{
	        "position":[53,70],
			"type":"9",
			"operation":"div 5",
        },
 		'''FULLY PAID LENDING QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity''':{
	        "position":[71,71],
			"type":"X",
			"operation":"",
        },
 		'''FULLY PAID LENDING QUANTITY COLLATERAL AMT''':{
	        "position":[72,89],
			"type":"9",
			"operation":"div 3",
        },
 		'''FULLY PAID LENDING QUANTITY COLLATERAL
		AMOUNT SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount''':{
	        "position":[90,90],
			"type":"X",
			"operation":"",
        },
 		'''OPTION ROOT ID''':{
	        "position":[91,96],
			"type":"X",
			"operation":"",
        },
 		'''EXPIRATION DATE, in YYMMDD format''':{
	        "position":[97,102],
			"type":"9",
			"operation":"",
        },
 		'''CALL/PUT INDICATOR, values include:
		“B” = Bank Pledge (Call)
		“C” = Call
		“D” = Bank Pledge (Put)
		“E” = Escrow Receipt
		“L” = Letter of Credit (Call)
		“M” = Letter of Credit (Put)
		“P” = Put''':{
	        "position":[103,103],
			"type":"X",
			"operation":"div 5",
        },
 		'''STRIKE PRICE''':{
	        "position":[104,111],
			"type":"9",
			"operation":"div 3",
        },
 		'''TRADE DATE REPO QUANTITY''':{
	        "position":[112,129],
			"type":"9",
			"operation":"div 5",
        },
 		'''TRADE DATE REPO QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable''':{
			"position":[130,130],
			"type":"X",
			"operation":"",
        },
 		'''SETTLEMENT DATE REPO QUANTITY''':{
			"position":[131,148],
			"type":"9",
			"operation":"div 5",
        },
 		'''SETTLEMENT DATE REPO QUANTITY SIGN; values
		include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable
		''':{
			"position":[149,149],
			"type":"X",
			"operation":"",
        },
 		'''TRADE DATE REVERSE REPO QUANTITY''':{
			"position":[150,167],
			"type":"9",
			"operation":"div 5",
        },
 		'''T/D REVERSE REPO QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable
		''':{
			"position":[168,168],
			"type":"X",
			"operation":"",
        },
 		'''SETTLEMENT DATE REVERSE REPO QUANTITY''':{
			"position":[169,186],
			"type":"9",
			"operation":"div 5",
        },
 		'''S/D REVERSE REPO QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable
		''':{
			"position":[187,187],
			"type":"X",
			"operation":"",
        },
 		'''COLLATERAL PLEDGE QUANTITY''':{
			"position":[188,205],
			"type":"9",
			"operation":"div 5",
        },
 		'''COLLATERAL PLEDGE QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable
		''':{
			"position":[206,206],
			"type":"X",
			"operation":"",
        },
 		'''CORPORATE EXECUTIVE SERVICES COLLATERAL
		PLEDGE QUANTITY''':{
			"position":[207,224],
			"type":"9",
			"operation":"div 5",
        },
 		'''CORPORATE EXECUTIVE SERVICES COLLATERAL
		PLEDGE QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable
		''':{
			"position":[225,225],
			"type":"X",
			"operation":"",
        },
 		'''TRADE DATE REPO LIQUIDATING VALUE''':{
			"position":[226,243],
			"type":"9",
			"operation":"div 3",
        },
 		'''T/D REPO LIQUIDATING VALUE SIGN; values include:
		“+” = Long Market Value
		“-” = Short Market Value
		“ ” = Not Applicable''':{
			"position":[244,244],
			"type":"X",
			"operation":"",
        },
 		'''SETTLEMENT DATE REPO LIQUIDATING VALUE''':{
			"position":[245,262],
			"type":"9",
			"operation":"div 3",
        },
 		'''S/D REPO LIQUIDATING VALUE SIGN; values include:
		“+” = Long Market Value
		“-” = Short Market Value
		“ ” = Not Applicable''':{
			"position":[263,263],
			"type":"X",
			"operation":"",
        },
 		'''TRADE DATE REVERSE REPO LIQUIDATING VALUE''':{
			"position":[264,281],
			"type":"9",
			"operation":"div 3",
        },
 		'''T/D REVERSE REPO LIQUIDATING VALUE SIGN; values
		include:
		“+” = Long Market Value
		“-” = Short Market Value
		“ ” = Not Applicable''':{
			"position":[282,282],
			"type":"X",
			"operation":"",
        },
 		'''SETTLEMENT DATE REVERSE REPO LIQUIDATING VALUE''':{
			"position":[283,300],
			"type":"9",
			"operation":"div 3",
        },
 		'''SETTLEMENT DATE REVERSE REPO LIQUIDATING
		VALUE SIGN; values include:
		“+” = Long Market Value
		“-” = Short Market Value
		“ ” = Not Applicable
		''':{
			"position":[301,301],
			"type":"X",
			"operation":"",
        },
 		'''COLLATERAL PLEDGE LIQUIDATING VALUE''':{
			"position":[302,319],
			"type":"9",
			"operation":"div 3",
        },
 		'''COLLATERAL PLEDGE LIQUIDATING VALUE SIGN;
		values include:
		“+” = Long Market Value
		“-” = Short Market Value
		“ ” = Not Applicable''':{
			"position":[320,320],
			"type":"X",
			"operation":"",
        },
 		'''CORPORATE EXECUTIVE SERVICES COLLATERAL
		PLEDGE LIQUIDATING VALUE''':{
			"position":[321,338],
			"type":"9",
			"operation":"div 3",
        },
 		'''CORPORATE EXECUTIVE SERVICES COLLATERAL
		PLEDGE LIQUIDATING VALUE SIGN; values include:
		“+” = Long Market Value
		“-” = Short Market Value
		“ ” = Not Applicable''':{
			"position":[339,339],
			"type":"X",
			"operation":"",
        },
 		'''TRADE DATE REPO LOAN AMOUNT''':{
			"position":[340,357],
			"type":"9",
			"operation":"div 3",
        },
 		'''T/D REPO LOAN AMOUNT SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[358,358],
			"type":"X",
			"operation":"",
        },
 		'''SETTLEMENT DATE REPO LOAN AMOUNT''':{
			"position":[359,376],
			"type":"9",
			"operation":"div 3",
        },
 		'''S/D REPO LOAN AMOUNT SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[377,377],
			"type":"X",
			"operation":"",
        },
 		'''TRADE DATE REVERSE REPO LOAN AMOUNT''':{
			"position":[378,395],
			"type":"9",
			"operation":"dev 3",
        },
 		'''T/D REVERSE REPO LOAN AMOUNT SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[396,396],
			"type":"X",
			"operation":"",
        },
 		'''SETTLEMENT DATE REVERSE REPO LOAN AMOUNT''':{
			"position":[397,414],
			"type":"9",
			"operation":"div 3",
        },
 		'''S/D REVERSE REPO LOAN AMOUNT SIGN; values include:
		“+” = Positive Amount
		“-” = Negative Amount
		“ ” = Not Applicable''':{
			"position":[415,415],
			"type":"X",
			"operation":"",
        },
 		'''ACCRUED INTEREST VALUE FROM LAST PAYABLE
		DATE; based on trade date quantity''':{
			"position":[416,433],
			"type":"9",
			"operation":"div 3",
        },
 		'''ACCRUED INTEREST VALUE SIGN; values include:
		“+” = Positive Value
		“-” = Negative Value
		“ ” = Not Applicable
		''':{
			"position":[434,434],
			"type":"X",
			"operation":"",
        },
 		'''DIVIDEND or COUPON RATE''':{
			"position":[435,452],
			"type":"9",
			"operation":"div 9",
        },
 		'''PENDING SPLIT QUANTITY LIQUIDATING VALUE (add
		this value to T/D or S/D Liquidating Values in Record A to equal
		Market Value displayed on NetX360); effective 08/02/2013
		”''':{
			"position":[453,470],
			"type":"9",
			"operation":"div 3",
        },
 		'''PENDING SPLIT QUANTITY LIQUIDATING VALUE SIGN;
		values include:
		“+” = Long Market Value
		“-” = Short Market Value
		“ ” = Not Applicable''':{
			"position":[471,471],
			"type":"X",
			"operation":"",
        },
 		'''For Pershing Internal Use Only''':{
			"position":[472,509],
			"type":"X",
			"operation":"",
        },
 		'''INTERNATIONAL NON-DOLLAR SYMBOL (effective
		02/07/2014)
		''':{
			"position":[510,525],
			"type":"X",
			"operation":"",
        },
 		'''PLEDGED QUANTITY (MEMO), applies only to brokerage;
		effective mid-2
		nd Q, 2017
		''':{
			"position":[526,543],
			"type":"9",
			"operation":"div 5",
        },
 		'''PLEDGED QUANTITY SIGN; values include:
		“+” = Long Quantity
		“-” = Short Quantity
		“ ” = Not Applicable''':{
			"position":[544,544],
			"type":"X",
			"operation":"div 9",
        },
 		'''Not Used''':{
			"position":[545,748],
			"type":"X",
			"operation":"",
        },
 		'''Literally “X”; indicates the end of detail record B''':{
			"position":[749,749],
			"type":"X",
			"operation":"",
        },
	}
	trailer_record = {
 		'''Literally “EOF PERSHING ” (end of Pershing
		file)''':{
	        "position":[0,17],
			"type":"X",
			"operation":"",
        },
 		'''Literally “GLOBAL CUST POS ”''':{
	        "position":[18,35],
			"type":"X",
			"operation":"",
        },
 		'''Literally “ DATA OF ”''':{
	        "position":[36,45],
			"type":"9",
			"operation":"",
        },
 		'''DATE OF DATA = “MM/DD/CCYY”''':{
	        "position":[46,55],
			"type":"X",
			"operation":"",
        },
 		'''Literally “ TO REMOTE ”''':{
	        "position":[56,66],
			"type":"X",
			"operation":"",
        },
 		'''REMOTE ID = “XXXX”''':{
	        "position":[67,70],
			"type":"X",
			"operation":"",
        },
 		'''Literally“ ENDS HERE. TOTAL DETAIL
		RECORDS: ”''':{
	        "position":[71,104],
			"type":"X",
			"operation":"",
        },
 		'''NUMBER OF DETAIL RECORDS''':{
	        "position":[105,114],
			"type":"9",
			"operation":"",
        },
 		'''Not Used''':{
	        "position":[115,117],
			"type":"X",
			"operation":"",
        },
 		'''Indicates if the file is REFRESHED/UPDATED – literally
		“REFRESHED” or “UPDATED ”''':{
	        "position":[118,126],
			"type":"X",
			"operation":"",
        },
 		'''Not Used''':{
	        "position":[127,748],
			"type":"X",
			"operation":"",
        },
 		'''Literally “Z”; indicates the end of the trailer record''':{
	        "position":[749,749],
			"type":"X",
			"operation":"",
        },
 	
	}

		


