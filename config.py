import  os

app_env = os.getenv("", 'b')



CCS_DB = {
    'user': os.getenv('DB_USER', 'ccs_external'),
    'pw': os.getenv('DB_PW', '32vfek5n'),
    'host': os.getenv('DB_HOST', '192.168.1.9'),
    'port': os.getenv('DB_PORT', 3360),
    'db': os.getenv('DB_NAME', 'ccs_external'),
}