=======
# Weather Data Fetcher

This project is a simple Python application that fetches and displays current weather data for a specified city using the OpenWeatherMap API.

## Project Structure

```
weather-app
└── weather-app
|   ├── src
|       ├── main.py          # Entry point of the application
|       └── weather
|           ├── __init__.py  # Initializes the weather package
|           └── api.py       # Contains functions to interact with the OpenWeatherMap API
|   ├── requirements.txt      # Lists project dependencies
|   └── README.md             # Project documentation
```

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenWeatherMap and set it in your environment variables or directly in the code.

## Usage

To run the application, execute the following command:
```
python src/main.py
```

You will be prompted to enter the name of the city for which you want to fetch the current weather data.

## License

This project is licensed under the MIT License.
