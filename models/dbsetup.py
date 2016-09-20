from datetime import datetime

## brand
db.define_table('brand',
	Field('name', 'string', requires=[IS_NOT_EMPTY()]),
	Field('is_active', 'boolean', default=True),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False),
	format='%(name)s')
## Model
db.define_table('model',
	Field('name', 'string', requires=[IS_NOT_EMPTY()]),
	Field('brand', 'reference brand', requires=[ IS_IN_DB(db, db.brand.id, '%(name)s'), IS_NOT_EMPTY() ]),
	Field('is_active', 'boolean', default=True),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False))


## Config
db.define_table('config',
	Field('name', 'string', requires=[IS_NOT_EMPTY()]),
	Field('config_type', 'string', requires=[IS_NOT_EMPTY()]),
	Field('is_active', 'boolean', default=True),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False))

## apps
db.define_table('apps',
	Field('name', 'string', requires=[IS_NOT_EMPTY()]),
	Field('is_active', 'boolean', default=True),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False))

## employee
db.define_table('employee',
	Field('name', 'string', requires=[IS_NOT_EMPTY()]),
	Field('job_title', 'string'),
	Field('department', 'string'),
	Field('email', 'string', requires=[IS_NOT_EMPTY(), IS_EMAIL()]),
	Field('is_active', 'boolean', default=True),
	Field('created_on', 'datetime', default=request.now,
			readable=True, writable=False),
	Field('created_by', 'reference auth_user', default=auth.user_id,
			readable=True, writable=False),
	Field('modified_on', 'datetime', update=request.now,
			readable=True, writable=False),
	Field('modified_by', 'reference auth_user', update=auth.user_id,
			readable=True, writable=False))

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
