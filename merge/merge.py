#!/usr/bin/python
#
# prereq:
# sudo apt-get install python-pip -y
# sudo pip install jinja2
# mkdir ./configs
#
import sys
import argparse
import json
import os
import jinja2

OUTPUT_DIR = './configs/'
def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './'),
        lstrip_blocks = True,
        trim_blocks = True
    ).get_template(filename).render(context)


# GET jsonConfigName from CLI
# GET templateFileName from CLI

parser = argparse.ArgumentParser(description='Merge json data with jinja2 templates')
parser.add_argument('-t','--template', nargs='?', help="Template file name")
parser.add_argument('-j','--json', nargs='*', help="JSON data file name")
args = parser.parse_args()

if not args.json:
  print('Data not provided')
  sys.exit(2)

if args.template:
  templ = True
  templateFileName = args.template
else:
  templ = None

# With every data file *.json in list args.json
# Create configuration files in ./configs/

for jsonConfig in args.json:
  print("================================================")
  print("+")
  print("+   Config file :" + jsonConfig)
  print("+")
  print("================================================")
  jsonConfigName = jsonConfig
  #templateFileName = args.template
  _, jsonName = os.path.split(jsonConfigName)
  print "jsonConfigName: " + jsonConfigName
  #print "templateFileName: " + templateFileName
  with open(jsonConfigName) as json_file:
      json_data = json.load(json_file)
      #print(json_data)
  if not templ:
    templateFileName = json_data['template'] + '.j2'
  
  nameDiff = json_data['template'].lower()

  #iterate through each json_data['data'] entry
  for entry in json_data['data']:

    # put entire json entry into jinja context for merging
    context = entry

    print("================================================")

    # get template name, output file name
    outputFileName = jsonName[:-4] + str(entry[nameDiff]) + ".conf"
    print("outputFileName: " + outputFileName)

    # merge template with data
    result = render(templateFileName,context)

    # write output to file
    outFile = open(OUTPUT_DIR+outputFileName,"w")
    outFile.write(result)
    outFile.close()

  print("================================================")