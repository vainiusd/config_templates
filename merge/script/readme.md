## Merge script usage

JSON file is a mandatory parameter.
```
./merge.py -j /json/file
```
Output file can be changed.
```
./merge.py -j /json/dir/* -o /output/path/
```
Templates can be provided in a separate dir or 1:1 with template.
```
./merge.py -j /json/dir/* -t /template/dir/
./merge.py -j /json/file -t /template/file
```

### Input parameters
* -j, --json : JSON config file or list of files (-j /path/to/file or
-j /json/config/dir/\*)
* -t, --template: Template file or template directory (optional, default 
is current dir)
* -o, --output-dir : Output directory (optional, default is ./config/)

#### JSON configuration files
JSON configuration files have a list of configuration parameter dictionaries.
Example JSON config files are provided with each template as a comment.

#### Template files
If template file is not provided as a parameter or a dir is provided,
template name is formed by adding '.j2' to 'template' value from JSON 
configuration file.  

### Templates

Jinja2 templates that represent configuration snippets needed to configure 
various networking services in $vendor network equipment. Each template 
[MUST](https://www.ietf.org/rfc/rfc2119.txt) include a JSON configuration 
file example that defines all used parameter values and can be used with 
this merge script.