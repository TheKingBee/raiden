from gevent import monkey

monkey.patch_all()


if __name__ == "__main__":
    from .main import main
    main()
