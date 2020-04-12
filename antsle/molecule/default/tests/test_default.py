import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_tmp_dir_exists(host):
    gen_dir = host.file(os.environ['MOLECULE_SCENARIO_DIRECTORY'] + "/.antsle/")
    assert gen_dir.exists

def test_terraform_dir_exists(host):
    gen_dir = host.file(os.environ['MOLECULE_SCENARIO_DIRECTORY'] + "/.antsle/terraform")
    assert gen_dir.exists

# def test_terraform_files_exists(host):
#     main_tf = host.file(os.environ['MOLECULE_SCENARIO_DIRECTORY'] + "/.antsle/terraform/main.tf")
#     vars_tf = host.file(os.environ['MOLECULE_SCENARIO_DIRECTORY'] + "/.antsle/terraform/variables.tf")
#     assert main_tf.exists
#     assert vars_tf.exists

# def test_terraform_files_exists(host):
#     tf = host.terraform()
#     assert tf.state == "present"
