import jinja2
import os
import sys
import yaml

# 変数ファイル読み込みメソッド
def load_var_file():
    with open(base_dir + '/input_values/template.yml', mode='r') as template_var_file:
        template_var = yaml.safe_load(template_var_file)
    return template_var

def create_nfs_var_file():
    container_list = var_list.get(location + '_container_list')
    
