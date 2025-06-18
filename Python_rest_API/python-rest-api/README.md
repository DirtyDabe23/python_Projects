# python-rest-api

This project is a simple REST API built using FastAPI. It provides endpoints that return JSON data.

## Project Structure

```
python-rest-api
├── src
│   ├── main.py          # Entry point of the application
│   ├── api
│   │   └── routes.py    # API endpoints
│   └── models
│       └── __init__.py  # Data models and schemas
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-rest-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

## Usage

Once the server is running, you can access the API at `http://127.0.0.1:8000`.

## API Endpoints

- **GET /example**: Returns a sample JSON response.
- **POST /example**: Accepts JSON data and returns it back.

## License

This project is licensed under the MIT License.