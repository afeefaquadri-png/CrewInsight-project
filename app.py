import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time
import json
import hashlib
from typing import List, Dict, Any
import random


st.set_page_config(
    page_title="CrewInsight",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_css():
    st.markdown("""
    <style>

    /* ===============================
       GLOBAL DARK THEME
    =============================== */

    html, body, [class*="stApp"] {
        background-color: #020617;
        color: #e5e7eb;
        font-family: "Inter", sans-serif;
    }

    /* Remove Streamlit default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* ===============================
       SIDEBAR
    =============================== */

    section[data-testid="stSidebar"] {
        background-color: #020617;
        border-right: 1px solid #1e293b;
    }

    section[data-testid="stSidebar"] * {
        color: #e5e7eb !important;
    }

    /* ===============================
       HEADINGS & TEXT
    =============================== */

    h1, h2, h3, h4 {
        color: #f8fafc;
        font-weight: 700;
    }

    p, span, label {
        color: #cbd5f5;
    }

    /* ===============================
       INPUTS
    =============================== */

    input, textarea {
        background-color: #020617 !important;
        color: #f8fafc !important;
        border: 1px solid #1e293b !important;
        border-radius: 10px !important;
    }

    input::placeholder {
        color: #64748b;
    }

    /* ===============================
       BUTTONS
    =============================== */

    .stButton > button {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        border-radius: 12px;
        padding: 10px 18px;
        font-weight: 600;
        border: none;
        transition: all 0.2s ease-in-out;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        opacity: 0.9;
    }

    /* ===============================
       ALERTS (SUCCESS / ERROR / INFO)
    =============================== */

    .stAlert {
        background-color: #020617;
        border: 1px solid #1e293b;
        border-radius: 12px;
        color: #e5e7eb;
    }

    /* ===============================
       TABS (FIX INVISIBLE TABS)
    =============================== */

    div[data-baseweb="tab-list"] {
        background-color: #0f172a;
        padding: 8px;
        border-radius: 14px;
        gap: 8px;
    }

    button[data-baseweb="tab"] {
        background-color: #020617;
        color: #e5e7eb !important;
        border-radius: 12px;
        padding: 10px 18px;
        font-weight: 600;
        border: 1px solid #1e293b;
        transition: all 0.2s ease-in-out;
    }

    button[data-baseweb="tab"]:hover {
        background-color: #1e293b;
        color: #ffffff !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white !important;
        border: none;
    }

    /* ===============================
       DOWNLOAD BUTTON FIX
    =============================== */

    .stDownloadButton > button {
        background: linear-gradient(90deg, #22c55e, #16a34a);
        color: white;
        border-radius: 12px;
        font-weight: 600;
        padding: 10px 18px;
    }

    /* ===============================
       SCROLLBAR
    =============================== */

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #020617;
    }

    ::-webkit-scrollbar-thumb {
        background: #334155;
        border-radius: 10px;
    }

    </style>
    """, unsafe_allow_html=True)


# Initialize session state
def init_session_state():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'api_key' not in st.session_state:
        st.session_state.api_key = None
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = []
    if 'current_request_id' not in st.session_state:
        st.session_state.current_request_id = None

# Mock authentication
def authenticate(api_key: str) -> bool:
    # For demo purposes, accept any key that looks like an API key
    if len(api_key) >= 16 and api_key.startswith("sk-"):
        st.session_state.authenticated = True
        st.session_state.api_key = api_key
        return True
    return False

# Mock Data Collector Agent
class DataCollectorAgent:
    @staticmethod
    def fetch_data(market: str, region: str, timeframe: str) -> Dict[str, Any]:
        """Simulate data collection from multiple sources"""
        time.sleep(1.5)  # Simulate API call delay
        
        sources = ["TechCrunch", "Bloomberg", "Reuters"]
        data_points = []
        
        for source in sources:
            data_points.append({
                "source": source,
                "timestamp": datetime.now() - timedelta(days=random.randint(1, 180)),
                "relevance_score": round(random.uniform(0.7, 0.99), 2),
                "raw_content": f"Market data from {source} regarding {market} in {region}"
            })
        
        return {
            "market": market,
            "region": region,
            "timeframe": timeframe,
            "sources": sources,
            "data_points": data_points,
            "total_articles": random.randint(150, 500)
        }

# Mock Analysis Agent
class TrendAnalyzer:
    @staticmethod
    def analyze(data: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate trend analysis"""
        time.sleep(2)  # Simulate processing delay
        
        market = data['market']
        region = data['region']
        
        # Generate realistic trends based on market
        trend_templates = {
            "AI Startups": [
                "Rapid increase in generative AI investments",
                "Growing focus on AI ethics and regulation compliance",
                "Expansion of AI-powered automation tools",
                "Rise in AI-human collaboration platforms"
            ],
            "Fintech": [
                "Digital banking adoption acceleration",
                "Blockchain integration in payment systems",
                "Regulatory technology (RegTech) expansion",
                "Embedded finance solutions growth"
            ],
            "Healthcare Tech": [
                "Telemedicine platform proliferation",
                "AI-driven diagnostic tools advancement",
                "Wearable health tech integration",
                "Digital therapeutics market expansion"
            ],
            "E-commerce": [
                "Social commerce integration growth",
                "AR/VR shopping experience adoption",
                "Sustainable e-commerce practices",
                "Cross-border marketplace expansion"
            ]
        }
        
        # Select relevant trends
        base_trends = trend_templates.get(market, [
            f"Increased market activity in {market}",
            f"Regional expansion in {region}",
            "Innovation in product offerings",
            "Strategic partnerships and acquisitions"
        ])
        
        trends = []
        for i, trend in enumerate(base_trends[:4], 1):
            trends.append({
                "trend": trend,
                "confidence": round(random.uniform(0.75, 0.95), 2),
                "impact": random.choice(["High", "Medium", "High"]),
                "timeframe": random.choice(["Short-term", "Medium-term", "Long-term"])
            })
        
        # Generate market metrics
        metrics = {
            "growth_rate": round(random.uniform(15, 45), 1),
            "market_size": round(random.uniform(5, 50), 1),
            "funding_increase": round(random.uniform(20, 60), 1),
            "new_entrants": random.randint(50, 200)
        }
        
        return {
            "trends": trends,
            "metrics": metrics,
            "sentiment": random.choice(["Highly Positive", "Positive", "Moderately Positive"]),
            "risk_level": random.choice(["Low", "Medium", "Low"])
        }

# Mock Summarization Agent
class SummaryGenerator:
    @staticmethod
    def summarize(analysis: Dict[str, Any], market: str, region: str) -> str:
        """Generate business-friendly summary"""
        time.sleep(1)  # Simulate GPT processing
        
        trends = analysis['trends']
        metrics = analysis['metrics']
        
        summary = f"""
## Executive Summary: {market} Market Analysis ({region})

### Market Overview
The {market} sector in {region} demonstrates {analysis['sentiment'].lower()} momentum with a growth rate of {metrics['growth_rate']}% over the analyzed period. Market size has expanded to ${metrics['market_size']}B, indicating robust expansion and investor confidence.

### Key Trends Identified

"""
        for i, trend in enumerate(trends, 1):
            summary += f"{i}. **{trend['trend']}** (Confidence: {trend['confidence']*100:.0f}%)\n"
            summary += f"   - Impact Level: {trend['impact']}\n"
            summary += f"   - Expected Timeframe: {trend['timeframe']}\n\n"
        
        summary += f"""
### Investment Landscape
Funding in the {market} sector has increased by {metrics['funding_increase']}% with {metrics['new_entrants']} new market entrants, signaling strong competitive dynamics and innovation potential.

### Strategic Recommendations
1. **Market Entry Timing**: Current market conditions present {analysis['sentiment'].lower()} opportunities
2. **Risk Assessment**: {analysis['risk_level']} risk environment based on regulatory and competitive factors
3. **Focus Areas**: Prioritize trends with high confidence scores for strategic planning
4. **Competitive Positioning**: Monitor the {metrics['new_entrants']} new entrants for partnership or acquisition opportunities

### Conclusion
The {market} market in {region} shows strong fundamentals and growth trajectory. Stakeholders should consider accelerating investment and expansion strategies while maintaining awareness of emerging regulatory frameworks.

---
*Analysis generated on {datetime.now().strftime("%B %d, %Y at %H:%M")}*
        """
        
        return summary.strip()

# Agent Orchestrator
class AgentOrchestrator:
    def __init__(self):
        self.data_collector = DataCollectorAgent()
        self.analyzer = TrendAnalyzer()
        self.summarizer = SummaryGenerator()
    
    def run_pipeline(self, request: Dict[str, str]) -> Dict[str, Any]:
        """Execute the complete analysis pipeline"""
        request_id = hashlib.md5(
            f"{request['market']}{request['region']}{datetime.now()}".encode()
        ).hexdigest()[:12]
        
        # Step 1: Data Collection
        progress_text = "🔍 Collecting market data from multiple sources..."
        progress_bar = st.progress(0, text=progress_text)
        
        collected_data = self.data_collector.fetch_data(
            request['market'],
            request['region'],
            request['timeframe']
        )
        progress_bar.progress(33, text="📊 Analyzing market trends...")
        
        # Step 2: Trend Analysis
        analysis_results = self.analyzer.analyze(collected_data)
        progress_bar.progress(66, text="✍️ Generating summary report...")
        
        # Step 3: Summary Generation
        summary = self.summarizer.summarize(
            analysis_results,
            request['market'],
            request['region']
        )
        progress_bar.progress(100, text="✅ Analysis complete!")
        time.sleep(0.5)
        progress_bar.empty()
        
        return {
            "request_id": request_id,
            "timestamp": datetime.now(),
            "request": request,
            "data": collected_data,
            "analysis": analysis_results,
            "summary": summary
        }

# Visualization functions
def plot_trend_confidence(trends: List[Dict]):
    """Create confidence chart for trends"""
    df = pd.DataFrame(trends)
    
    fig = go.Figure(data=[
        go.Bar(
            x=df['confidence'],
            y=[t[:50] + "..." if len(t) > 50 else t for t in df['trend']],
            orientation='h',
            marker=dict(
                color=df['confidence'],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Confidence")
            ),
            text=[f"{c*100:.0f}%" for c in df['confidence']],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Trend Analysis Confidence Scores",
        xaxis_title="Confidence Level",
        yaxis_title="Identified Trends",
        height=400,
        template="plotly_dark",
        showlegend=False
    )
    
    return fig

def plot_market_metrics(metrics: Dict):
    """Create metrics visualization"""
    fig = go.Figure()
    
    categories = ['Growth Rate (%)', 'Market Size ($B)', 'Funding Increase (%)', 'New Entrants']
    values = [
        metrics['growth_rate'],
        metrics['market_size'],
        metrics['funding_increase'],
        metrics['new_entrants'] / 4  # Scale down for visibility
    ]
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Market Metrics',
        marker=dict(color='#667eea')
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, max(values) * 1.2])
        ),
        showlegend=False,
        title="Market Performance Metrics",
        height=400
    )
    
    return fig

def create_timeline_chart(data_points: List[Dict]):
    """Create timeline of data collection"""
    df = pd.DataFrame(data_points)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')
    
    fig = px.scatter(
        df,
        x='timestamp',
        y='source',
        size='relevance_score',
        color='source',
        title='Data Collection Timeline',
        labels={'timestamp': 'Date', 'source': 'Source'},
        height=300
    )
    
    fig.update_layout(
        showlegend=True,
        template="plotly_dark"
    )
    
    return fig

# Main application
def main():
    load_css()
    init_session_state()
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🔐 Authentication")
        
        if not st.session_state.authenticated:
            api_key_input = st.text_input(
                "API Key",
                type="password",
                placeholder="sk-your-api-key-here",
                help="Enter your CrewInsight API key"
            )
            
            if st.button("🔓 Login", use_container_width=True):
                if authenticate(api_key_input):
                    st.success("✅ Authenticated successfully!")
                    st.rerun()
                else:
                    st.error("❌ Invalid API key. Use format: sk-xxxxx...")
            
            st.markdown("---")
            st.markdown("### 📖 Demo Access")
            st.info("For demo purposes, use any API key starting with 'sk-' (minimum 16 characters)")
            
        else:
            st.success("✅ Authenticated")
            if st.button("🔒 Logout", use_container_width=True):
                st.session_state.authenticated = False
                st.session_state.api_key = None
                st.rerun()
            
            st.markdown("---")
            st.markdown("### ⚙️ Quick Settings")
            st.markdown(f"**API Key:** {st.session_state.api_key[:12]}...")
            st.markdown(f"**Analyses Run:** {len(st.session_state.analysis_results)}")
    
    # Main content
    st.markdown("# 📊 CrewInsight - Business Analyst Agent")
    st.markdown("### AI-Powered Market Intelligence & Trend Analysis")
    
    if not st.session_state.authenticated:
        st.warning("🔒 Please authenticate using the sidebar to access the application.")
        
        # Show features while not authenticated
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 🔍 Data Collection")
            st.markdown("Aggregate market data from multiple authoritative sources in real-time.")
        
        with col2:
            st.markdown("### 📈 Trend Analysis")
            st.markdown("AI-powered analysis identifies key market trends and opportunities.")
        
        with col3:
            st.markdown("### 📝 Smart Summaries")
            st.markdown("Generate actionable insights and executive-ready reports instantly.")
        
        return
    
    # Tabs for authenticated users
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 New Analysis", "📊 Results History", "⚙️ Settings", "ℹ️ About"])
    
    with tab1:
        st.markdown("## Request Market Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            market = st.selectbox(
                "🎯 Select Market Sector",
                ["AI Startups", "Fintech", "Healthcare Tech", "E-commerce", "SaaS", "Clean Energy", "EdTech"],
                help="Choose the market sector for analysis"
            )
            
            timeframe = st.selectbox(
                "📅 Analysis Timeframe",
                ["Last 3 months", "Last 6 months", "Last 12 months", "Last 2 years"],
                index=1,
                help="Select the historical period for trend analysis"
            )
        
        with col2:
            region = st.selectbox(
                "🌍 Geographic Region",
                ["US", "Europe", "Asia-Pacific", "Global", "North America", "Latin America"],
                help="Select the geographic focus area"
            )
            
            depth = st.radio(
                "🎚️ Analysis Depth",
                ["Quick Overview", "Standard Analysis", "Deep Dive"],
                index=1,
                horizontal=True
            )
        
        st.markdown("---")
        
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        
        with col_btn2:
            analyze_btn = st.button(
                "🚀 Run Analysis",
                use_container_width=True,
                type="primary"
            )
        
        if analyze_btn:
            orchestrator = AgentOrchestrator()
            
            request = {
                "market": market,
                "region": region,
                "timeframe": timeframe,
                "depth": depth
            }
            
            with st.spinner("🤖 AI agents are working on your analysis..."):
                result = orchestrator.run_pipeline(request)
                st.session_state.analysis_results.insert(0, result)
                st.session_state.current_request_id = result['request_id']
            
            st.success(f"✅ Analysis completed! Request ID: `{result['request_id']}`")
            
            # Display results
            st.markdown("---")
            st.markdown("## 📊 Analysis Results")
            
            # Metrics row
            metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
            
            with metric_col1:
                st.metric(
                    "Growth Rate",
                    f"{result['analysis']['metrics']['growth_rate']}%",
                    delta=f"+{result['analysis']['metrics']['growth_rate']/2:.1f}%"
                )
            
            with metric_col2:
                st.metric(
                    "Market Size",
                    f"${result['analysis']['metrics']['market_size']}B",
                    delta="Growing"
                )
            
            with metric_col3:
                st.metric(
                    "Funding Increase",
                    f"{result['analysis']['metrics']['funding_increase']}%",
                    delta=f"+{result['analysis']['metrics']['funding_increase']/3:.1f}%"
                )
            
            with metric_col4:
                st.metric(
                    "New Entrants",
                    result['analysis']['metrics']['new_entrants'],
                    delta="Active Market"
                )
            
            st.markdown("---")
            
            # Visualizations
            viz_col1, viz_col2 = st.columns(2)
            
            with viz_col1:
                st.plotly_chart(
                    plot_trend_confidence(result['analysis']['trends']),
                    use_container_width=True
                )
            
            with viz_col2:
                st.plotly_chart(
                    plot_market_metrics(result['analysis']['metrics']),
                    use_container_width=True
                )
            
            # Timeline
            st.plotly_chart(
                create_timeline_chart(result['data']['data_points']),
                use_container_width=True
            )
            
            # Summary
            st.markdown("---")
            st.markdown("## 📝 Executive Summary")
            st.markdown(result['summary'])
            
            # Export options
            st.markdown("---")
            export_col1, export_col2, export_col3 = st.columns(3)
            
            with export_col1:
                st.download_button(
                    "📄 Download Summary (MD)",
                    data=result['summary'],
                    file_name=f"analysis_{result['request_id']}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            
            with export_col2:
                json_data = json.dumps(result, default=str, indent=2)
                st.download_button(
                    "📦 Download Full Report (JSON)",
                    data=json_data,
                    file_name=f"analysis_{result['request_id']}.json",
                    mime="application/json",
                    use_container_width=True
                )
            
            with export_col3:
                # Create CSV of trends
                trends_df = pd.DataFrame(result['analysis']['trends'])
                csv = trends_df.to_csv(index=False)
                st.download_button(
                    "📊 Download Trends (CSV)",
                    data=csv,
                    file_name=f"trends_{result['request_id']}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
    
    with tab2:
        st.markdown("## 📚 Analysis History")
        
        if not st.session_state.analysis_results:
            st.info("No analyses yet. Run your first analysis in the 'New Analysis' tab!")
        else:
            # Summary statistics
            total_analyses = len(st.session_state.analysis_results)
            st.markdown(f"### Total Analyses: {total_analyses}")
            
            # Filter options
            filter_col1, filter_col2 = st.columns(2)
            
            with filter_col1:
                filter_market = st.multiselect(
                    "Filter by Market",
                    options=list(set([r['request']['market'] for r in st.session_state.analysis_results])),
                    default=None
                )
            
            with filter_col2:
                filter_region = st.multiselect(
                    "Filter by Region",
                    options=list(set([r['request']['region'] for r in st.session_state.analysis_results])),
                    default=None
                )
            
            st.markdown("---")
            
            # Display results
            for result in st.session_state.analysis_results:
                # Apply filters
                if filter_market and result['request']['market'] not in filter_market:
                    continue
                if filter_region and result['request']['region'] not in filter_region:
                    continue
                
                with st.expander(
                    f"📊 {result['request']['market']} - {result['request']['region']} | "
                    f"{result['timestamp'].strftime('%Y-%m-%d %H:%M')} | ID: {result['request_id']}"
                ):
                    # Request details
                    detail_col1, detail_col2, detail_col3 = st.columns(3)
                    
                    with detail_col1:
                        st.markdown(f"**Market:** {result['request']['market']}")
                        st.markdown(f"**Region:** {result['request']['region']}")
                    
                    with detail_col2:
                        st.markdown(f"**Timeframe:** {result['request']['timeframe']}")
                        st.markdown(f"**Depth:** {result['request']['depth']}")
                    
                    with detail_col3:
                        st.markdown(f"**Sentiment:** {result['analysis']['sentiment']}")
                        st.markdown(f"**Risk Level:** {result['analysis']['risk_level']}")
                    
                    # Key metrics
                    st.markdown("#### Key Metrics")
                    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                    
                    with m_col1:
                        st.metric("Growth", f"{result['analysis']['metrics']['growth_rate']}%")
                    with m_col2:
                        st.metric("Market Size", f"${result['analysis']['metrics']['market_size']}B")
                    with m_col3:
                        st.metric("Funding ↑", f"{result['analysis']['metrics']['funding_increase']}%")
                    with m_col4:
                        st.metric("New Entrants", result['analysis']['metrics']['new_entrants'])
                    
                    # Trends
                    st.markdown("#### Identified Trends")
                    trends_df = pd.DataFrame(result['analysis']['trends'])
                    st.dataframe(trends_df, use_container_width=True, hide_index=True)
                    
                    # Download
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            "📄 Download Summary",
                            data=result['summary'],
                            file_name=f"analysis_{result['request_id']}.md",
                            key=f"dl_md_{result['request_id']}"
                        )
                    with col2:
                        json_data = json.dumps(result, default=str, indent=2)
                        st.download_button(
                            "📦 Download JSON",
                            data=json_data,
                            file_name=f"analysis_{result['request_id']}.json",
                            key=f"dl_json_{result['request_id']}"
                        )
    
    with tab3:
        st.markdown("## ⚙️ Application Settings")
        
        st.markdown("### 🔐 Authentication")
        st.text_input("Current API Key", value=st.session_state.api_key, type="password", disabled=True)
        
        if st.button("🔄 Regenerate API Key"):
            st.info("In production, this would regenerate your API key. Contact support for key management.")
        
        st.markdown("---")
        
        st.markdown("### 📊 Analysis Preferences")
        
        default_market = st.selectbox(
            "Default Market Sector",
            ["AI Startups", "Fintech", "Healthcare Tech", "E-commerce", "SaaS"],
            help="Set your preferred default market"
        )
        
        default_region = st.selectbox(
            "Default Region",
            ["US", "Europe", "Asia-Pacific", "Global"],
            help="Set your preferred default region"
        )
        
        auto_export = st.checkbox(
            "Auto-export results",
            help="Automatically download analysis results after completion"
        )
        
        st.markdown("---")
        
        st.markdown("### 🎨 Display Options")
        
        show_confidence = st.checkbox("Show confidence scores", value=True)
        show_timeline = st.checkbox("Show data collection timeline", value=True)
        show_metrics = st.checkbox("Show market metrics", value=True)
        
        st.markdown("---")
        
        st.markdown("### 💾 Data Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🗑️ Clear Analysis History", use_container_width=True):
                st.session_state.analysis_results = []
                st.success("History cleared successfully!")
        
        with col2:
            if st.session_state.analysis_results:
                all_results = json.dumps(st.session_state.analysis_results, default=str, indent=2)
                st.download_button(
                    "📦 Export All Analyses",
                    data=all_results,
                    file_name=f"all_analyses_{datetime.now().strftime('%Y%m%d')}.json",
                    mime="application/json",
                    use_container_width=True
                )
    
    with tab4:
        st.markdown("## ℹ️ About CrewInsight")
        
        st.markdown("""
        ### 🎯 Mission
        CrewInsight empowers startups and entrepreneurs with AI-driven market intelligence,
        delivering actionable insights to support informed business decision-making.
        
        ### 🤖 Technology Stack
        """)
        
        tech_col1, tech_col2 = st.columns(2)
        
        with tech_col1:
            st.markdown("""
            **Core Technologies:**
            - 🐍 Python 3.10+
            - ⚡ FastAPI
            - 🤖 CrewAI (Agent Orchestration)
            - 🧠 OpenAI API (NLP)
            """)
        
        with tech_col2:
            st.markdown("""
            **Infrastructure:**
            - 🎨 Streamlit (UI)
            - 📊 Plotly (Visualizations)
            - 🔐 API Key Authentication
            - ☁️ Cloud-Ready Architecture
            """)
        
        st.markdown("---")
        
        st.markdown("### 🔄 Agent Workflow")
        
        st.markdown("""
        1. **Data Collection Agent** 🔍
           - Aggregates data from TechCrunch, Bloomberg, Reuters, and more
           - Filters and preprocesses raw market information
        
        2. **Trend Analysis Agent** 📈
           - Applies machine learning to identify patterns
           - Calculates confidence scores and impact assessments
        
        3. **Summarization Agent** ✍️
           - Generates executive-ready summaries
           - Provides strategic recommendations
        """)
        
        st.markdown("---")
        
        st.markdown("### 📚 API Documentation")
        
        with st.expander("📡 POST /analyze"):
            st.code("""
Request:
{
  "market": "AI Startups",
  "region": "US",
  "timeframe": "last 6 months"
}

Response:
{
  "request_id": "abc123",
  "summary": "AI startups in the US have seen...",
  "trends": [...]
}
            """, language="json")
        
        with st.expander("📊 GET /results/{request_id}"):
            st.code("""
Response:
{
  "request_id": "abc123",
  "status": "completed",
  "timestamp": "2024-02-06T10:30:00Z",
  "results": {...}
}
            """, language="json")
        
        st.markdown("---")
        
        st.markdown("### 📞 Support & Feedback")
        
        feedback_col1, feedback_col2 = st.columns(2)
        
        with feedback_col1:
            st.markdown("""
            **Contact Information:**
            - 📧 Email: support@crewinsight.ai
            - 💬 Slack: #crewinsight-support
            - 📚 Docs: docs.crewinsight.ai
            """)
        
        with feedback_col2:
            st.markdown("""
            **Resources:**
            - [API Documentation](https://docs.crewinsight.ai)
            - [GitHub Repository](https://github.com/crewinsight)
            - [Community Forum](https://community.crewinsight.ai)
            """)
        
        st.markdown("---")
        
        st.markdown("""
        <div style='text-align: center; padding: 2rem; color: #667eea;'>
            <h4>CrewInsight v1.0.0</h4>
            <p>Built with ❤️ for entrepreneurs and innovators</p>
            <p>© 2024 CrewInsight. All rights reserved.</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
