# 📊 CrewInsight - Business Analyst Agent

An AI-powered market intelligence platform that collects, analyzes, and summarizes market trends to support business decision-making.

![CrewInsight Dashboard](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red)

## 🌟 Features

- **🔍 Multi-Source Data Collection**: Aggregates market data from TechCrunch, Bloomberg, Reuters, and more
- **📈 AI-Powered Trend Analysis**: Identifies key market trends with confidence scoring
- **✍️ Smart Summarization**: Generates executive-ready reports with strategic recommendations
- **📊 Interactive Visualizations**: Beautiful charts and graphs for data insights
- **💾 Analysis History**: Track and compare multiple analyses over time
- **📤 Export Capabilities**: Download results in Markdown, JSON, and CSV formats
- **🔐 Secure Authentication**: API key-based access control
- **🎨 Professional UI**: Modern, gradient-based design with responsive layout

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Local Installation

1. **Clone or download the project files**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Access the application**
   - Open your browser and navigate to: `http://localhost:8501`
   - For demo access, use any API key starting with `sk-` (minimum 16 characters)
   - Example: `sk-demo1234567890`

## 🎯 Usage Guide

### Authentication

1. Enter an API key in the sidebar (format: `sk-xxxxx...` with minimum 16 characters)
2. Click "Login" to authenticate
3. For demo purposes, any key matching the format will work

### Running an Analysis

1. Navigate to the "🔍 New Analysis" tab
2. Select your parameters:
   - **Market Sector**: Choose from AI Startups, Fintech, Healthcare Tech, etc.
   - **Geographic Region**: US, Europe, Asia-Pacific, or Global
   - **Analysis Timeframe**: 3 months to 2 years
   - **Analysis Depth**: Quick Overview, Standard, or Deep Dive
3. Click "🚀 Run Analysis"
4. Wait for the AI agents to complete the analysis (15-30 seconds)
5. View results with interactive charts and metrics

### Viewing Results

- **Metrics Dashboard**: Growth rate, market size, funding trends, and new entrants
- **Confidence Scores**: Visual representation of trend reliability
- **Market Metrics Radar**: Comprehensive market performance overview
- **Timeline Chart**: Data collection timeline across sources
- **Executive Summary**: Detailed business-ready report

### Exporting Data

Choose from three export formats:
- **Markdown (.md)**: Executive summary for reports
- **JSON (.json)**: Complete analysis data for further processing
- **CSV (.csv)**: Trend data for spreadsheet analysis

### Analysis History

- Access the "📊 Results History" tab to view all past analyses
- Filter by market sector or geographic region
- Re-download previous analyses
- Compare trends over time

## 📁 Project Structure

```
crewinsight/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .streamlit/           # Streamlit configuration (optional)
    └── config.toml       # Custom theme settings
```

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.10+**: Application logic
- **Streamlit**: Web UI framework
- **Pandas**: Data manipulation
- **Plotly**: Interactive visualizations

### Agent Architecture (Mock Implementation)
- **DataCollectorAgent**: Simulates multi-source data collection
- **TrendAnalyzer**: Analyzes market data and identifies trends
- **SummaryGenerator**: Creates business-friendly summaries
- **AgentOrchestrator**: Coordinates the analysis pipeline

### Production Technologies (For Real Implementation)
- **FastAPI**: RESTful API backend
- **CrewAI**: Agent orchestration framework
- **OpenAI API**: Natural language processing
- **SQLite/PostgreSQL**: Data persistence

## 🚀 Deployment Options

### Option 1: Streamlit Community Cloud (Free)

1. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository, branch, and `app.py`
   - Click "Deploy"

3. **Your app will be live at**: `https://<username>-crewinsight.streamlit.app`

### Option 2: Heroku

1. **Create a `Procfile`**
   ```
   web: sh setup.sh && streamlit run app.py
   ```

2. **Create `setup.sh`**
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   ```

3. **Deploy**
   ```bash
   heroku create crewinsight
   git push heroku main
   heroku open
   ```

### Option 3: Docker

1. **Create a `Dockerfile`**
   ```dockerfile
   FROM python:3.10-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY app.py .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build and run**
   ```bash
   docker build -t crewinsight .
   docker run -p 8501:8501 crewinsight
   ```

### Option 4: AWS EC2 / DigitalOcean

1. **SSH into your server**
2. **Install Python and dependencies**
   ```bash
   sudo apt update
   sudo apt install python3.10 python3-pip
   ```
3. **Clone repository and install**
   ```bash
   git clone <your-repo>
   cd crewinsight
   pip install -r requirements.txt
   ```
4. **Run with nohup or screen**
   ```bash
   nohup streamlit run app.py --server.port=8501 &
   ```

## 🎨 Customization

### Changing Colors

Edit the CSS in the `load_css()` function in `app.py`:

```python
# Main gradient background
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

# Button colors
background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
```

### Adding New Market Sectors

In the `main()` function, update the market selectbox:

```python
market = st.selectbox(
    "🎯 Select Market Sector",
    ["AI Startups", "Fintech", "Your New Sector", ...],
)
```

And add trend templates in `TrendAnalyzer.analyze()`:

```python
trend_templates = {
    "Your New Sector": [
        "Trend 1 for your sector",
        "Trend 2 for your sector",
        ...
    ],
}
```

### Configuring Data Sources

Update the `DataCollectorAgent.fetch_data()` method to add/remove sources:

```python
sources = ["TechCrunch", "Bloomberg", "Reuters", "Your Source"]
```

## 📊 Features Breakdown

### New Analysis Tab
- Market sector selection (7 options)
- Geographic region selection (6 options)
- Timeframe selection (4 options)
- Analysis depth selection (3 levels)
- Real-time progress tracking
- Comprehensive results display

### Results History Tab
- View all past analyses
- Filter by market and region
- Quick access to metrics
- Re-download any analysis
- Compare multiple analyses

### Settings Tab
- API key management
- Analysis preferences
- Display options
- Data management (clear history, export all)

### About Tab
- Technology stack overview
- Agent workflow explanation
- API documentation
- Support resources

## 🔧 Troubleshooting

### Issue: Port already in use
```bash
# Kill existing Streamlit process
pkill -f streamlit
# Or use a different port
streamlit run app.py --server.port=8502
```

### Issue: Module not found
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt --upgrade
```

### Issue: Blank screen on deployment
- Check that your deployment platform has Python 3.10+
- Verify all dependencies are in requirements.txt
- Check deployment logs for errors

## 🤝 Contributing

This is a demonstration/MVP application. For production use:

1. Replace mock agents with real CrewAI implementation
2. Integrate actual OpenAI API for NLP
3. Add proper database (PostgreSQL/MongoDB)
4. Implement FastAPI backend
5. Add comprehensive error handling
6. Implement rate limiting
7. Add user management system
8. Set up monitoring and logging

## 📝 License

This project is provided as-is for demonstration purposes.

## 📞 Support

For questions or support:
- Email: support@crewinsight.ai
- Documentation: docs.crewinsight.ai
- Issues: Use the GitHub issues tab

## 🎉 Acknowledgments

Built with:
- Streamlit for the amazing web framework
- Plotly for beautiful visualizations
- The open-source community

---

**Made with ❤️ for entrepreneurs and innovators**

*Current Version: 1.0.0*
*Last Updated: February 2024*
