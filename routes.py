ROUTES = (
    (r'/api/v1/portal/role/', 'app.handlers.role_handler.RoleHandler'),
    (r'/api/v1/portal/camp/name_id_list/', 'app.handlers.camp_handler.CampNameIdListHandler'),
    (r'/api/v1/portal/organize/name_id_list/', 'app.handlers.organize_handler.OrganizeNameIdListHandler'),
)
