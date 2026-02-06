# 🚀 Quick Deployment Guide

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Access at http://localhost:8501
```

## Streamlit Community Cloud (Recommended - FREE)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/crewinsight.git
   git push -u origin main
   ```

2. **Deploy:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Select `app.py` as the main file
   - Click "Deploy"

3. **Done!** Your app will be live at:
   `https://YOUR_USERNAME-crewinsight.streamlit.app`

## Docker Deployment

```bash
# Build
docker build -t crewinsight .

# Run
docker run -p 8501:8501 crewinsight

# Access at http://localhost:8501
```

## Heroku Deployment

```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Deploy
git push heroku main

# Open app
heroku open
```

## AWS EC2 / DigitalOcean

```bash
# SSH into server
ssh user@your-server-ip

# Install Python
sudo apt update
sudo apt install python3.10 python3-pip git

# Clone repository
git clone https://github.com/YOUR_USERNAME/crewinsight.git
cd crewinsight

# Install dependencies
pip install -r requirements.txt

# Run with nohup
nohup streamlit run app.py --server.port=8501 --server.address=0.0.0.0 &

# Or use screen for better management
screen -S crewinsight
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
# Press Ctrl+A, then D to detach
```

## Environment Variables (Optional)

Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_key_here
CREWAI_API_KEY=your_crewai_key_here
```

## Troubleshooting

**Port already in use:**
```bash
# Find process
lsof -i :8501

# Kill process
kill -9 PID

# Or use different port
streamlit run app.py --server.port=8502
```

**Module not found:**
```bash
pip install -r requirements.txt --upgrade
```

**Permission denied on deployment:**
```bash
chmod +x setup.sh
```

## Production Checklist

- [ ] Test all tabs and features
- [ ] Verify authentication works
- [ ] Test export functionality
- [ ] Check mobile responsiveness
- [ ] Review error handling
- [ ] Set up monitoring (optional)
- [ ] Configure SSL/HTTPS (for production)
- [ ] Set up backups (if using database)

## Access the Demo

1. Open the application
2. Use demo API key: `sk-demo1234567890123456`
3. Go to "New Analysis" tab
4. Select market parameters
5. Click "Run Analysis"
6. Explore visualizations and export features

Enjoy your CrewInsight deployment! 🎉
