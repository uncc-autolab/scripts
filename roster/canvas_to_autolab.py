#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:07:06 2018

@author: archit
"""

import pandas as pd
import argparse 


def main(args):
   columns = ['Semester','email','last_name','first_name','school','major','year','grading_policy','courseNumber','courseLecture','section']

   canvas = pd.read_csv(args['canvas_roster_file'],usecols=['Student', 'ID', 'SIS Login ID', 'Section'])
   canvas.drop(index=0, inplace=True)

   autolab = pd.DataFrame(columns=columns)
   Semester = args['semester']
   school = 'UNCC'

   for index, row in canvas.iterrows():
      email = row['SIS Login ID'] + '@uncc.edu'
      student = row['Student']
    
      last_name, first_name = student.split(',')
      first_name = first_name.strip()
      
      if first_name == 'Test':
          continue
         
      course = row['Section']
      course = course.split('-')
      dept, courseLecture, section = course
      
      autolab = autolab.append({'Semester': Semester, 'email' : email, 'last_name' : last_name,
                     'first_name' : first_name, 'school' : school,
                     'courseLecture' : courseLecture, 'section' : section}, ignore_index=True)
      

   output_file = 'autolab_roster_{}_{}_{}_{}_{}.csv'.format(school, args['semester'], dept, courseLecture, section)
   autolab.to_csv(output_file, index=False,header=False)
   print('Exported: ', output_file)
   
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert canvas roster to autolab')
    parser.add_argument('--canvas_roster_file', type=str, help='Canvas roster filepath')
    parser.add_argument('--semester', type=str, help='Current semester eg: Fall-2020')
    args = vars(parser.parse_args())
    main(args)

   
