# 🏗️ CrewInsight Architecture

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                     (Streamlit Web App)                         │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                         │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌──────────┐  ┌──────────┐ │
│  │   New       │  │  Results    │  │ Settings │  │  About   │ │
│  │  Analysis   │  │  History    │  │          │  │          │ │
│  │    Tab      │  │    Tab      │  │   Tab    │  │   Tab    │ │
│  └─────────────┘  └─────────────┘  └──────────┘  └──────────┘ │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION LAYER                          │
├─────────────────────────────────────────────────────────────────┤
│                   AgentOrchestrator                             │
│  • Coordinates agent workflow                                   │
│  • Manages task delegation                                      │
│  • Handles progress tracking                                    │
│  • Returns unified results                                      │
└────────────┬────────────┬────────────┬──────────────────────────┘
             │            │            │
    ┌────────▼───┐   ┌───▼─────┐   ┌─▼──────────┐
    │   Data     │   │  Trend  │   │  Summary   │
    │ Collector  │   │ Analyzer│   │ Generator  │
    │   Agent    │   │  Agent  │   │   Agent    │
    └────────┬───┘   └───┬─────┘   └─┬──────────┘
             │            │            │
             │            │            │
┌────────────▼────────────▼────────────▼──────────────────────────┐
│                       DATA LAYER                                │
├─────────────────────────────────────────────────────────────────┤
│  • Session State (In-Memory)                                    │
│  • Analysis Results Cache                                       │
│  • User Preferences                                             │
│  • Authentication State                                         │
└─────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Presentation Layer (Streamlit UI)

**Technology:** Streamlit 1.31.0

**Components:**
- **New Analysis Tab**
  - Input forms for analysis parameters
  - Progress tracking during execution
  - Results visualization (charts, metrics)
  - Export controls (MD, JSON, CSV)

- **Results History Tab**
  - Historical analysis browser
  - Filtering capabilities
  - Re-download functionality
  - Comparison tools

- **Settings Tab**
  - Authentication management
  - Preference configuration
  - Data management tools

- **About Tab**
  - Documentation
  - API reference
  - Support resources

**Features:**
- Professional gradient UI
- Responsive design
- Interactive visualizations (Plotly)
- Real-time updates

---

### 2. Orchestration Layer

**Component:** `AgentOrchestrator`

**Responsibilities:**
1. Receives analysis requests from UI
2. Coordinates agent execution sequence
3. Manages inter-agent data flow
4. Tracks and reports progress
5. Assembles final results

**Workflow:**
```python
def run_pipeline(request):
    1. Generate unique request_id
    2. Call DataCollectorAgent.fetch_data()
    3. Call TrendAnalyzer.analyze()
    4. Call SummaryGenerator.summarize()
    5. Return unified result object
```

---

### 3. Agent Layer

#### DataCollectorAgent

**Purpose:** Gather market data from multiple sources

**Mock Implementation:**
- Simulates API calls to TechCrunch, Bloomberg, Reuters
- Generates realistic data points with timestamps
- Returns relevance-scored content

**Production Implementation:**
```python
class DataCollectorAgent:
    def fetch_data(market, region, timeframe):
        # Real API integrations
        techcrunch_data = fetch_techcrunch_api()
        bloomberg_data = fetch_bloomberg_api()
        reuters_data = fetch_reuters_api()
        return aggregate_sources()
```

**Output:**
```python
{
    "market": "AI Startups",
    "region": "US",
    "sources": ["TechCrunch", "Bloomberg", "Reuters"],
    "data_points": [...],
    "total_articles": 342
}
```

---

#### TrendAnalyzer

**Purpose:** Process data and identify market trends

**Mock Implementation:**
- Generates 4 market-specific trends
- Calculates confidence scores (75-95%)
- Assigns impact levels and timeframes
- Creates market metrics

**Production Implementation:**
```python
class TrendAnalyzer:
    def analyze(data):
        # CrewAI integration
        analyzer = CrewAI.Agent(
            role="Market Trend Analyst",
            goal="Identify key market trends",
            tools=[sentiment_analysis, pattern_detection]
        )
        return analyzer.execute(data)
```

**Output:**
```python
{
    "trends": [
        {
            "trend": "AI investment surge",
            "confidence": 0.92,
            "impact": "High",
            "timeframe": "Short-term"
        },
        ...
    ],
    "metrics": {
        "growth_rate": 35.2,
        "market_size": 24.5,
        "funding_increase": 48.3,
        "new_entrants": 127
    },
    "sentiment": "Highly Positive",
    "risk_level": "Low"
}
```

---

#### SummaryGenerator

**Purpose:** Create executive-ready business summaries

**Mock Implementation:**
- Builds structured Markdown report
- Includes market overview, trends, recommendations
- Formats for business stakeholders

**Production Implementation:**
```python
class SummaryGenerator:
    def summarize(analysis, market, region):
        # OpenAI integration
        prompt = f"Create executive summary for {market}..."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
```

**Output:**
```markdown
## Executive Summary: AI Startups (US)

### Market Overview
The AI Startups sector demonstrates highly positive momentum...

### Key Trends Identified
1. **Rapid increase in generative AI investments**
   - Confidence: 92%
   - Impact Level: High
   ...
```

---

### 4. Data Layer

**Technology:** Streamlit Session State (In-Memory)

**Storage:**
```python
st.session_state = {
    'authenticated': True,
    'api_key': 'sk-...',
    'analysis_results': [
        {
            'request_id': 'abc123',
            'timestamp': datetime(...),
            'request': {...},
            'data': {...},
            'analysis': {...},
            'summary': "..."
        },
        ...
    ],
    'current_request_id': 'abc123'
}
```

