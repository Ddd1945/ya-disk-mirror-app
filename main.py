from waitress import serve
from website import create_app, config

app = create_app()

if __name__ == '__main__':
    if config.APP_MODE == 'dev':
        app.run(
            host=config.APP_HOST,
            port=config.APP_PORT,
            debug=config.DEBUG,
            use_reloader=config.USE_RELOADER
        )
    else:
        serve(
            app=app,
            host=config.APP_HOST,
            port=config.APP_PORT,
            threads=config.THREADS
        )
