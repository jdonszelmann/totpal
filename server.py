if __name__ == '__main__': (lambda articles, app, named, shuffle, argv: [app.route("/")(named(lambda: open(argv[1]).read().replace("NUMBER", str(len(articles))), "home")),app.route('/submit', methods=['POST'])(named(lambda: [(lambda s: [articles.append(s),f"submit {s} OK"][1])(__import__("flask").request.form["article"])], "submit")),app.route('/random', methods=['GET'])(named(lambda: [[shuffle(articles), articles[0]][1] if len(articles) else "no articles submitted"], "random")),app.route('/all', methods=['GET'])(named(lambda: f"{[shuffle(articles), articles][1] if len(articles) else []}", "all")),app.route('/reset')(named(lambda: [articles.clear(),"rest OK (jana can't spell sorry)"][1], "reset")),app.run(host= '0.0.0.0', debug=True ,port=2442)])([], __import__("flask").Flask(__name__), lambda x, n: type(n, (), {"__call__": lambda _, *__, **___: __import__("flask").Response(x(), mimetype="text/html"), "__name__": n})(), __import__("random").shuffle, __import__("sys").argv)
