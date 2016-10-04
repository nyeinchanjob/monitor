# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
from gluon.contrib.appconfig import AppConfig
from gluon.serializers import json
from gluon.tools import geocode

myconf = AppConfig(reload=True)

@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    # current_page = request.vars.page or None
    # print request.vars
    # response.title += ' | ' + T('Posts')
    # if not current_page:
    #     redirect(URL('index'))
    # else:
    #     page = int(current_page)

    response.flash = T("Welcome")
    return dict(message=T('Welcome to web2py!'))


def about():
    return dict(message="This is about")

latitude = longitude = ''
def getGPS():
    form=SQLFORM.factory(Field('search'), _class='form-search')
    form.custom.widget.search['_class'] = 'input-long search-query'
    form.custom.submit['_value'] = 'Search'
    form.custom.submit['_class'] = 'btn'
    if form.accepts(request):
        address=form.vars.search
        (latitude, longitude) = geocode(address)
    else:
        (latitude, longitude) = ('','')
    return dict(form=form, latitude=latitude, longitude=longitude)

def brand():
    grid = SQLFORM.smartgrid(
        db.brand,
        paginate=10,
        csv=False,
        details=False,
        orderby = db.brand.name,
        linked_tables=False
    )
    response.moduleTitle = 'Brand'
    return dict(form=grid)
    ##data = db().select(db.brand.ALL, orderby=~db.brand.id)
    ##return dict(form=SQLFORM(db.brand).process(), data=data)

def model():
    grid = SQLFORM.smartgrid(
        db.model,
        paginate=10,
        csv=False,
        details=False,
        orderby=[db.model.brand, db.model.name],
        linked_tables=False
    )

    # grid=SQLFORM(db.model).process()
    response.moduleTitle = 'Model'
    return dict(form=grid)

def general_table():
    grid = SQLFORM.smartgrid(
        db.general_table,
        paginate=10,
        csv=False,
        details=False,
        orderby=[db.general_table.config_type, db.general_table.name],
        linked_tables=False
    )

    response.moduleTitle = 'Genral Set up'
    return dict(form=grid)

def sim():
    grid = SQLFORM.smartgrid(
        db.sim,
        paginate=10,
        csv=False,
        details=False,
        orderby=[db.sim.brand_type, db.sim.plan_type, db.sim.sim_number],
        linked_tables=False
    )
    response.moduleTitle = 'SIM Card'
    return dict(form=grid)


def room():
    grid = SQLFORM.smartgrid(
        db.room,
        paginate=10,
        csv=False,
        details=False,
        orderby=[db.room.config, db.sim.name],
        linked_tables=False
    )
    response.moduleTitle = 'Room'
    return dict(form=grid, lcode=json(l_code))

def apps():
    grid = SQLFORM.smartgrid(
        db.apps,
        paginate=10,
        csv=False,
        details=False,
        orderby=[db.apps.app_type, db.apps.name],
        linked_tables=False
    )
    response.moduleTitle = 'Application'
    return dict(form=grid)

def employee():
    grid = SQLFORM.smartgrid(
        db.employee,
        paginate=10,
        csv=False,
        details=False,
        orderby=[db.employee.department, db.employee.name],
        linked_tables=False
    )

    response.moduleTitle = 'Brand'
    return dict(form=grid)

def email_account():
    grid = SQLFORM.smartgrid(
        db.email_account,
        paginate=10,
        csv=False,
        details=False,
        orderby=[db.email_account.user_type, db.email_account.username],
        linked_tables=False
    )

    response.moduleTitle = 'Brand'
    return dict(form=grid)

def device():
    grid = SQLFORM.smartgrid(
        db.device,
        paginate=10,
        csv=False,
        details=False,
        orderby=[db.device.device_type, db.device.name],
        linked_tables=False
    )
    response.moduleTitle = 'Device'
    return dict(form=grid, dcode=json(d_code))

def register():
    form=SQLFORM.factory(db.client,db.address)
    if form.process().accepted:
        id = db.client.insert(**db.client._filter_fields(form.vars))
        form.vars.client=id
        id = db.address.insert(**db.address._filter_fields(form.vars))
        response.flash='Thanks for filling the form'
    response.moduleTitle = 'Register'
    return dict(form=form)

