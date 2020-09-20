# Exporting student accounts from Canvas to Autolab

1. Download the roster for your course from canvas:

   ```
   Canvas > Course > Grades > Actions > Export
   ```

2. Execute the script as:

   ```bash
   python canvas_to_autolab.py --canvas_roster_file=example_canvas_roster.csv --semester='Fall-2020'
   ```

3. Use the generated roster in Autolab to create student accounts:

   ```
   Autolab > Course > Manage Course > Manage Students > Import Roster/Users > Browse > Select the generated file
   ```

   