**Persistence:**
- Session-scoped (browser session)
- Cleared on logout/refresh
- Export available for long-term storage

**Production Options:**
- SQLite (lightweight)
- PostgreSQL (scalable)
- MongoDB (document-based)
- Redis (caching)

---

## Data Flow Diagram

```
┌──────┐
│ User │
└──┬───┘
   │ 1. Enters analysis parameters
   ▼
┌─────────────────┐
│  Streamlit UI   │
└────────┬────────┘
         │ 2. Creates request object
         ▼
┌──────────────────────┐
│ AgentOrchestrator    │
└────────┬─────────────┘
         │ 3. Delegates to agents
         │
    ┌────▼────────────────────────┐
    │                             │
    ▼                             ▼
┌──────────────┐         ┌──────────────┐
│DataCollector │────────▶│TrendAnalyzer │
└──────────────┘  data   └──────┬───────┘
                                 │ trends
                                 ▼
                        ┌─────────────────┐
                        │SummaryGenerator │
                        └────────┬────────┘
                                 │ 4. Returns complete result
                                 ▼
                        ┌────────────────┐
                        │ Orchestrator   │
                        └────────┬───────┘
                                 │ 5. Stores in session
                                 ▼
                        ┌────────────────┐
                        │  Session State │
                        └────────┬───────┘
                                 │ 6. Renders results
                                 ▼
                        ┌────────────────┐
                        │  Streamlit UI  │
                        └────────┬───────┘
                                 │ 7. Displays to user
                                 ▼
                               ┌──────┐
                               │ User │
                               └──────┘
```

---

## Technology Stack

### Frontend
- **Streamlit 1.31.0** - Web framework
- **Plotly 5.18.0** - Visualizations
- **Pandas 2.1.4** - Data manipulation

### Backend (Current - Mock)
- **Python 3.10+** - Core language
- **Native Python classes** - Agent simulation

### Backend (Production - Real)
- **FastAPI** - REST API framework
- **CrewAI** - Agent orchestration
- **OpenAI API** - Natural language processing

### Data Storage
- **Current:** Session State (in-memory)
- **Production:** PostgreSQL / MongoDB

### Deployment
- **Streamlit Cloud** - Hosting (recommended)
- **Docker** - Containerization
- **Heroku** - PaaS option

---

## Scalability Considerations

### Current (MVP) Scale
- **Users:** Demo/development
- **Concurrency:** 1 user per session
- **Storage:** Session-scoped
- **Performance:** Suitable for testing

### Production Scale

**API Layer:**
- FastAPI with async handlers
- Load balancer (NGINX)
- Multiple worker processes

**Agent Layer:**
- Queue-based processing (Celery)
- Distributed task execution
- Result caching (Redis)

**Data Layer:**
- Database connection pooling
- Read replicas for queries
- Caching layer

**Infrastructure:**
- Horizontal scaling (multiple instances)
- Auto-scaling based on load
- CDN for static assets

---

## Security Architecture

### Current Implementation
- API key authentication (demo mode)
- Session-based state management
- No persistent storage of sensitive data

### Production Requirements

**Authentication:**
- OAuth 2.0 / JWT tokens
- Rate limiting per API key
- IP whitelisting (optional)

**Data Security:**
- HTTPS/TLS encryption
- Database encryption at rest
- Secure credential storage (vault)

**Access Control:**
- Role-based permissions
- Audit logging
- Request validation

**Compliance:**
- GDPR compliance
- Data retention policies
- Privacy controls

---

## Monitoring & Observability

### Metrics to Track

**Application Metrics:**
- Analysis request count
- Average response time
- Error rate
- Active sessions

**System Metrics:**
- CPU usage
- Memory consumption
- Network I/O
- Database connections

**Business Metrics:**
- Active users
- Analyses per user
- Most analyzed markets
- Export downloads

### Tools (Production)

- **Application Monitoring:** New Relic / Datadog
- **Log Aggregation:** ELK Stack / Splunk
- **Error Tracking:** Sentry
- **Uptime Monitoring:** Pingdom

---

## Deployment Architecture

### Development
```
Local Machine
├── Python 3.10+
├── Streamlit (localhost:8501)
└── In-memory session state
```

### Staging
```
Streamlit Cloud
├── GitHub integration
├── Automatic deployments
├── HTTPS enabled
└── Custom domain (optional)
```

### Production
```
Cloud Infrastructure (AWS/GCP/Azure)
├── Load Balancer
├── Multiple App Instances
│   ├── Streamlit Frontend
│   └── FastAPI Backend
├── Redis Cache
├── PostgreSQL Database
└── Object Storage (S3)
```

---

## Future Enhancements

### Phase 2
- Real-time data streaming
- Custom market definitions
- Advanced filtering
- Scheduled reports

### Phase 3
- Multi-user collaboration
- Team workspaces
- API access for developers
- Webhook notifications

### Phase 4
- Machine learning model training
- Predictive analytics
- Custom data sources
- White-label solutions

---

## API Specification

### Endpoints (Future)

**POST /api/v1/analyze**
```json
Request:
{
  "market": "AI Startups",
  "region": "US",
  "timeframe": "last 6 months",
  "depth": "standard"
}

Response:
{
  "request_id": "abc123",
  "status": "processing",
  "estimated_time": 20
}
```

**GET /api/v1/results/{request_id}**
```json
Response:
{
  "request_id": "abc123",
  "status": "completed",
  "data": {...},
  "analysis": {...},
  "summary": "..."
}
```

**GET /api/v1/history**
```json
Response:
{
  "total": 42,
  "analyses": [...]
}
```

---

**Architecture Version:** 1.0.0  
**Last Updated:** February 6, 2024  
**Status:** Production Ready (MVP)
