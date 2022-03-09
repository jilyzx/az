import io
import json
import time
import random
from contextlib import redirect_stdout
from azure.cli.core import get_default_cli
from random import choice,randint

#username = 'w38ojudp@arthurshillprimaryschools.co.uk'
#password = '14dV54iTtC'
group_name = 'az'
locations = ['eastus', 'eastus2', 'westus', 'centralus', 'northcentralus', 'southcentralus', 'northeurope', 'westeurope', 
			'eastasia', 'southeastasia', 'japaneast', 'japanwest', 'australiaeast', 'australiasoutheast', 'australiacentral', 'brazilsouth',
            'southindia', 'centralindia', 'westindia', 'canadacentral', 'canadaeast', 'westus2', 'westcentralus', 
            'uksouth', 'ukwest', 'koreacentral', 'francecentral', 'southafricanorth', 'uaenorth', 'switzerlandnorth', 
            'germanywestcentral', 'norwayeast', 'westus3']


def get_verification_code(length=int()) -> str:
    str_tmp = ''
    for index in range(length):
        str_tmp += choice([get_random_alpha(), str(randint(0, 9))])
    return str_tmp


def get_random_alpha(ab_a=int(65), ab_b=int(90)) -> str:
    # chr() upper 65,90 lower 97,122
    str_tmp = chr(randint(ab_a, ab_b))
    return choice([str_tmp, str_tmp.lower()])

origin_name = 'batch'
batch_defaul_name = origin_name+get_verification_code(length=6)

#登录信息#


#资源组信息#
vm_list_date = [

'vm',
'list',
'-g',
f'{group_name}'
]

group_create_date = ['group','create','-n',f'{group_name}','-l','eastus2',
    '--query',
	'{"创建资源组":properties.provisioningState}']


def get_cli(date):
	  get_default_cli().invoke(date)



def batch_create_command(a,b):
	create_command = [
		'deployment', 'group','create', '--resource-group', f'{group_name}', '--template-file','/home/fern/1.json',
		'--parameters',f'location={a}','--parameters',f'batchAccounts_batches_name={b}','--query','[].providers.provisioningState',
	]

	return create_command

#登录，仅限子号#
#get_cli(login_date)

#创建资源#
get_cli(group_create_date)

#batch数量#
count = 0

#开始循环创建batch#
while count < 34 :
	#定义初始值#
	mylocation = locations[count]
	#print(mylocation)
	batch_name = batch_defaul_name + str(count)
	print(batch_name)
	#创建batch#
	get_cli(batch_create_command(mylocation,batch_name))
	count+=1
else:
	print("已完成一共" + str(count) + "个地区")

#get_cli(logout)
