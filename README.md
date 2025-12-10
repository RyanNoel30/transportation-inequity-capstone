# Transportation Inequity Capstone

A project analyzing transportation inequity and investigating how transportation inequality manifests across regions.

**Key Research Questions:**
- Who has the longest commutes?
- Who pays the most for transportation?
- Which communities benefit most—or least—from transit infrastructure?

## Project Structure

```
transportation-inequity-capstone/
├── src/
│   ├── backend/
│   │   ├── main.py          # Main entry point
│   │   ├── etl.py           # ETL functions
│   │   ├── database.py      # Database management
│   │   └── models.py        # Data models
│   │
│   ├── frontend_v2/         # Streamlit dashboard
│   │   ├── app.py           # Main dashboard app
│   │   ├── api_client.py    # API integration
│   │   ├── components/      # UI components
│   │   └── utils/           # Utility functions
│   │
│   └── data/
│       ├── raw/             # Raw data files
│       └── processed/       # Processed data files
│
├── requirements.txt         # Project dependencies
├── README.md               # This file
└── .env                    # Environment variables (not tracked)
```

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in `.env`

3. Run the main application:
   ```bash
   python src/backend/main.py
   ```

4. Run the Streamlit dashboard:
   ```bash
   streamlit run src/frontend_v2/app.py
   ```

## Features

- **Backend**: ETL pipeline and data processing
- **Frontend**: Interactive Streamlit dashboard with:
  - Key metrics visualization
  - Transportation mode analysis
  - Regional cost burden comparison
  - Geographic distribution maps
  - Data insights and analysis
=======
>>>>>>> 3d085fe2aafc5795a7b8946fd3af84d66a1af69c
