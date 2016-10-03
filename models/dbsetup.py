from datetime import datetime
from gluon.contrib.appconfig import AppConfig
myconf = AppConfig(reload=True)


## brand
db.define_table('brand',
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
## model
db.define_table('model',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Model"),
	Field('brand', 'reference brand', requires=[ IS_IN_DB(db, db.brand.id, '%(name)s'), IS_NOT_EMPTY() ], label="Brand"),
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

db.model.brand.requires=IS_IN_DB(db, db.brand.id, '%(name)s')


## config group
db.define_table('config_group',
	Field('name', 'string', requires=[IS_NOT_EMPTY()]),
	Field('is_active', 'boolean', default=True),
	format='%(name)s'
)

## config
db.define_table('general_table',
	Field('code', 'string', requires=[IS_NOT_EMPTY()], label="Code"),
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Name"),
	Field('config_type', 'reference config_group', requires=[IS_IN_DB(db, db.config_group.id, '%(name)s'), IS_NOT_EMPTY()], label="Type"),
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
db.general_table.config_type.requires=IS_IN_DB(db, db.config_group.id, '%(name)s')

## Room
db.define_table('room',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Room"),
	Field('config', 'reference general_table', requires=[
	IS_IN_DB(db(db.general_table.config_type ==db(db.config_group.name==myconf.get('default_type.loc')).select(db.config_group.id)),
	db.general_table.id, '%(name)s'),
	IS_NOT_EMPTY() ], label="Location"),
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

location_id = ''

for id in db(db.config_group.name==myconf.get('default_type.loc')).select(db.config_group.id):
    location_id = id
l_code = db(db.general_table.config_type == location_id).select(db.general_table.id, db.general_table.code)
db.room.config.requires=IS_IN_DB(db(db.general_table.config_type == location_id), db.general_table.id, '%(name)s', sort=True)


## apps
db.define_table('apps',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Name"),
	Field('app_type', 'reference general_table', requires=[
	IS_IN_DB(db(db.general_table.config_type == db(db.config_group.name==myconf.get('default_type.app')).select(db.config_group.id)),
	db.general_table.id, '%(name)s'),
	IS_NOT_EMPTY()], label="Type"),
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

application_id=''
for id in db(db.config_group.name==myconf.get('default_type.app')).select(db.config_group.id):
    application_id = id
db.apps.app_type.requires=IS_IN_DB(db(db.general_table.config_type == application_id), db.general_table.id, '%(name)s', sort=True)

## employee
db.define_table('employee',
	Field('code', 'string', requires=[IS_NOT_EMPTY()], label="Code"),
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Name"),
	Field('job_title', 'string', label="Job Title"),
	Field('department', 'reference general_table', requires=[
	IS_IN_DB(db(db.general_table.config_type == db(db.config_group.name==myconf.get('default_type.dpt')).select(db.config_group.id)),
	db.general_table.id, '%(name)s'),
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

department_id = ''
for id in db(db.config_group.name==myconf.get('default_type.dpt')).select(db.config_group.id):
    department_id = id
db.employee.department.requires=IS_IN_DB(db(db.general_table.config_type == department_id), db.general_table.id, '%(name)s', sort=True)

##sim
db.define_table('sim',
	Field('sim_number', 'string', requires=[IS_NOT_EMPTY()],label="Phone Number"),
	Field('brand_type', 'reference general_table', requires=[
	IS_IN_DB(db(db.general_table.config_type == db(db.config_group.name==myconf.get('default_type.opt')).select(db.config_group.id)),
	db.general_table.id, '%(name)s'),
	IS_NOT_EMPTY()], label="Operator"),
	Field('empty_col', 'string', requires=[IS_NOT_EMPTY()], label="Empty", default=None, readable=True, writable=False),
	Field('plan_type', 'reference general_table', requires=[
	IS_IN_DB(db(db.general_table.config_type == db(db.config_group.name==myconf.get('default_type.pln')).select(db.config_group.id)),
	db.general_table.id, '%(name)s'),
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
operator_id = ''
plan_id = ''
for id in db(db.config_group.name==myconf.get('default_type.opt')).select(db.config_group.id):
	operator_id = id
db.sim.brand_type.requires=IS_IN_DB(db(db.general_table.config_type == operator_id), db.general_table.id, '%(name)s', sort=True)
for id in db(db.config_group.name==myconf.get('default_type.pln')).select(db.config_group.id):
	operator_id = id
db.sim.plan_type.requires=IS_IN_DB(db(db.general_table.config_type == plan_id), db.general_table.id, '%(name)s', sort=True)

## email
db.define_table('email_account',
	Field('username', 'string', requires=[IS_NOT_EMPTY()], label="Email Address"),
	Field('default_password', 'string', label="Default Password"),
	Field('user_type', 'reference general_table', requires=[
	IS_IN_DB(db(db.general_table.config_type == db(db.config_group.name==myconf.get('default_type.user')).select(db.config_group.id)),
	db.general_table.id, '%(name)s'),
	IS_NOT_EMPTY()], label="User Type"),
	Field('empty_col', 'string', requires=[IS_NOT_EMPTY()], default=None, label="Empty", readable=True, writable=False),
	Field('license_type', 'reference general_table', requires=[
	IS_IN_DB(db(db.general_table.config_type == db(db.config_group.name==myconf.get('default_type.lns')).select(db.config_group.id)),
	db.general_table.id, '%(name)s'),
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

user_id = ''
license_id = ''
for id in db(db.config_group.name==myconf.get('default_type.usr')).select(db.config_group.id):
    user_id = id
db.email_account.user_type.requires=IS_IN_DB(db(db.general_table.config_type == user_id), db.general_table.id, '%(name)s', sort=True)
for id in db(db.config_group.name==myconf.get('default_type.lns')).select(db.config_group.id):
    license_id = id
db.email_account.license_type.requires=IS_IN_DB(db(db.general_table.config_type == license_id), db.general_table.id, '%(name)s', sort=True)

## email
db.define_table('device',
	Field('name', 'string', requires=[IS_NOT_EMPTY()], label="Name"),
	Field('device_type', 'reference general_table', requires=[
	IS_IN_DB(db(db.general_table.config_type == db(db.config_group.name==myconf.get('default_type.dvc')).select(db.config_group.id)),
	db.general_table.id, '%(name)s'),
	IS_NOT_EMPTY()], label="Type"),
	Field('model_id', 'reference model', requires=[ IS_IN_DB(db, db.model.id, '%(name)s'), IS_NOT_EMPTY() ], label="Model"),
	Field('os_type', 'reference general_table', requires=[
	IS_IN_DB(db(db.general_table.config_type == db(db.config_group.name==myconf.get('default_type.oss')).select(db.config_group.id)),
	db.general_table.id, '%(name)s'),
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


device_id = ''
os_id = ''
db.device.model_id.requires=IS_IN_DB(db, db.model.id, '%(name)s')
for id in db(db.config_group.name==myconf.get('default_type.dvc')).select(db.config_group.id):
    device_id = id
db.device.device_type.requires=IS_IN_DB(db(db.general_table.config_type == device_id), db.general_table.id, '%(name)s', sort=True)
d_code = db(db.general_table.config_type == device_id).select(db.general_table.id, db.general_table.code)
for id in db(db.config_group.name==myconf.get('default_type.oss')).select(db.config_group.id):
    os_id = id
db.device.os_type.requires=IS_IN_DB(db(db.general_table.config_type == os_id), db.general_table.id, '%(name)s', sort=True)
db.device.name.readonly = True


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
    Field('employee_id', 'reference employee', label="Employee"),
    Field('assign_date', 'datetime', default=request.now, label="Assign Date"),
	Field('email_id', 'reference email_account', label="E-Mail"),
	Field('room_id', 'reference room', label="Room"),
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


db.assign.employee_id.requires = [IS_IN_DB(db(db.employee.is_active == True),
									db.employee.id, '%(name)s'),
								  IS_NOT_EMPTY()]
db.assign.assign_date.requires = [IS_NOT_EMPTY()]
db.assign.email_id.requires = [IS_IN_DB(db(db.email_account.is_used == False and
									db.email_account.is_active == True),
									db.email_account.id, '%(username)s'),
							   IS_NOT_EMPTY()]
db.assign.room_id.requires = [IS_IN_DB(db(db.room.is_active == True),
									db.room.id, '%(name)s'),
							  IS_NOT_EMPTY()]


db.define_table('assign_detail',
    Field('assign_id', 'reference assign'),
    Field('device_id', 'reference device'),
    Field('serial', 'string'),
    Field('asset_number', 'string'),
    Field('device_color', 'string')
    )


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

if db(db.config_group).count() < 1:
	db.config_group.bulk_insert([
		dict(name=myconf.get('default_type.acs')),
		dict(name=myconf.get('default_type.app')),
		dict(name=myconf.get('default_type.dpt')),
		dict(name=myconf.get('default_type.dvc')),
		dict(name=myconf.get('default_type.eml')),
		dict(name=myconf.get('default_type.loc')),
		dict(name=myconf.get('default_type.lnc')),
		dict(name=myconf.get('default_type.opt')),
		dict(name=myconf.get('default_type.pln')),
		dict(name=myconf.get('default_type.usr'))
	])
