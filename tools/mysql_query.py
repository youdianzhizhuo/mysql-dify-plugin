from typing import Any, Generator
import mysql.connector
from mysql.connector import Error
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin import Tool

class MySQLQueryTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        try:
            # 建立数据库连接
            connection = mysql.connector.connect(
                host=tool_parameters['host'],
                port=int(tool_parameters['port']),
                user=tool_parameters['username'],
                password=tool_parameters['password'],
                database=tool_parameters['database']
            )
            
            cursor = connection.cursor(dictionary=True)
            cursor.execute(tool_parameters['query'])
            
            # 获取查询结果
            result = cursor.fetchall()
            
            # 格式化输出
            if result:
                columns = result[0].keys()
                table_header = "| " + " | ".join(columns) + " |\n"
                table_separator = "| " + " | ".join(["---"] * len(columns)) + " |\n"
                table_body = ""
                for row in result:
                    table_body += "| " + " | ".join(str(row[col]) for col in columns) + " |\n"
                
                markdown_result = f"Query executed successfully\n\n{table_header}{table_separator}{table_body}"
            else:
                markdown_result = "Query executed successfully. No results returned."
            
            yield self.create_text_message(markdown_result)
            
        except Error as e:
            yield self.create_text_message(f"MySQL Error: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"Execution failed: {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()