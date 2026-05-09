from api import config, permission

permission.create("manage_boards", "manage_channels")
config.create_field("boards", dict)