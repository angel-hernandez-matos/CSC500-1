# File: mainDiscussionForum.py
# Written by: Angel Hernandez
# Description: Code snippet for discussion forum - Module 3
# Requirement(s):
#
#Identify three real-life scenarios in which an array could be used for storing information.
# Provide a sample code segment that illustrates how to store data in an array for one of your outlined scenarios.
# Provide a rationale for your response. In response to your peers, provide constructive feedback on strategies and
# rationales that were posted. Include additional code segments if applicable.

import os
import requests
import uuid
import inflect

class ChartUserPreferences:
    labels = []
    datasets = []

    @property
    def is_valid(self):
        return len(self.labels) == len(self.datasets) > 0 and len(self.labels) > 0

    def user_input(self):
       print("*** Chart User Preferences ***")
       user_entry = [("Label(s)", self.labels), ("Dataset(s)", self.datasets)]
       for category, target_array in user_entry:
           self.__input_preference(category, target_array)

    @staticmethod
    def __input_preference(category, target_array):
        count = 0
        number_to = inflect.engine()
        print()
        while True:
            count = count + 1
            preference = input(f"Enter {number_to.ordinal(count)} {category.replace('(s)', '')} value: ")
            if not preference.strip():
                break
            else:
                target_array.append(preference)

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def flatten_array(array, attribute, treat_as_char):
    retval = ""

    if array:
       retval = attribute + ":["
       delimiter = "'" if treat_as_char else ""
       for item in array:
           retval = retval + delimiter + item + delimiter +","
       retval = retval[:-1] + "]"

    return retval

def main():
    clear_screen()
    print('*** Module 3 - Discussion Forum ***\n')

    try:
      chart_user_preferences = ChartUserPreferences()
      chart_user_preferences.user_input()

      if chart_user_preferences.is_valid:
          labels = flatten_array(chart_user_preferences.labels, "labels", True)
          datasets = flatten_array(chart_user_preferences.datasets, "data", False)
          newfile = str(uuid.uuid4()) + ".png"
          chart_url = "https://quickchart.io/chart?c=" + "{type:'bar',data:{" + labels +",datasets:[{" + datasets + "}]}}".replace("'","%27")
          response = requests.get(chart_url)

          if response.status_code == 200:
              with open(newfile, "wb") as file:
                  file.write(response.content)
          else:
              print("Error:", response.status_code)
      else:
          print("Chart user preferences is not valid")
    except Exception as e:
        print(e)

if __name__ ==  '__main__': main()