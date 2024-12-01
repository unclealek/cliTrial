# Clinical Trials API

A Flask-based REST API for managing clinical trials data.

## Prerequisites

- Docker
- Docker Compose
- Python 3.x (if running locally)

## Installation

### Using Docker (Recommended)

1. Clone the repository:
git clone <repository-url>
cd clinical-trials-a

2. Build and run the Docker container:
bash
docker-compose up --build

The API will be available at `http://localhost:5000`

### Local Installation

1. Create and activate a virtual environment:
bash
python -m venv myenv
source myenv/bin/activate # On Windows: myenv\Scripts\activate

2. Install dependencies:
pip install -r requirements.txt


3. Run the application:
bash
flask run

## API Endpoints

(Here you should list your API endpoints, for example:)

- `GET /trials` - Retrieve all clinical trials
- `GET /trials/<id>` - Retrieve a specific trial
- `POST /trials` - Create a new trial
- `PUT /trials/<id>` - Update an existing trial
- `DELETE /trials/<id>` - Delete a trial

## Environment Variables

The following environment variables can be configured:

- `FLASK_ENV`: Set to `development` for development mode
- `FLASK_APP`: Set to `croApi.py` (your main application file)

## Project Structure
clinical-trials-api/
├── croApi.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


## Development

To run the application in development mode:

1. Make sure Docker is running
2. Run `docker-compose up`
3. The API will automatically reload when changes are made to the code

## License

VerticalX
# cliTrial
