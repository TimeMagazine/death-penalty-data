class Execution(object):

	ICPSRStudyNumber8451 = ""
	ICPSRSEditionNumber = ""
	ICPSRPartNumber = ""
	CaseNumber = ""
	RaceOfOffender = ""
	AgeAtExecution = ""
	NameOfOffender = ""
	PlaceOfExecution = ""
	JurisdictionOfExecution = ""
	CrimeCommitted = ""
	MethodOfExecution = ""
	DateDay = ""
	DateMonth = ""
	DateYear = ""
	CheckDigit = ""
	StateOfExecution = ""
	CountyOfConviction = ""
	ICPSRStateCode = ""
	SexOfOffender = ""
	CompensationCase = ""
	OccupationOfOffender = ""

	def getExecution(current_execution):
		execution = {}
		execution['ICPSRStudyNumber8451'] = current_execution.ICPSRStudyNumber8451
		execution['ICPSRSEditionNumber'] = current_execution.ICPSRSEditionNumber
		execution['ICPSRPartNumber'] = current_execution.ICPSRPartNumber
		execution['CaseNumber'] = current_execution.CaseNumber
		execution['RaceOfOffender'] = current_execution.RaceOfOffender
		execution['AgeAtExecution'] = current_execution.AgeAtExecution
		execution['NameOfOffender'] = current_execution.NameOfOffender
		execution['PlaceOfExecution'] = current_execution.PlaceOfExecution
		execution['JurisdictionOfExecution'] = current_execution.JurisdictionOfExecution
		execution['CrimeCommitted'] = current_execution.CrimeCommitted
		execution['MethodOfExecution'] = current_execution.MethodOfExecution
		execution['DateDay'] = current_execution.DateDay
		execution['DateMonth'] = current_execution.DateMonth
		execution['DateYear'] = current_execution.DateYear
		execution['CheckDigit'] = current_execution.CheckDigit
		execution['StateOfExecution'] = current_execution.StateOfExecution
		execution['CountyOfConviction'] = current_execution.CountyOfConviction
		execution['ICPSRStateCode'] = current_execution.ICPSRStateCode
		execution['SexOfOffender'] = current_execution.SexOfOffender
		execution['CompensationCase'] = current_execution.CompensationCase
		execution['OccupationOfOffender'] = current_execution.OccupationOfOffender
		return execution