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
