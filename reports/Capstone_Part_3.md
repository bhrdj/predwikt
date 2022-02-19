## Capstone Part 3

Steven Bhardwaj - GA DSiFX Australia - 2022-02-19 Saturday

---

#### Data acquisition

I have acquired sufficient jawiki dumps to do the project on static data.  I have also accessed the RSS and EventStream live versions of this data.

#### EDA

I have done multiple stages of initial EDA and am *almost* done with a first-pass version of data cleaning. I have not done a thorough EDA yet, and have not begun modeling yet.

I'm not facing significant blockers, other than a steady learning curve in SQL and the mysql.connector / sqlalchemy libraries. Upcoming challenges include:

- Creating a SQL View Virtual Table (or new permanent table) to do EDA with 9x 2gb ```history``` tables
- EDA while pulling data from SQL tables for each step, using JOINs across ```history```, ```category```, ```categorylinks```, and ```page``` tables.
- Binning time series data for modeling
- Modeling design choices

#### Blockers

Once I begin processing I will certainly begin facing the challenge of processing-time. To avoid this in preliminary analysis, I will bin the data by-day.

#### Topic changes

I haven't changed my topic.

#### 2-week Timeline

For this week I need to do a first pass-through in modeling.  I also am doing a deep dive into DeFi for an interview this Friday (Feb 25).

#### What topics do you want to discuss during your 1:1?

- Collaboratively sketch an overall flowchart for my capstone
  - On https://docs.google.com/drawings ?
  - If the instructor has experience with any PM system like scrum, maybe we can frame it in that?