#!/usr/bin/python
#
# prereq:
# sudo apt-get install python-pip -y
# sudo pip install jinja2
#
import sys
import argparse
import json
import os
import jinja2

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './'),
        lstrip_blocks = True,
        trim_blocks = True
    ).get_template(filename).render(context)


# GET json_config_name from CLI
# GET tamplate_file_name from CLI

parser = argparse.ArgumentParser(description='Merge json data with jinja2 templates')
parser.add_argument('-j','--json', nargs='*', help="JSON data file name(s)")
parser.add_argument('-t','--template', nargs='?', help="Template file name/directory")
parser.add_argument('-o','--output-dir', nargs='?', help='File output directory')
args = parser.parse_args()

if not args.json:
  print('Data not provided')
  sys.exit(2)

# If template is provided, set template
# If template is dir or not provided,
# search for template in .json config file and template dir
# If not provided, template dir is current dir
template_dir = ''
if args.template:
  if os.path.isdir(args.template):
    template_dir = args.template
    templ = False
  elif os.path.isfile(args.template):
    tamplate_file_name = args.template
    templ = True
else:
  templ = False

DEFAULT_OUTPUT_DIR = './configs/'
if args.output_dir:
  output_dir = args.output_dir
else:
  output_dir = DEFAULT_OUTPUT_DIR

if not os.path.exists(output_dir):
  os.makedirs(output_dir)


# With every data file *.json in list args.json
# Create configuration files in output_dir

for json_config in args.json:
  json_config_name = json_config
  _, json_name = os.path.split(json_config_name)
  with open(json_config_name) as json_file:
      json_data = json.load(json_file)
  if not templ:
    tamplate_file_name = template_dir + json_data['template'] + '.j2'
  
  print("======================================================================")
  print("+")
  print("+ Configuration data file: " + json_config)
  print("+ Template               : " + tamplate_file_name)
  print("+")

  name_diff = json_data['template'].lower()
  #iterate through each json_data['data'] entry
  for entry in json_data['data']:
    # put entire json entry into jinja context for merging
    context = entry
    # get template name, output file name
    # json config file must have a data parameter of the same name
    # as the template value (in lowerase)
    # template - AAA.j2, data must have "aaa": "xxx"
    # str(entry[name_diff]) = "xxx"
    out_filename = json_name[:-4] + str(entry[name_diff]) + ".conf"
    print("+")
    print("+ Configuration entry    : " + str(entry[name_diff]))
    # merge template with data
    try:
      result = render(tamplate_file_name,context)
      # write output to file
      outFile = open(output_dir + out_filename,"w")
      outFile.write(result)
      outFile.close()
      print("+ Merged output file     : " + out_filename)
    except jinja2.exceptions.TemplateNotFound as e:
      print("+ TEMPLATE NOT FOUND     : " + str(e))

  print("+")
  print("======================================================================")