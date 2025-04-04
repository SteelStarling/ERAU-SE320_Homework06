# Coronal Mass Ejection Web Viewer

A tool designed to use NASA's DONKI API to display information on Coronal Mass Ejections

Shows information on the most recent CME and has a page showing raw data on the CMEs of the past 30 days.

Currently very bare bones, but I might end up adding more features later, since this is quite fun to mess with (and good practice with web dev)

### How to Run Yourself:

Add your own API key to a .env file in the root directory, in the format: `API_KEY="your api key"`, or as shown in the .env.example file

Ensure all requirements are installed

Run via the command `streamlit run app/coronal_mass_ejections.py`

### Future Development Plans

Have an EPIC image viewer (shows pictures of Earth from one of the same systems used to track CMEs)

Charts showing CME frequency over time

Better information for each CME