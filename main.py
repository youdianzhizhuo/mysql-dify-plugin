from dify_plugin import Plugin, DifyPluginEnv

plugin = Plugin(DifyPluginEnv(
    MAX_REQUEST_TIMEOUT=120,
    REQUIRED_PYTHON_PACKAGES=[
        'mysql-connector-python>=8.1.0'
    ]
))

if __name__ == '__main__':
    plugin.run()