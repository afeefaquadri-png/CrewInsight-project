# 📖 CrewInsight User Guide

Welcome to CrewInsight - your AI-powered business analyst agent! This guide will help you get the most out of the platform.

## 🎯 Table of Contents

1. [Getting Started](#getting-started)
2. [Authentication](#authentication)
3. [Running Your First Analysis](#running-your-first-analysis)
4. [Understanding Results](#understanding-results)
5. [Managing History](#managing-history)
6. [Settings & Customization](#settings--customization)
7. [Exporting Data](#exporting-data)
8. [Tips & Best Practices](#tips--best-practices)
9. [FAQ](#faq)

---

## 🚀 Getting Started

### First Time Setup

1. **Launch the Application**
   - Local: Open browser to `http://localhost:8501`
   - Deployed: Visit your deployment URL

2. **Check the Sidebar**
   - You'll see the authentication panel
   - Demo credentials are provided

3. **Explore the Interface**
   - Four main tabs: New Analysis, Results History, Settings, About
   - Professional gradient design
   - Mobile-responsive layout

---

## 🔐 Authentication

### Demo Access (Development)

For testing and demonstration:

1. Click on the API Key field in the sidebar
2. Enter any key starting with `sk-` (minimum 16 characters)
   - Example: `sk-demo1234567890`
   - Example: `sk-test9876543210abc`
3. Click "🔓 Login"
4. You're in! ✅

### Production Access

In production environments:
- Use your actual CrewInsight API key
- Keys are validated against the backend
- Contact support@crewinsight.ai for API keys

### Logout

- Click "🔒 Logout" button in sidebar
- Your session data remains until browser refresh
- API key is cleared from session

---

## 📊 Running Your First Analysis

### Step-by-Step Guide

1. **Navigate to "🔍 New Analysis" Tab**

2. **Select Market Sector**
   - Choose from 7 options:
     - AI Startups
     - Fintech
     - Healthcare Tech
     - E-commerce
     - SaaS
     - Clean Energy
     - EdTech

3. **Choose Geographic Region**
   - US: United States market
   - Europe: European market
   - Asia-Pacific: APAC region
   - Global: Worldwide analysis
   - North America: USA + Canada
   - Latin America: Central & South America

4. **Set Timeframe**
   - Last 3 months: Recent trends
   - Last 6 months: Medium-term patterns (recommended)
   - Last 12 months: Annual overview
   - Last 2 years: Long-term trends

5. **Select Analysis Depth**
   - Quick Overview: Fast insights (lighter data)
   - Standard Analysis: Balanced approach (recommended)
   - Deep Dive: Comprehensive analysis (more detailed)

6. **Click "🚀 Run Analysis"**

7. **Wait for Results**
   - Progress bar shows each stage:
     - 🔍 Collecting data (5 seconds)
     - 📊 Analyzing trends (7 seconds)
     - ✍️ Generating summary (3 seconds)
   - Total time: ~15-20 seconds

---

## 📈 Understanding Results

### Metrics Dashboard

Four key metrics are displayed:

1. **Growth Rate**
   - Percentage growth in market sector
   - Green arrow shows positive momentum
   - Based on funding, revenue, and market cap data

2. **Market Size**
   - Current market valuation in billions
   - "Growing" indicator shows expansion trend
   - Reflects total addressable market

3. **Funding Increase**
   - Investment growth percentage
   - Indicates investor confidence
   - Year-over-year comparison

4. **New Entrants**
   - Number of new companies in sector
   - "Active Market" shows competitive dynamics
   - Higher numbers indicate opportunity

### Trend Analysis Chart

**Horizontal Bar Chart:**
- Each bar represents an identified trend
- Length indicates confidence score (0-100%)
- Color gradient shows strength
- Longer bars = higher confidence

**How to Read:**
- 90%+ confidence: Very reliable trend
- 75-90% confidence: Strong trend
- Below 75%: Emerging pattern

### Market Metrics Radar

**Polar Chart showing:**
- Growth Rate
- Market Size
- Funding Increase
- New Entrants (scaled)

**Interpretation:**
- Larger coverage = stronger market
- Balanced shape = healthy ecosystem
- Spikes indicate exceptional performance in specific areas

### Data Collection Timeline

**Scatter Plot showing:**
- X-axis: Date of data collection
- Y-axis: Source (TechCrunch, Bloomberg, Reuters)
- Bubble size: Relevance score

**Purpose:**
- Verify data freshness
- Check source diversity
- Assess data quality

### Executive Summary

**Structured Report containing:**

1. **Market Overview**
   - High-level market assessment
   - Key growth indicators
   - Market size and trajectory

2. **Key Trends** (numbered list)
   - Trend description
   - Confidence percentage
   - Impact level (High/Medium/Low)
   - Expected timeframe

3. **Investment Landscape**
   - Funding trends
   - New market entrants
   - Competitive dynamics

4. **Strategic Recommendations**
   - Actionable insights
   - Risk assessment
   - Focus areas
   - Opportunities

5. **Conclusion**
   - Summary of findings
   - Strategic direction
   - Next steps

---

## 📚 Managing History

### Viewing Past Analyses

1. **Go to "📊 Results History" Tab**

2. **See All Analyses**
   - Sorted by most recent first
   - Shows total count at top
   - Each entry displays: Market, Region, Date, Request ID

3. **Filter Results**
   - Filter by Market: Select one or more sectors
   - Filter by Region: Select one or more regions
   - Filters apply in real-time

4. **Expand an Analysis**
   - Click on any analysis card
   - View full details:
     - Request parameters
     - Key metrics
     - Trends table
     - Download options

### Comparing Analyses

To compare multiple analyses:

1. Filter by same market, different regions
2. Or filter by same region, different timeframes
3. Look for patterns in:
   - Growth rates
   - Trend evolution
   - Market sentiment

---

## ⚙️ Settings & Customization

### Authentication Settings

- **View Current API Key**: Masked for security
- **Regenerate Key**: Contact support (production feature)

### Analysis Preferences

- **Default Market Sector**: Auto-selects on new analysis
- **Default Region**: Pre-fills your preferred region
- **Auto-export Results**: Downloads after each analysis

### Display Options

- **Show Confidence Scores**: Toggle confidence visualization
- **Show Timeline**: Toggle data collection timeline
- **Show Metrics**: Toggle market metrics radar

### Data Management

- **Clear History**: Remove all stored analyses
- **Export All**: Download complete history as JSON

---

## 💾 Exporting Data

### Export Formats

1. **Markdown (.md)**
   - Executive summary in Markdown format
   - Perfect for reports, wikis, GitHub
   - Includes all narrative content
   - Copy-paste friendly

2. **JSON (.json)**
   - Complete analysis data structure
   - Includes all raw data and metrics
   - For developers and data pipelines
   - Machine-readable format

3. **CSV (.csv)**
   - Trends table only
   - Open in Excel, Google Sheets
   - For further analysis
   - Includes trend, confidence, impact, timeframe

### How to Export

**From New Analysis Tab:**
1. Complete an analysis
2. Scroll to bottom
3. Click desired export button
4. File downloads automatically

**From Results History:**
1. Expand any previous analysis
2. Click "Download Summary" or "Download JSON"
3. File downloads with Request ID in filename

---

## 💡 Tips & Best Practices

### Getting Better Results

1. **Choose Appropriate Timeframe**
   - Fast-moving sectors (AI, Crypto): 3-6 months
   - Stable sectors (Healthcare, Energy): 12-24 months

2. **Match Depth to Need**
   - Quick decisions: Quick Overview
   - Strategic planning: Standard Analysis
   - Investment decisions: Deep Dive

3. **Use Multiple Regions**
   - Compare US vs Europe for global perspective
   - Asia-Pacific for emerging market trends
   - Global for overall market direction

### Interpreting Results

1. **Focus on High-Confidence Trends**
   - Prioritize trends with 85%+ confidence
   - Use lower confidence for exploration

2. **Consider Multiple Metrics**
   - Don't rely on single metric
   - Look for consistent patterns
   - Cross-reference trends with metrics

3. **Track Over Time**
   - Run monthly analyses
   - Compare quarter-over-quarter
   - Identify emerging vs fading trends

### Workflow Recommendations

**For Founders:**
1. Weekly: Quick Overview of your sector
2. Monthly: Standard Analysis of competition
3. Quarterly: Deep Dive for strategic planning

**For Analysts:**
1. Daily: Monitor multiple sectors
2. Weekly: Export and compile reports
3. Monthly: Comparative analysis across regions

**For Investors:**
1. Before meetings: Quick sector overview
2. Due diligence: Deep Dive analysis
3. Portfolio review: Multiple sector comparison

---

## ❓ FAQ

### General Questions

**Q: How accurate is the analysis?**
A: Analysis aggregates data from TechCrunch, Bloomberg, and Reuters. Confidence scores indicate reliability. 85%+ confidence indicates high accuracy.

**Q: How often is data updated?**
A: Data sources are queried in real-time for each analysis request.

**Q: Can I analyze custom sectors?**
A: Currently limited to preset sectors. Custom sectors available in Enterprise plan.

**Q: How many analyses can I run?**
A: Demo: Unlimited. Production: Based on your plan tier.

### Technical Questions

**Q: What if analysis fails?**
A: Retry the analysis. If problem persists, check Settings > Data Management and clear cache.

**Q: Can I share analyses?**
A: Yes! Export to Markdown and share via email/Slack. JSON format for API integration.

**Q: Where is my data stored?**
A: Current session only (in-memory). Analyses persist until browser refresh. Enterprise plans include database storage.

**Q: Is my data secure?**
A: Yes. API key authentication required. Data not persisted on server. HTTPS encryption on all requests.

### Feature Questions

**Q: Can I schedule automatic analyses?**
A: Not in MVP. Enterprise plans include scheduled reports and email delivery.

**Q: Can I compare two analyses side-by-side?**
A: Use Results History tab with filters. Visual comparison coming in v2.0.

**Q: Can I export to PowerPoint?**
A: Not directly. Use Markdown export and convert, or copy charts as images.

**Q: Can I customize trends detected?**
A: AI automatically detects trends. Keyword filtering available in Enterprise plans.

### Troubleshooting

**Q: Authentication not working?**
A: Ensure API key starts with `sk-` and is 16+ characters. For demo, any format works.

**Q: Charts not displaying?**
A: Ensure JavaScript is enabled. Try refreshing the page. Check browser console for errors.

**Q: Export buttons not working?**
A: Check browser popup blocker. Ensure downloads are enabled for the site.

**Q: App is slow?**
A: Each analysis takes 15-20 seconds. Clear history if you have 50+ analyses stored.

---

## 📞 Getting Help

### Support Channels

- **Email**: support@crewinsight.ai
- **Documentation**: docs.crewinsight.ai
- **Community**: community.crewinsight.ai
- **GitHub Issues**: github.com/crewinsight/issues

### Report a Bug

Include:
1. Browser and version
2. Steps to reproduce
3. Expected vs actual behavior
4. Screenshots if applicable
5. Request ID if analysis-related

### Feature Requests

Submit via:
- Community forum (preferred)
- Email to features@crewinsight.ai
- GitHub discussions

---

## 🎓 Learning Resources

- **Video Tutorials**: youtube.com/crewinsight
- **Blog**: blog.crewinsight.ai
- **API Docs**: api.crewinsight.ai
- **Changelog**: changes.crewinsight.ai

---

**Happy Analyzing! 🚀**

*Version 1.0.0 | Last Updated: February 2024*
