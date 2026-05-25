from api import config, permission

permission.create("manage_boards", "Manage Boards", "manage_channels")
config.create_field("boards", dict)