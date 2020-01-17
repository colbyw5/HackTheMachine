import pandas as pd

# Rename columns to be formatted in snake case so they're easier to query
def rename_columns_in_snake_case(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')

### MAF DATA
maf_data = pd.read_csv("Data/HTM_MAF_Data_Final.csv")
rename_columns_in_snake_case(maf_data)
print("Total number of rows in MAF Data:", maf_data.shape[0])
print("Columns in MAF Data:", maf_data.columns)
print()

print("Unique values in Aircraft column:", maf_data.aircraft.unique())
print("Unique values in Transaction Code column:", maf_data.transaction_code.unique())
print("Unique values in Malfunction Code column:", maf_data.malfunction_code.unique())
print("Unique values in Action Taken Code column:", maf_data.action_taken_code.unique())
print("Unique values in Description of Problem column:", maf_data.description_of_problem.unique())
print("Unique values in Correction of Problem column:", maf_data.correction_of_problem.unique())
print("Unique values in Received Date column:", maf_data.received_date.unique())
print("Unique values in Completion Date column:", maf_data.completion_date.unique())

# Get all corrosion rows
corrosion = maf_data[maf_data.corrosion == "Yes"]
print("Number of corrosion:", corrosion.shape[0])

# Get all bare metal rows
bare_metal = maf_data[maf_data.bare_metal == "Yes"]
print("Number of bare metal:", bare_metal.shape[0])

# Get all corrosion prevention treatments
corrosion_prevention_treatments = maf_data[maf_data.corrosion_prevention_treatment == "Yes"]
print("Number of corrosion prevention treatments:", corrosion_prevention_treatments.shape[0])

# Get all routine maintenance
routine_maintenance = maf_data[maf_data.routine_maintenance == "Yes"]
print("Number of routine maintenance actions:", routine_maintenance.shape[0])

# Get all unscheduled maintenance
unscheduled_maintenance = maf_data[maf_data.unscheduled_maintenance == "Yes"]
print("Number of unscheduled maintenance actions:", unscheduled_maintenance.shape[0])

# Get all mission-related maintenance
mission_related_maintenance = maf_data[maf_data.mission_related_maintenance == "Yes"]
print("Number of mission-related maintenance actions:", mission_related_maintenance.shape[0])

# Get all failures
failures = maf_data[maf_data.failure == "Yes"]
print("Number of failures:", failures.shape[0])

# Get all rows where description_of_problem == "Perform a periodic inspection"
periodic_inspections = maf_data[maf_data.description_of_problem == "Perform a periodic inspection"]
print("Number of rows where description of problem is 'Perform a periodic inspection':", periodic_inspections.shape[0])
print()

### MU DATA
mu_data = pd.read_csv("Data/HTM_MSP_Final.csv")
rename_columns_in_snake_case(mu_data)
print("Total number of rows in MU Data:", mu_data.shape[0])
print("Columns in MU Data:", mu_data.columns)
print()

print("Unique values in AIRCRAFT column:", mu_data.aircraft.unique())
print("Unique values in SQUADRON column:", mu_data.squadron.unique())
print("Unique values in LOT column:", mu_data.lot.unique())
print("Unique values in MSP column:", mu_data.msp.unique())
print("Unique values in ZULU_TIME column:", mu_data.zulu_time.unique())
print("Unique values in FLIGHT_MODE column:", mu_data.flight_mode.unique())
