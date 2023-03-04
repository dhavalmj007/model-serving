from uvicorn import run


def main():
    from src.app import app
    run(
        app,
        host='0.0.0.0',
        port=4010,
        http='h11',
        debug=False,
        reload=False,
        access_log=False
    )


if __name__ == '__main__':
    main()