def rent():
    grid = SQLFORM.smartgrid(
        db.rent,
        paginate=10,
        csv=False,
        details=False,
        orderby=~db.rent.rent_date|db.rent.employee_id,
        linked_tables=False
    )

    response.moduleTitle = 'Rent'
    return dict(form=grid)

def assign():

	def redirectToDetail(form):
		assign_id = form.vars.id
		redirect(URL('assigndetail', vars=dict(assign_id=assign_id)))
	form=SQLFORM.grid(db.assign,
		oncreate=redirectToDetail,
		onupdate=redirectToDetail,
		details=False,
		paginate=15,
		orderby=~db.assign.id|db.assign.employee_id
        )
	response.moduleTitle = 'Assign'
	return dict(form=form)

def assigndetail():
	assign_id=request.vars.assign_id
	if type(assign_id) == list:
		assign_id=assign_id[-1]
	db.assign_device.assign_id.default = assign_id
	db.assign_app.assign_id.default = assign_id
	db.assign_accessories.assign_id.default = assign_id
	db.assign_sim.assign_id.default = assign_id
	form_device = SQLFORM(db.assign_device)
	form_app = SQLFORM(db.assign_app)
	form_accessories = SQLFORM(db.assign_accessories)
	form_sim = SQLFORM(db.assign_sim)
	form_device.add_button('Back', URL('default', 'assign'))
	form_device.add_button('Back', URL('default', 'assign'))
	form_app.add_button('Back', URL('default', 'assign'))
    form_accessories.add_button('Back', URL('default', 'assign'))
    form_sim.add_button('Back', URL('default', 'assign'))

	if form_device.process().accepted:
		redirect(URL('assigndetail', vars=dict(assign_id=assign_id)))
	if form_app.process().accepted:
		redirect(URL('assigndetail', vars=dict(assign_id=assign_id)))
	if form_accessories.process().accepted:
		redirect(URL('assigndetail', vars=dict(assign_id=assign_id)))
	if form_sim.process().accepted:
        redirect(URL('assigndetail', vars=dict(assign_id=assign_id)))

	response.moduleTitle = 'Assign Detail'
	return dict(form_device=form_device, form_app=form_app, form_accessories=form_accessories, form_sim=form_sim, assign_id=assign_id)

def assigndetaillist():
	assign_id = request.vars.assign_id
	device_where = (db.assign_device.assign_id == assign_id)
	device_grid = SQLFORM.grid(device_where, fields=[db.assign_device.id,
            db.assign_device.device_id, db.assign_device.serial,
            db.assign_device.is_used, db.assign_device.is_damaged,
            db.assign_device.is_lost],
		create=False,
		searchable=False,
		editable=False,
		details=False,
		csv=False,
		paginate=5,
		orderby=~db.assign_device.device_id
		)
	return dict(device_grid=device_grid)

def assignapplist():
	assign_id = request.vars.assign_id
	app_where = (db.assign_app.assign_id == assign_id)
	app_grid = SQLFORM.grid(app_where, fields=[db.assign_app.id, db.assign_app.app_id],
		create=False,
		searchable=False,
		editable=False,
		details=False,
		csv=False,
		paginate=5,
		orderby=~db.assign_app.app_id
		)
	return dict(app_grid=app_grid)

def assignaccessorieslist():
	assign_id = request.vars.assign_id
	accessories_where = (db.assign_accessories.assign_id == assign_id)
	accessories_grid = SQLFORM.grid(accessories_where, fields=[db.assign_accessories.id, db.assign_accessories.accessories_id,
        db.assign_accessories.serial, db.assign_accessories.is_used,
        db.assign_accessories.is_damaged, db.assign_accessories.is_lost],
		create=False,
		searchable=False,
		editable=False,
		details=False,
		csv=False,
		paginate=5,
		orderby=~db.assign_accessories.accessories_id
		)
	return dict(accessories_grid=accessories_grid)

def assignsimlist():
	assign_id = request.vars.assign_id
	sim_where = (db.assign_sim.assign_id == assign_id)
	sim_grid = SQLFORM.grid(sim_where, fields=[db.assign_sim.id, db.assign_sim.sim_id, db.assign_sim.is_used,
    db.assign_sim.is_damaged, db.assign_sim.is_lost],
		create=False,
		searchable=False,
		editable=False,
		details=False,
		csv=False,
		paginate=5,
		orderby=~db.assign_accessories.accessories_id
		)
	return dict(accessories_grid=accessories_grid)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())




@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
