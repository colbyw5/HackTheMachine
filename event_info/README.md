# TRACK 2: Data Science: Cleared for Takeoff
Naval aircraft are complex systems that transmit, receive, and collect gigabytes of data
during every mission. Normally when a system fails, it warns the aircrew with flashing
lights and audible alarms or at least registers a fault code in the onboard computer
system. However, sometimes pilots experience unpredictable behavior without clear
warnings, or the fault codes don’t align to what the pilot experienced. Even more
frustrating is when the problems are intermittent. Maintainers can spend hours pulling
apart the assemblies and running through the troubleshooting procedures to try and
determine the root cause, but they can’t replicate the fault or find an issue. The issue is
reported as Malfunction Code “799” or “No Fault Found” in the maintenance log.
Often, a problem does indeed exist. Issues with corrosion or wiring can cause fault
codes that are seemingly unrelated to the problems the aircraft is experiencing.
Fortunately, sometimes the story is in the data. Patterns in the aircraft fault codes and
maintenance logs can reveal when wires within the aircraft began to chafe or corrosion
causes systems on the aircraft to intermittently report errors before they can be
detected by the pilot or the maintainer. Finding these unique patterns in the data could
reveal the damage before an incident occurs and save dollars and potentially lives.

## Data Intro:
For this challenge we are providing you with two unique datasets that have never
before been publicly available. The first dataset is the Maintenance Action Form (MAF)
data, which contains a record of maintenance actions performed on the aircraft. It is a
record of everything maintainers have done to the aircraft including: routine
inspections, part removal and replacement, mission-related changes, and unscheduled
maintenance, including unforeseen failures. The second dataset is the Memory Unit
(MU) data. The MU data is a time-stamped record of all failures or anomalies
automatically reported by the aircraft’s avionics system, similar to an error log your
auto mechanic might download from your car when the check engine light comes on.

## Challenge Intro:
The challenge is to identify patterns and correlations in the MU data and determine
how those relate to the maintenance actions. For example, a maintainer accidently
switches two wires during a routine inspection. From that point on, three seemingly
unrelated fault codes appear with extremely high correlation. The wiring mismatch is
fixed two months later, but one intermittent fault code remains. Upon further
inspection, it is determined that this fault code is caused by chafing in a wiring harness.
Once the harness is repaired the fault code ceases. We need your help discovering
patterns of aircraft generated fault codes that are indicative “signature” conditions
related to corrosion and wiring issues. The early identification of these problems will
help reduce the downtime and number of mishaps experienced by F-18s.

# The Challenge
You have ~7 years of data from 45 F-18s. The dataset contains 13 aircraft that were subject
to a special set of inspections to fix wiring issues. The wiring issues were corrected at some
point in the past. The remaining aircraft have never before been analyzed. Your task is to
develop analytic techniques to identify patterns of interest in the MSP codes (MU data) and
relate them to the maintenance actions (MAF data). Relevant analytical techniques may
include timeseries, correlation analysis, and clustering algorithms. In particular, we are
interested in corrosion-related problems and have tagged the data with a flag for
corrosion-related maintenance actions.

## Challenge 1: 
Up to 40 Points will be awarded for your ability to identify the MSP code
patterns in the 13 aircraft with known wiring issues. For this challenge, your objective is to
identify which 13 of the 45 aircraft had the wiring inspections and subsequent repairs and
to provide a list of the maintenance actions that you believe fixed the wiring issues. You
may provide up to 200 maintenance actions as part of your solution. Additionally, you can
provide up to 10 MSP codes for each maintenance action that you believe are associated
with the wiring fixes.

Hint #1: Intermittent MSP codes related to the issue likey stopped after the repair.
Hint #2: Some aircraft have clusters of wiring related MAFs and the same MSP codes can be
correctly attributed to more than one MAF.
Hint #3: Some aircraft had more than one wiring inspection.

There is a challenge 1 submission spreadsheet template that will be provided. In order to
receive points, the algorithms and methodology behind your solution must be provided
and the evaluation criteria will include accuracy of your solution as well as generalizability
to other non-wiring issues.

## Challenge 2: 
Up to 50 Points will be awarded for algorithms, techniques, and visualizations
that most effectively identify demonstrate patterns in the relationship between MSP codes
and maintenance actions, particularly those related to corrosion. Variables of interest
include: Aircraft, MSP Code(s) (with start and stop dates), correlation with maintenance
actions or with other MSP codes, frequency, duration, and flight mode. These patterns
could be within aircraft or across aircraft and might correspond to aircraft sub-type,
squadron, or other variables.

For individual aircraft, the Navy has anecdotal examples of a corrosion-related
maintenance actions resulting in intermittent MSP codes stopping. Across aircraft, the
Navy has discovered that sometimes when an aircraft is moved between certain squadrons
the transfer inspection results in intermittent MSP codes stopping. If you are able to
uncover a systematic way to discover these features in the data, it may change the way
maintenance is performed.

Your solution should include a visualization component, as the ability to display data is a
critical component in recognizing patterns of fault codes. Points will be given for MSP code
patterns and the corresponding MAFs that the Navy should investigate, as well as the
development of a data visualization tool that clearly communicates the fault code patterns
to the aviation enterprise. Points will be awarded for informative approaches to pattern
recognition as evaluated by subject matter experts. The criteria will include technical
strength of the methodology, generalizability, creativity/uniqueness of the approach, and
the degree to which the visualizations provide insight and support your conclusions.

## Containerization: 
Up to 10 Points will be given to teams that containerize their algorithms
to run within on the cloud-based Agile Core Services (ACS) environment (see Environment
and Tools section). These algorithms may be run on the ACS system after the hackathon.
We will have staff on hand to assist if you’ve never done this before.
Environment Review: Up to 5 Bonus Points will be awarded for the feedback on the ACS
environment. Specifically, we will be looking for feedback on usability and tools. Regarding
tools, we would like your thoughts on the current tool suite as well as tools that should be
included to support data science. A feedback template will be provided as part of the
participant materials.

