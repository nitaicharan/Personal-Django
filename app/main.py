import uvicorn
from app.src.infrastructure.app import create_app

app = create_app()


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
