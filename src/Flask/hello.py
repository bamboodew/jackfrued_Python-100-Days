# 首先我们导入了 Flask 类。 该类的实例将会成为我们的 WSGI 应用。
from flask import Flask

# 接着我们创建一个该类的实例。
# 第一个参数是应用模块或者包的名称。
# 如果你使用一个单一模块（就像本例），那么应当使用 __name__ ，
# 因为名称会根据这个模块是按应用方式使用还是作为一个模块导入而发生变化
# （可能是 ‘__main__’ ， 也可能是实际导入的名称）。
# 这个参数是必需的，这样Flask才能知道在哪里可以找到模板和静态文件等东西。更多内容详见Flask文档。
app = Flask(__name__)


# 然后我们使用 route() 装饰器来告诉 Flask 触发函数的 URL 。
@app.route('/')
# 函数名称被用于生成相关联的 URL 。
def hello_world():
    return 'Hello, world!'  # 函数最后返回需要在用户浏览器中显示的信息。


if __name__ == '__main__':
    app.run()
