# flask_pastedeploy

flask_pastedeploy 是一个将flask app 作为pastedeploy pipeline的app.

## 快速使用

``` python
# 在flask init_app加载完成所有app后，生成pastedeploy对象

from flask_pastedeploy import PasteDeployWrapper
from werkzeug.serving import run_simple

paste = PasteDeployWrapper()
deploy = paste.setup_app(app)

```

启动web服务, `run_simple`是Flask 启动服务的一个方法，方法中可以传入很多参数

```
run_simple("localhost", 9999, deploy)
```
以后，与pastedeploy使用无异

## 与flask before_app_request对比
* 使用flask before_app_request可以在视图函数前处理，看起来也更简单。
* 使用pastedeploy更灵活，且更好维护