#贷后报告
afterLoanReportSql  ='''
SELECT
	p.id,
	p.batch_no,
	p.report_apply_no,
	p.bill_no,
	a.CUS_NAME,
	a.CONT_AMT,
	p.check_date,
	ccra.REPORT_DATE,
	p.risk_level,
	GROUP_CONCAT(content.red_risk_content separator '；') content,
	u.USR_NAME cust_mgr_cname,
	b.BCH_DESC main_br_id_cname,
	ccra.REPINFODIR 
FROM
	psp_batch_check p
	LEFT JOIN ( SELECT BILL_NO, CUS_ID, CUS_NAME, CONT_AMT, CUST_MGR, MAIN_BR_ID, LOAN_START_DATE, LOAN_END_DATE FROM acc_loan ) a ON p.bill_no = a.bill_no
	LEFT JOIN view_cus_all v ON a.cus_id = v.CUS_ID
	LEFT JOIN psp_batch_check_detail pbcd ON pbcd.check_id = p.id
	LEFT JOIN cus_credit_rep_app ccra ON ccra.PK_ID = pbcd.credit_rep_id
	LEFT JOIN s_usr u ON u.USR_CDE = a.CUST_MGR
	LEFT JOIN s_bch b ON b.BCH_CDE = a.MAIN_BR_ID
  LEFT JOIN cus_risk_content content ON content.credit_rep_id = pbcd.credit_rep_id 
WHERE
	batch_no != 'BP20000000001' 
	AND pbcd.id IS NOT NULL 
	AND p.check_date >= '2020-12-01' 
	AND p.check_date <= '2021-01-31'
	and exists(select 1 from (SELECT
	max(ccra.REPORT_DATE) REPORT_DATE,
	max(p.check_date) check_date,
	p.bill_no
FROM
	psp_batch_check p
	LEFT JOIN ( SELECT BILL_NO, CUS_ID, CUS_NAME, CONT_AMT, CUST_MGR, MAIN_BR_ID, LOAN_START_DATE, LOAN_END_DATE FROM acc_loan ) a ON p.bill_no = a.bill_no
	LEFT JOIN view_cus_all v ON a.cus_id = v.CUS_ID
	LEFT JOIN psp_batch_check_detail pbcd ON pbcd.check_id = p.id
	LEFT JOIN cus_credit_rep_app ccra ON ccra.PK_ID = pbcd.credit_rep_id
	LEFT JOIN s_usr u ON u.USR_CDE = a.CUST_MGR
	LEFT JOIN s_bch b ON b.BCH_CDE = a.MAIN_BR_ID
	LEFT JOIN cus_risk_content content ON content.credit_rep_id = pbcd.credit_rep_id 
WHERE
	batch_no != 'BP20000000001' 
	AND pbcd.id IS NOT NULL 
	AND p.check_date >= '2020-12-01' 
	AND p.check_date <= '2021-01-31'
	group by p.bill_no) temp where ccra.REPORT_DATE = temp.REPORT_DATE and p.bill_no = temp.bill_no and p.check_date = temp.check_date)
	group by p.id,
	p.batch_no,
	p.report_apply_no,
	p.bill_no,
	a.CUS_NAME,
	a.CONT_AMT,
	p.check_date,
	ccra.REPORT_DATE,
	p.risk_level,
	u.USR_NAME,
	b.BCH_DESC,
	ccra.REPINFODIR 
'''



CusComquery ='''


'''