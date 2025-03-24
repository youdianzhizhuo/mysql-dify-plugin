from tools.mysql_query import MySQLQueryTool
from dify_plugin import ToolProvider

class MySQLProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict) -> None:
        # 验证必要参数存在
        required_fields = ['host', 'port', 'username', 'password', 'database']
        for field in required_fields:
            if field not in credentials:
                raise ValueError(f"Missing required field: {field}")
        
        # 初始化工具实例
        MySQLQueryTool()