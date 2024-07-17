tags:: TODO, framework

-
- Flask is flexible. It doesn’t require you to use any particular project or code layout.
- However, when first starting, it’s helpful to use a more structured approach. This means that the tutorial will require a bit of boilerplate up front, but it’s done to avoid many common pitfalls that new developers encounter, and it creates a project that’s easy to expand on.
- Once you become more comfortable with Flask, you can step out of this structure and take full advantage of Flask’s flexibility.
- [[sqlite]]
  - SQLite is convenient because it doesn’t require setting up a separate database server and is built-in to Python. However, if concurrent requests try to write to the database at the same time, they will slow down as each write happens sequentially. Small applications won’t notice this. Once you become big, you may want to switch to a different database.
    session is what ???
    what that effection ???
- # Endpoints and URLs
  - The url_for() function generates the URL to a view based on a name and arguments. The name associated with a view is also called the endpoint, and by default it’s the same as the name of the view function.
    For example, the hello() view that was added to the app factory earlier in the tutorial has the name 'hello' and can be linked to with url_for('hello'). If it took an argument, which you’ll see later, it would be linked to using url_for('hello', who='World').
    When using a blueprint, the name of the blueprint is prepended to the name of the function, so the endpoint for the login function you wrote above is 'auth.login' because you added it to the 'auth' blueprint.
- # view->template?!
  - https://flask.palletsprojects.com/en/2.0.x/tutorial/templates/
    You’ve written the authentication views for your application, but if you’re running the server and try to go to any of the URLs, you’ll see a TemplateNotFound error. That’s because the views are calling render_template(), but you haven’t written the templates yet. The template files will be stored in the templates directory inside the flaskr package.
  - Flask uses the [Jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/) template library to render templates.
    Jinja looks and behaves mostly like Python. Special delimiters are used to distinguish Jinja syntax from the static data in the template. Anything between {{ and }} is an expression that will be output to the final document. {% and %} denotes a control flow statement like if and for. Unlike Python, blocks are denoted by start and end tags rather than indentation since static text within a block could change indentation. Jinja 的外观和行为很像 Python。 使用特殊分隔符 将 Jinja 语法与模板中的静态数据区分开来。 之间的任何东西 {{和 }}是一个将被输出的表达式 到最终文件。 {%和 %}表示控制流 像这样的语句 if和 for. 与 Python 不同，块被表示 通过开始和结束标签而不是缩进，因为其中的静态文本 一个块可以改变缩进。
- 模板是包含静态数据和占位符的文件  用于动态数据。 使用特定数据呈现模板以生成  最终文件。 Flask 使用 [Jinja ](https://jinja.palletsprojects.com/templates/)模板库进行渲染  模板。
- 在应用程序中，您将使用模板来渲染 [HTML ](https://developer.mozilla.org/docs/Web/HTML)，其  将显示在用户的浏览器中。 在 Flask 中，Jinja 被配置为  *自动转义* HTML 模板中呈现的任何数据。 这表示  呈现用户输入是安全的； 他们输入的任何字符  可能会弄乱 HTML，例如 `<`和 `>`会 *逃脱* 与  *安全* 在浏览器中看起来相同但不会导致不需要的 值  效果。
- Jinja 的外观和行为很像 Python。  使用特殊分隔符 将 Jinja 语法与模板中的静态数据区分开来。 之间的任何东西 `{{`和 `}}`是一个将被输出的表达式 到最终文件。 `{%`和 `%}`表示控制流 像这样的语句 `if`和 `for`.  与 Python 不同，块被表示 通过开始和结束标签而不是缩进，因为其中的静态文本 一个块可以改变缩进。