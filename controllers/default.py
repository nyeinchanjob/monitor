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

def device_brand():
    brand_grid = SQLFORM.smartgrid(
        db.device_brand,
        paginate=25,
        csv=True,
        details=False,
        orderby=~db.device_brand.id,
        linked_tables=False
    )
    response.moduleTitle = "Brand"
    return dict(form_device_brand= brand_grid)

def device_model():
    model_grid = SQLFORM.smartgrid(
        db.device_model,
        paginate=25,
        csv=True,
        details=False,
        orderby=~db.device_model.id,
        linked_tables=False
    )
    response.moduleTitle = "Model"
    return dict(form_device_model= model_grid)

def device_os():
    os_grid = SQLFORM.smartgrid(
        db.os_type,
        paginate=25,
        csv=True,
        details=False,
        orderby=~db.os_type.id,
        linked_tables=False
    )
    response.moduleTitle = "Device OS"
    return dict(form_os_type= os_grid)

def device_type():
    type_grid = SQLFORM.smartgrid(
        db.device_type,
        paginate=25,
        csv=True,
        details=False,
        orderby=~db.device_type.id,
        linked_tables=False
    )
    response.moduleTitle = "Device Type"
    return dict(form_device_type= type_grid)

def device():
    grid = SQLFORM.smartgrid(
        db.device,
        paginate=25,
        csv=True,
        details=False,
        orderby=[db.device.device_type_id, db.device.name],
        linked_tables=False
    )

    response.moduleTitle = "Device"
    return dict(form_device=grid, dcode=json(d_code))

def apps_type():
    type_grid = SQLFORM.smartgrid(
        db.apps_type,
        paginate=25,
        csv=True,
        details=False,
        orderby=~db.apps_type.id,
        linked_tables=False
    )
    response.moduleTitle = "Application Type"
    return dict(form_app_type= type_grid)

def apps():
    apps_grid = SQLFORM.smartgrid(
        db.apps,
        paginate=25,
        csv=True,
        details=False,
        orderby=~db.apps.id,
        linked_tables=False
    )
    response.moduleTitle = "Applications"
    return dict(form_apps = apps_grid)

def app_assign():

    def redirectToAppDetail(form):
        app_assign_id = form.vars.id
        redirect(URL('app_assign_detail', vars=dict(app_assign_id=app_assign_id)))
    form=SQLFORM.grid(db.app_assign,
                        oncreate=redirectToAppDetail,
                        onupdate=redirectToAppDetail,
                        details=False,
                        paginate=25,
                        orderby=~db.app_assign.id|db.app_assign.app_type_id
                        )
    response.moduleTitle = 'Application Assign'
    return dict(form=form)

def app_assign_detail():
    app_assign_id=request.vars.app_assign_id
    if type(app_assign_id) == list:
        app_assign_id=app_assign_id[-1]
    db.app_assign_detail.app_assign_id.default = app_assign_id
    form_app_assign_detail = SQLFORM(db.app_assign_detail)
    form_app_assign_detail.add_button('Back', URL('default', 'app_assign'))
    if form_app_assign_detail.process().accepted:
        redirect(URL('app_assign_detail', vars=dict(app_assign_id=app_assign_id)))

    response.moduleTitle = 'Applications Assign Detail'
    return dict(form_app_assign_detail=form_app_assign_detail, app_assign_id=app_assign_id)

def app_assign_detail_list():
    #db.assign_device.device_id.requires = IS_IN_DB(db(db.device.is_active==True), db.device.id, '%(name)s')
    app_assign_id = request.vars.app_assign_id
    app_assign_detail_where = (db.app_assign_detail.app_assign_id == app_assign_id)
    app_assign_detail_grid = SQLFORM.grid(app_assign_detail_where, fields=[db.app_assign_detail.id,
                db.app_assign_detail.apps_id],
        		create=False,
        		searchable=False,
        		editable=False,
        		details=False,
        		csv=True,
        		paginate=5,
        		orderby=~db.app_assign_detail.app_assign_id
    		)
    return dict(app_assign_detail_grid=app_assign_detail_grid)

def sim_plan():
    grid = SQLFORM.smartgrid(db.sim_plan,
        paginate=20,
        csv=True,
        details=False,
        orderby=~db.sim_plan.id,
        linked_tables=False)
    response.moduleTitle = 'SIM Plan'
    return dict(form=grid)

