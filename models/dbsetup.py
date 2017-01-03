from datetime import datetime
from gluon.contrib.appconfig import AppConfig
import os

# myconf = AppConfig(reload=True)


# device_brand
db.define_table('device_brand',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Brand"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)
# device_model
db.define_table('device_model',
	Field('name', 'string',requires=[IS_NOT_EMPTY()], label="Model"),
	Field('brand_id', 'reference device_brand',
		requires=[IS_NOT_EMPTY()], label="Brand"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format = '%(name)s')

db.device_model.brand_id.requires=IS_IN_DB(db(db.device_brand.is_active == True), db.device_brand.id, '%(name)s')


# device_type
db.define_table('device_type',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Device Type"),
	Field('device_code', 'string', requires=[IS_NOT_EMPTY()], label="Prefix Code"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)

# device_type
db.define_table('os_type',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="OS Name"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)

# apps_type
db.define_table('apps_type',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="App Type"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)


# apps
db.define_table('apps',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="App Name"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)


# app_assign
db.define_table('app_assign',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="App Name"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	Field('app_type_id', 'reference apps_type', label="Type"), # , requires=[IS_NOT_EMPTY()]
	format='%(name)s'
)

db.app_assign.app_type_id.requires=IS_IN_DB(db(db.apps_type.is_active == True), db.apps_type.id, '%(name)s')

#app_assign_detail
db.define_table('app_assign_detail',
	Field('app_assign_id', 'reference app_assign', requires=[IS_NOT_EMPTY()], label="Assign ID"),
	Field('apps_id', 'reference apps', requires=[IS_NOT_EMPTY()], label="Application Name")
)

db.app_assign_detail.apps_id.requires=IS_IN_DB(db(db.apps.is_active == True), db.apps.id, '%(name)s')
# email_type
db.define_table('email_type',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Email Type"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)

# license_type
db.define_table('license_type',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="License Type"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)


# department
db.define_table('department',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Department Name"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)


# location
db.define_table('location_plant',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Location/Plant"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)


# sim_brand
db.define_table('sim_brand',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="SIM Brand"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)


# sim_plan
db.define_table('sim_plan',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="SIM Plan"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)

##sim
db.define_table('sim',
	Field('sim_number', 'string', requires=[IS_NOT_EMPTY()],label="Phone Number"),
	Field('brand_type_id', 'reference sim_brand', requires=[
	IS_IN_DB(db(db.sim_brand.is_active == True).select(),
	db.sim_brand.id, '%(name)s'),
	IS_NOT_EMPTY()], label="Operator"),
	Field('plan_type_id', 'reference sim_plan', requires=[
	IS_IN_DB(db(db.sim_plan.is_active == True).select(),
	db.sim_plan.id, '%(name)s'),
	IS_NOT_EMPTY()], label="Plan"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s'
)

## device
db.define_table('device',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Name"),
	Field('device_brand_id', 'reference device_brand', requires=[IS_NOT_EMPTY()], label="Brand"),
	Field('device_model_id', 'reference device_model', requires=[
	IS_IN_DB(db(db.device_model.is_active == True).select(db.device_model.id),
	db.device_model.id, '%(name)s'),
	IS_NOT_EMPTY()], label="Model"),
	Field('device_type_id', 'reference device_type', requires=[
	IS_IN_DB(db(db.device_type.is_active == True).select(db.device_type.id),
	db.device_type.id, '%(name)s'),
	IS_NOT_EMPTY()], label="Type"),
	Field('os_type_id', 'reference os_type', requires=[
	IS_IN_DB(db(db.os_type.is_active == True).select(db.os_type.id),
	db.os_type.id, '%(name)s'),
	IS_NOT_EMPTY()], label="Operation System"),
	Field('cpu', 'string', requires=[IS_NOT_EMPTY()], label="CPU"),
	Field('ram', 'string', requires=[IS_NOT_EMPTY()], label="RAM"),
	Field('hard_disk', 'string', requires=[IS_NOT_EMPTY()], label="HDD"),
	Field('drive', 'string', label="CD/DVD"),
	Field('screen_size', 'string', label="Display"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s')


db.device.name.readonly = True
db.device.device_brand_id.requires = IS_IN_DB(db(db.device_brand.is_active == True),db.device_brand.id, '%(name)s')
db.device.device_model_id.requires = IS_IN_DB(db(db.device_model.is_active == True),db.device_model.id, '%(name)s')
db.device.device_type_id.requires = IS_IN_DB(db(db.device_type.is_active == True),db.device_type.id, '%(name)s')
db.device.os_type_id.requires = IS_IN_DB(db(db.os_type.is_active == True),db.os_type.id, '%(name)s')
d_code = db(db.device_type.is_active == True).select(db.device_type.id, db.device_type.device_code)

## employee
db.define_table('employee',
	Field('code', 'string', requires=[IS_NOT_EMPTY()], label="Code"),
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Name"),
	Field('job_title', 'string', label="Job Title"),
	Field('department_id', 'reference department', requires=[
	IS_IN_DB(db(db.department.is_active == True).select(),
	db.department.id, '%(name)s'),
	IS_NOT_EMPTY()], label="Department"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s')



## email
db.define_table('email_account',
	Field('username', 'string', requires=[IS_NOT_EMPTY()], label="Email Address"),
	Field('default_password', 'string', label="Default Password"),
	Field('email_type_id', 'reference email_type', requires=[IS_IN_DB(db(db.email_type.is_active == True).select(), db.email_type.id, '%(name)s'),
	IS_NOT_EMPTY()], label="User Type"),
	Field('license_type_id', 'reference license_type', requires=[
	IS_IN_DB(db(db.license_type.is_active == True).select(),
	db.license_type.id, '%(name)s'),
	IS_NOT_EMPTY()], label="License Type"),
	Field('is_used', 'boolean', default=True, label="Used"),
	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s')



## Rent Device
db.define_table('rent',
	Field('employee_id', 'reference employee', requires=IS_NOT_EMPTY(), label="Employee"),
	Field('rent_date', 'datetime', requires=IS_NOT_EMPTY(),  default=request.now, label="Rent Date"),
	Field('device_id', 'reference device', requires=IS_NOT_EMPTY(), label="Device"),
	Field('serial_number', 'string', requires=IS_NOT_EMPTY(), label="S/N or Assets Number"),
	Field('rent_desc', 'string', label="Rent Description"),
	Field('is_received', 'boolean', default=False, label="Received"),
	Field('receive_date', 'datetime', label="Receive Date"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),

)
db.rent.rent_date.represent= lambda x, row: x.strftime("%B %d, %Y")
db.rent.receive_date.show_if = (db.rent.is_received == True)
db.rent.employee_id.requires = IS_IN_DB(db(db.employee.is_active == True),
									db.employee.id, '%(name)s', sort=True)
db.rent.device_id.requires = IS_IN_DB(db(db.device.is_active == True),
										  db.device.id, '%(name)s', sort=True)


db.define_table('assign',
    Field('employee_id', 'reference employee', label="Employee", requires=IS_NOT_EMPTY()),
    Field('assign_date', 'datetime', default=request.now, label="Assign Date", requires=IS_NOT_EMPTY()),
	Field('email_id', 'reference email_account', label="E-Mail", requires=IS_NOT_EMPTY()),

	Field('is_active', 'boolean', default=True, label="Active"),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
    format=lambda r: "%s_%s" % (r.assign_date.strftime("%Y%m%d"),
                                   db.employee(r.employee_id).name))


db.assign.employee_id.requires = IS_IN_DB(db(db.employee.is_active == True),
									db.employee.id, '%(name)s')
db.assign.assign_date.requires = IS_NOT_EMPTY()
db.assign.email_id.requires = IS_IN_DB(db(db.email_account.is_used == False and
									db.email_account.is_active == True),
									db.email_account.id, '%(username)s')

db.define_table('assign_device',
    Field('assign_id', 'reference assign', label='Assign ID'),
    Field('device_id', 'reference device', label='Device', requires=IS_NOT_EMPTY()),
    Field('serial', 'string', unique=True, requires=IS_NOT_EMPTY(), label='S/N or Unique Number'),
    Field('asset_number', 'string', label='Assets Number'),
    Field('device_color', 'string', label='Color'),
	Field('is_used', 'boolean', default=True, label="Used"),
	Field('is_damaged', 'boolean', default=False, label="Damaged"),
	Field('is_lost', 'boolean', default=False, label="Lost")
)

db.assign_device.device_id.requires=IS_IN_DB(db(db.device.is_active=='T'), db.device.id, '%(name)s')

used_serial =[id for id in db((db.assign_device.is_used == True) |
	(db.assign_device.is_lost==True) | (db.assign_device.is_damaged==True)).select(db.assign_device.serial)]
db.assign_device.serial.requires=IS_NOT_IN_DB(db(db.assign_device.serial == used_serial), 'assign_device.serial')

db.define_table('assign_app',
	Field('assign_id', 'reference assign', label='Assign ID'),
	Field('app_id', 'string', label='Application Name', requires=IS_NOT_EMPTY()),
)

db.assign_app.app_id.requires = IS_IN_DB(db(db.apps.is_active == True), db.apps.id, '%(name)s')

db.define_table('assign_accessories',
	Field('assign_id', 'reference assign', label='Assign ID'),
	# Field('accessories_id', 'reference general_table', label='Accessory', requires=IS_NOT_EMPTY()),
	Field('serial', 'string', requires=IS_NOT_EMPTY(), label='S/N or Unique Number'),
    Field('asset_number', 'string', label='Assets Number'),
	Field('is_used', 'boolean', default=True, label="Used"),
	Field('is_damaged', 'boolean', default=False, label="Damaged"),
	Field('is_lost', 'boolean', default=False, label="Lost")
)

# acs_id = ''
# for id in db(db.config_group.name==myconf.get('default_type.acs')).select(db.config_group.id):
#      acs_id = id
# db.assign_accessories.accessories_id.requires=IS_IN_DB(db(db.general_table.config_type == acs_id), db.general_table.id, '%(name)s', sort=True)


db.define_table('assign_sim',
	Field('assign_id', 'reference assign', label='Assign ID'),
	# Field('sim_id', 'reference general_table', label='SIM', requires=IS_NOT_EMPTY()),
	Field('is_used', 'boolean', default=True, label="Used"),
	Field('is_locked', 'boolean', default=False, label="Locked"),
	Field('is_lost', 'boolean', default=False, label="Lost")
)

# db.assign_sim.sim_id.requires=IS_IN_DB(db(db.sim.is_active==True), db.sim.id, '%(name)s')
# used_sim =[id for id in db((db.assign_sim.is_used == True) | (db.assign_sim.is_locked == True) | (db.assign_sim.is_lost == True)).select(db.assign_sim.sim_id)]
# db.assign_device.device_id.requires=IS_NOT_IN_DB(db(db.assign_sim.sim_id == used_sim), 'assign_sim.sim_id')

## default user root
if db(db.auth_user).count() <1:
	db.auth_group.bulk_insert([
		dict(role='Admin', description='System user'),
		dict(role='Manager', description='Manager'),
		dict(role='User', description='User')
	])

	db.auth_user.bulk_insert([
		dict(
			first_name='System',
			last_name='Admin',
			email='root@coca-cola.com.mm',
			password=db.auth_user.password.validate('C0ke@12345')[0]
		),
		dict(
			first_name='Nyein',
			last_name='Chan',
			email='nyeinchan@coca-cola.com.mm',
			password=db.auth_user.password.validate('Basn4@C01')[0]
		)
	])

	auth.add_membership(user_id=1, group_id=1)
	auth.add_membership(user_id=2, group_id=1)

# if db(db.config_group).count() < 1:
# 	db.config_group.bulk_insert([
# 		dict(name=myconf.get('default_type.acs')),
# 		dict(name=myconf.get('default_type.app')),
# 		dict(name=myconf.get('default_type.dpt')),
# 		dict(name=myconf.get('default_type.dvc')),
# 		dict(name=myconf.get('default_type.eml')),
# 		dict(name=myconf.get('default_type.loc')),
# 		dict(name=myconf.get('default_type.lnc')),
# 		dict(name=myconf.get('default_type.opt')),
# 		dict(name=myconf.get('default_type.pln')),
# 		dict(name=myconf.get('default_type.usr'))
# 	])

# Insert into outlet(name, is_active) values
# ('Computer Shop', 1)
# ,('Café', 1)
# ,('Café Pub', 1)
# ,('Clinic with Pharmacy', 1)
# ,('Cold Drink', 1)
# ,('Computer Shop', 1)
# ,('Convenience Store _ Cigarette Specialized', 1)
# ,('Convenience Store _ Liquor Specialized', 1)
# ,('Convenience Store _ Miscellaneous/ Sundry', 1)
# ,('Convenience Store _ Modern Trade', 1)
# ,('Convenience Store _ Petro Station', 1)
# ,('Convenience Store _ Specialized', 1)
# ,('Convenience Store _ Traditional', 1)
# ,('Department Store', 1)
# ,('Diner Outlet', 1)
# ,('Family Stall', 1)
# ,('Food Stall/Traditional Food', 1)
# ,('Game Center', 1)
# ,('General Store', 1)
# ,('Grocery Store', 1)
# ,('Guest House/Inn/Motel', 1)
# ,('Home Appliance', 1)
# ,('Hotel (International Standard)', 1)
# ,('Hotel (Local Standard)', 1)
# ,('Internet Cafe', 1)
# ,('Kiosks/Hawker', 1)
# ,('KTV', 1)
# ,('Mini Mart', 1)
# ,('Mobile Shop', 1)
# ,('Night Club', 1)
# ,('Pharmacy Store', 1)
# ,('Restaurant with indoor/outdoor Sports', 1)
# ,('Restaurant with Live Entertainment', 1)
# ,('Semi Whole Sale', 1)
# ,('Super Market/Hyper Market', 1)
# ,('Tea Shop', 1)
# ,('Whole Sale', 1)
# ,('Others', 1);
#
# Insert into question (name, is_active) values
# ('Cooler Coke', 1)
# ,('Cooler Pepsi', 1)
# ,('Cooler Blue Mountain', 1)
# ,('Cooler Asia', 1)
# ,('Cooler Own', 1)
# ,('Refrigerator Own', 1)
# ,('Freezer Own', 1)
# ,('Self Service/Outlet Service', 1)
# ,('Coke RGB', 1)
# ,('Pepsi RGB', 1)
# ,('CSD (Non-Alcohol)', 1)
# ,('Soda (Non-Alcohol)', 1)
# ,('FF Drink (Non-Alcohol)', 1)
# ,('FF Powder (Non-Alcohol)', 1)
# ,('ASD (Non-Alcohol)', 1)
# ,('Isotonic Drink (Non-Alcohol)', 1)
# ,('Energy Drink (Non-Alcohol)', 1)
# ,('Carbonated Energy Drink (Non-Alcohol)', 1)
# ,('Drinking Water (Non-Alcohol)', 1)
# ,('Instant Coffee (Non-Alcohol)', 1)
# ,('Tea Mix (Non-Alcohol)', 1)
# ,('Coffee Canned (Non-Alcohol)', 1)
# ,('Import Snack (Foods)', 1)
# ,('Confectionary (Foods)', 1)
# ,('Ice Cream/Lollies (Foods)', 1);
#
