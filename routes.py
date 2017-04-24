ROUTES = (
    (r'/api/v1/portal/role/', 'app.handlers.role_handler.RoleHandler'),
    (r'/api/v1/portal/role/tag/', 'app.handlers.role_handler.RoleTagHandler'),
    (r'/api/v1/portal/camp/name_id_list/', 'app.handlers.camp_handler.CampNameIdListHandler'),
    (r'/api/v1/portal/organize/name_id_list/', 'app.handlers.organize_handler.OrganizeNameIdListHandler'),
    (r'/api/v1/portal/user/', 'app.handlers.user_handler.UserHandler'),
    (r'/api/v1/portal/medal/', 'app.handlers.medal_handler.MedalHandler'),
    (r'/api/v1/portal/role/task/', 'app.handlers.task_handler.TaskRecordHandler'),
    (r'/api/v1/portal/topics/', 'app.handlers.topic_handler.TopicHandler'),
)