def sim_brand():
    grid= SQLFORM.smartgrid(db.sim_brand,
        paginate=20,
        csv=True,
        details=False,
        orderby=~db.sim_brand.id,
        linked_tables=False)

    response.moduleTitle= 'SIM Brand'
    return dict(form=grid)

def sim():
    grid = SQLFORM.smartgrid(db.sim,
                                paginate=20,
                                csv=True,
                                details=False,
                                orderby=~db.sim.id|db.sim.brand_type_id,
                                linked_tables=False
                                )
    response.moduleTitle = 'SIM Card'
    return dict(form=grid)


def department():
    grid = SQLFORM.smartgrid(
        db.department,
        paginate=20,
        csv=True,
        details=False,
        orderby=~db.department.id,
        linked_tables=False
    )
    response.moduleTitle = 'Department'
    return dict(form=grid)

def location_plant():
    grid = SQLFORM.smartgrid(db.location_plant,
        paginate=20,
        csv=True,
        details=False,
        orderby=~db.location_plant.id,
        linked_tables=False)

    response.moduleTitle='Plant'
    return dict(form=grid)

def printer_location():
    grid = SQLFORM.smartgrid(db.printer_location,
        paginate=20,
        csv=True,
        details=False,
        orderby=~db.printer_location.id,
        linked_tables=False)

    response.moduleTitle='Printer Location'
    return dict(form=grid)


def employee():
    grid = SQLFORM.smartgrid(
        db.employee,
        paginate=20,
        csv=True,
        details=False,
        orderby=[db.employee.department_id, db.employee.name],
        linked_tables=False
    )

    response.moduleTitle = 'Employee'
    return dict(form=grid)

def account_type():
    grid = SQLFORM.smartgrid(
        db.account_type,
        paginate=20,
        csv=True,
        details=False,
        orderby=~db.account_type.id,
        linked_tables=False
    )

    response.moduleTitle = 'EMail Type'
    return dict(form=grid)

def email_type():
    grid = SQLFORM.smartgrid(
        db.email_type,
        paginate=20,
        csv=True,
        details=False,
        orderby=~db.email_type.id,
        linked_tables=False
    )

    response.moduleTitle = 'EMail Type'
    return dict(form=grid)

def license_type():
    grid = SQLFORM.smartgrid(
        db.license_type,
        paginate=20,
        csv=True,
        details=False,
        orderby=~db.license_type.id,
        linked_tables=False
    )

    response.moduleTitle = 'License Type'
    return dict(form=grid)


def email_account():
    grid = SQLFORM.smartgrid(
        db.email_account,
        paginate=20,
        csv=True,
        details=False,
        orderby=[db.email_account.email_type_id, db.email_account.username],
        linked_tables=False)
    response.moduleTitle = 'Email Account'
    return dict(form=grid)

def device_accessories():
    grid = SQLFORM.smartgrid(
        db.device_accessories,
        paginate=20,
        csv=True,
        details=False,
        orderby=~db.device_accessories.id,
        linked_tables=False)
    response.moduleTitle = 'Accessories'
    return dict(form=grid)


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
        csv=True,
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
    db.assign_device.device_id.requires=IS_IN_DB(db(db.device.is_active=='T'), db.device.id, '%(name)s')
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
    form_device.add_button('Back', URL('default', 'assign'))
    form_device.add_button('Back', URL('default', 'assign'))
    form_app.add_button('Back', URL('default', 'assign'))
    if form_device.process().accepted:
        redirect(URL('assigndetail', vars=dict(assign_id=assign_id)))
    if form_app.process().accepted:
        redirect(URL('assigndetail', vars=dict(assign_id=assign_id)))
    if form_accessories.process().accepted:
        redirect(URL('assigndetail', vars=dict(assign_id=assign_id)))

    response.moduleTitle = 'Assign Detail'
    return dict(form_device=form_device, form_app=form_app, form_accessories=form_accessories, assign_id=assign_id)

def assigndetaillist():
    #db.assign_device.device_id.requires = IS_IN_DB(db(db.device.is_active==True), db.device.id, '%(name)s')
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
		csv=True,
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
		csv=True,
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
		csv=True,
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
