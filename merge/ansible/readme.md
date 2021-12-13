## Ansible template merging usage

### Playbook

#### Inventory

Add inventory hosts by editing `./inventory/hosts`

#### Tasks

Add/remove playbook tasks that use existing templates

#### Configuration state

Configuration state that is used in merged template variables can be provided
in multiple ways:
* Host variables in files under `./host_vars`
* Group variables in files under `./group_vars`
* Imported variable files (not implemented in this playbook)

Configuration state binding to devices that are defined in inventory can be 
checked with `ansible-inventory` tooling.

#### Running playbook

`ansible-playbook merge-templates.yml`

### Ansible installation

TBD