[For more information on the challenge check out the participant guide here.](https://static1.squarespace.com/static/596d24cd4402430bb863ffad/t/5d670d7ca9c073000161a06c/1567034750634/HACKtheMACHINE_New+York_Data+Science+Participant+Guide.pdf)

# Welcome:
Welcome to HACKtheMACHINE New York. We are really excited you are here. This GitLab Repo will be here for your convenience throughout the challenge. It contains information for you to get started on the challenge as well as advice on how to approach the challenge. If anything comes up during the hackathon, we will try to update this page. In addition to this repo, you should have access to your personal team repository. There is more information on how to use that repository over there. 

If you’ve never been to a hackathon, you might not know what to expect this weekend. Generally, you can break this hackathon into 7 stages:
1.	Team Formation
2.	Environment Access
3.	Get Started
4.	Hack Away
5.	Submit Your Project
6.	Tell us About it
7.	Winners Announced

We’ve outlined what each of these stages will entail below. Let us know if you have any questions!

To stay in the loop during the hackathon be sure you join our slack workspace at: https://bit.ly/2k33zcL

# Team Formation:
There will be a maximum of 20 teams allowed in the data science challenge. To ensure that every individual that signed up gets to be on a team we will prioritize environment access to teams of 5+. If you have a smaller team, we may have to add members to your team. If there is an exceptional turn out, we may be forced to also add participants to teams of 5+. Members will be added to smaller teams first. 

You can begin official team formation on Friday night during the Hackathon kick off event. Once you finalize your team, fill out the [team registration form here](https://docs.google.com/forms/d/e/1FAIpQLSdALoXDwOm9cpoN6RDgmiQblaxU4ifICxyJDdzQV-eKwKABmw/viewform?usp=sf_link). Alternatively, you can finish forming your team on Saturday morning. All teams will be formally finalized Saturday morning.

# Accessing Environment:
For this hackathon we are using a replica of a Navy environment called Agile Core Services. You will need to go through a series of steps which are detailed below to access this environment. 
![Architecture Diagram](./HtmContestantDiagram_copy.png "Architecture Diagram")

## Team Repo
 To access this environment each person on your team needs to first go to https://gitlab.htm.boozallencsn.com and create an account. If you are reading this you have likely already done this. Once each team member has created an account, [fill out the team registration form](https://docs.google.com/forms/d/e/1FAIpQLSdALoXDwOm9cpoN6RDgmiQblaxU4ifICxyJDdzQV-eKwKABmw/viewform?usp=sf_link). Once you do this our environment team will give you access to a private Team repo with team specific information. Please confirm that each of your team members can access this environment and let our environment team know when you have successfully accessed your team repo. Note that that you will find credentials and team level information within this repository. This information should not be shared with other teams.

## Sagemaker
Once you have access to your team repository you should have access to a personlized Sagemaker Notebook at https://sagemaker.htm.boozallencsn.com/

## Tableau
Finally, to visualize your information we have made Tableau available to all teams. You will find credentials in your team repository. Check in with the Tableau team if you want help getting up and running. You can download [Tableau Desktop here.](https://www.tableau.com/products/desktop/download)

# Get Started:
Most of your work during this hackathon will be self-directed, but we wanted to make it as seamless as possible to get started on the challenge. We’ve included quick start information, such as how to access the entirety of the data, in the Getting started Jupyter notebook within this repository. Check it out 
[here](./GETTING_STARTED_Track2.ipynb). If you have any questions, reach out to one of the data science mentors.

# Hack Away:
We’ll give you the freedom to hack away in whatever manner works for you and your team. There will be updates during the hackathon around expert availability so you know when your questions can get answered. Additionally, there may be some VIP visits where you will have a chance to share your work with Navy personnel and industry professionals. We’ll keep you all posted via the slack channel if there are any updates!

# Submission Requirements:
All work must be submitted by 1:30PM EST Sunday, September 8th. Specifically, requirements are as follows: 
- All work pushed to Gitlab, including:
    - A readme file that:
    	- Provides contact info for all team members
    	- Describes their general approach to the problem
    	- Walks through code. At a minimum, we need to know what script does what, but the more detail, the better
    	- Summarizes their findings
	- Code must include:
		- Code used to generate solutions to challenge 1
		- Code used to generate solutions to challenge 2
		- Code used to the build the image for containerization (docker file and any config or other files that would be required for us to build the image)
	- Docker images created by the team. 
	- Documents, including:
		- Spreadsheets of results
			- Wiring issues csv (template provided)
			- Challenge 2 csv
		- Powerpoint of final presentations 
- Tableau dashboards pushed to Tableau server
- Wiring issues csv submitted to Google Drive
    - Upload your submissions [here](https://drive.google.com/drive/folders/1siQQeZn1L9jleWsxZltDVXZ2QkDBMkIX)
	- Note: THIS MUST BE UPLOADED BY 12:30PM SUNDAY, SEPTEMBER 8th 
- [Feedback form on the ACS environment](https://bit.ly/2lHgCkw): https://bit.ly/2lHgCkw



# Tell us about your experience:
We want to make this hackathon better for future participants, please give us feedback on your experience. Any info you have to share Is very much appreciated! [You can fill out a feedback form here. ](https://forms.gle/e9gSDPPNcoZn2iHt5)

# Winners:
We want to make sure that each project gets judged fairly and thoroughly. We will be sending out an email after the challenge with an announcement on who won the track. We plan to have a few special announcements immediately following the hackathon.


