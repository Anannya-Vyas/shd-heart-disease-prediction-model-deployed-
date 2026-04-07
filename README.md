# 🚀 SHD Heart Disease Prediction

<div align="center">

**An AI-powered web application for predicting heart disease risk based on user-provided health parameters.**

**Created by [Anannya Vyas](https://github.com/Anannya-Vyas) in 2026**

[GitHub](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-) • [Issues](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-/issues)

</div>

## 📖 Overview

This project presents a web-based tool designed to help individuals assess their potential risk of heart disease. Leveraging machine learning models, the application processes a set of health-related inputs from the user and provides a predictive outcome, serving as a preliminary screening tool. The project is structured into two main components: a user-friendly frontend (`shd-hf`) for data input and display, and a powerful AI backend (`shd-screening-ai`) responsible for the actual prediction logic.

The goal is to provide an accessible and informative resource for early awareness, encouraging users to consult healthcare professionals based on their risk assessment.

## ✨ Features

-   🎯 **Interactive Health Parameter Input**: User-friendly web interface to input various health metrics (e.g., age, cholesterol, blood pressure).
-   🧠 **AI-Powered Risk Prediction**: Utilizes a trained machine learning model to predict the likelihood of heart disease.
-   📊 **Clear Prediction Outcome**: Presents the prediction result in an understandable format.
-   🏗️ **Modular Architecture**: Separates the user interface from the prediction service for better maintainability and scalability.
-   🌐 **Web-Based Accessibility**: Easily accessible through a web browser, making it convenient for users.

## 🖥️ Screenshots

<!-- TODO: Add actual screenshots of the web application, showing input forms and prediction results. -->
<!-- ![Screenshot 1](path-to-screenshot-1.png) -->
<!-- ![Screenshot 2](path-to-screenshot-2.png) -->

## 🛠️ Tech Stack

### Frontend (shd-hf)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
<!-- Potentially add:
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
-->

### Backend & Machine Learning (shd-screening-ai)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask (Hypothetical)](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/) <!-- Assuming Flask or FastAPI for API -->
[![Scikit-learn (Hypothetical)](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/) <!-- Assuming scikit-learn for ML model -->
[![Pandas (Hypothetical)](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy (Hypothetical)](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

### AI Integration (shd-hf)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-000000?style=for-the-badge&logo=openai&logoColor=white)](https://openrouter.ai/)

## 🔌 API Overview

This application leverages **OpenRouter** to provide AI-powered health analysis. OpenRouter is a unified API platform that gives access to hundreds of AI models through a single endpoint, automatically handling fallbacks and cost optimization.

### OpenRouter Integration

The `shd-hf` backend uses the **OpenRouter API** to analyze user health data and provide personalized insights:

-   **Endpoint**: `https://openrouter.ai/api/v1/chat/completions`
-   **Model**: `meta-llama/llama-3.3-70b-instruct:free` (Free tier)
-   **Purpose**: Process health parameters and generate AI-driven risk assessments

### Key Features of OpenRouter

✅ **Unified API**: Access hundreds of models through a single endpoint  
✅ **Automatic Fallbacks**: Model fallback support for reliability  
✅ **Cost Optimization**: Automatically selects cost-effective options  
✅ **Free Models**: Access to free-tier models like Llama 3.3  
✅ **Simple Integration**: Works with standard HTTP requests or SDKs  

### API Request Example

The application sends health analysis prompts to OpenRouter:

```python
import httpx

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "https://your-app.com",  # Optional but recommended
    "Content-Type": "application/json"
}

payload = {
    "model": "meta-llama/llama-3.3-70b-instruct:free",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful Heart Health AI Assistant..."
        },
        {
            "role": "user",
            "content": "Analyze my health metrics..."
        }
    ],
    "temperature": 0.4
}

response = await client.post(url, json=payload, headers=headers)
```

### Setting Up OpenRouter API Key

1. **Create an OpenRouter Account**
   - Visit [openrouter.ai](https://openrouter.ai) and sign up
   - Navigate to your dashboard to get your API key

2. **Configure the API Key**
   - Set the environment variable `OPENROUTER_API_KEY` in your system or `.env` file:
   ```bash
   export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
   ```
   - On Windows PowerShell:
   ```powershell
   $env:OPENROUTER_API_KEY = "sk-or-v1-your-key-here"
   ```

3. **Verify Configuration**
   - The application will automatically detect and use the API key
   - If not found, you can hardcode it in `shd-hf/app.py` (not recommended for production)

### Available Models

OpenRouter provides access to:
- **Free Models**: Llama 3.3 70B, Mistral, and others
- **Premium Models**: GPT-4, Claude 3, and more
- **Custom Models**: Fine-tuned versions for specific domains

For a full list of available models, visit: https://openrouter.ai/models

### Rate Limits and Quotas

- **Free Tier**: Limited requests per day
- **Paid Tier**: Higher rate limits based on subscription
- Check your OpenRouter dashboard for current usage and limits

## 🚀 Quick Start

This project consists of two main parts: the frontend web application (`shd-hf`) and the backend AI prediction service (`shd-screening-ai`). Both need to be set up to run the full application.

### Prerequisites

-   **Python 3.8+**: Required for the FastAPI backend.
-   **OpenRouter API Key**: Required for AI-powered health analysis. Get one free at [openrouter.ai](https://openrouter.ai)
-   **Web Browser**: To access the web interface.
-   **pip**: Python package manager (comes with Python).

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Anannya-Vyas/shd-heart-disease-prediction-.git
    cd shd-heart-disease-prediction-
    ```

2.  **Setup the Frontend Application (`shd-hf`)**
    ```bash
    cd shd-hf
    
    # Create a virtual environment (recommended)
    python -m venv venv
    source venv/bin/activate # On Windows: .\venv\Scripts\activate

    # Install Python dependencies
    pip install -r requirements.txt
    ```

3. **Configure OpenRouter API Key**
    ```bash
    # Set environment variable
    # On Linux/macOS:
    export OPENROUTER_API_KEY="your-api-key-here"
    
    # On Windows PowerShell:
    # $env:OPENROUTER_API_KEY = "your-api-key-here"
    ```
    Get your free API key from [openrouter.ai](https://openrouter.ai)

### Start Development Servers

1.  **Start the Frontend Application with FastAPI (`shd-hf`)**
    ```bash
    cd shd-hf
    
    # Activate virtual environment if not already active
    source venv/bin/activate # On Windows: .\venv\Scripts\activate
    
    # Start the FastAPI server with uvicorn
    python -m uvicorn app:app --reload
    ```
    *This will start the server on `http://localhost:8000` by default.*

2.  **Open your browser**
    Visit `http://localhost:8000` to access the heart health analysis application.
    
    The application will be ready to accept health data and provide AI-powered risk assessments.

## 📁 Project Structure

```
shd-heart-disease-prediction-/
├── .gitignore              # Standard Git ignore file
└── shd-hf/                 # FastAPI Frontend & Backend Application
    ├── app.py              # FastAPI main application (handles /api/analyze endpoint)
    ├── requirements.txt    # Python dependencies (fastapi, uvicorn, httpx, python-multipart)
    ├── Dockerfile          # Docker configuration for containerization
    ├── README.md           # Service-specific documentation
    └── static/             # Static files served by FastAPI
        └── index.html      # Main web application interface
```

*Note: The `shd-screening-ai` directory mentioned in the original structure is separate and contains legacy prediction models. The current application uses `shd-hf` as an integrated FastAPI service with OpenRouter AI integration.*

## ⚙️ Configuration

### Environment Variables (for `shd-hf`)

| Variable              | Description                                       | Example                   | Required |
| :-------------------- | :------------------------------------------------ | :------------------------ | :------- |
| `OPENROUTER_API_KEY`  | Your OpenRouter API key for AI analysis.          | `sk-or-v1-...`            | Yes      |

*Set environment variables before starting the application:*

```bash
# Linux/macOS
export OPENROUTER_API_KEY="your-key-here"

# Windows PowerShell
$env:OPENROUTER_API_KEY = "your-key-here"
```

### Legacy Environment Variables (for `shd-screening-ai`, if used)

| Variable      | Description                                       | Default                   | Required |
| :------------ | :------------------------------------------------ | :------------------------ | :------- |
| `MODEL_PATH`  | Path to the trained machine learning model file.  | `./models/model.pkl`      | Yes      |
| `PORT`        | Port on which the backend API will run.           | `5000`                    | No       |
| `DEBUG_MODE`  | Set to `True` for development debugging.          | `False`                   | No       |

*These variables should be set in a `.env` file within the `shd-screening-ai` directory.*

### Configuration Files

-   `shd-hf/requirements.txt`: Lists all Python package dependencies for the FastAPI application.
-   `shd-hf/app.py`: Contains the FastAPI application configuration and API endpoint definitions.
-   `shd-hf/static/index.html`: The main web interface with health parameter input forms.

### Environment Configuration

Create a `.env` file in the `shd-hf` directory (optional, for convenience):

```env
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

Or set the environment variable directly in your shell/terminal before running the application.

## 🔧 Development

### Available Commands

| Command                           | Description                                     |
| :-------------------------------- | :---------------------------------------------- |
| `python -m uvicorn app:app --reload` (in `shd-hf`) | Starts the FastAPI development server with auto-reload |
| `python -m uvicorn app:app` (in `shd-hf`)     | Starts the FastAPI production server        |

### Development Workflow

1.  **Set up the environment**
    ```bash
    cd shd-hf
    python -m venv venv
    source venv/bin/activate  # or .\venv\Scripts\activate on Windows
    pip install -r requirements.txt
    ```

2.  **Configure API key**
    ```bash
    export OPENROUTER_API_KEY="your-key-here"
    ```

3.  **Start development server**
    ```bash
    python -m uvicorn app:app --reload
    ```
    The `--reload` flag enables auto-restart on code changes.

4.  **Make changes** to `app.py` (backend) or `static/index.html` (frontend).

5.  **Test in browser** at `http://localhost:8000`

## 🧪 Testing

### Manual Testing

1. **Start the development server**
   ```bash
   python -m uvicorn app:app --reload
   ```

2. **Test the `/api/analyze` endpoint**
   ```bash
   curl -X POST http://localhost:8000/api/analyze \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Analyze my health: 45 years old, cholesterol 200, blood pressure 120/80"}'
   ```

3. **Open the web interface**
   Navigate to `http://localhost:8000` in your browser

### Automated Testing (Optional)

To add automated tests, install pytest and create tests:

```bash
pip install pytest pytest-httpx
```

Then create `shd-hf/tests/test_api.py`:

```python
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_analyze_endpoint():
    response = client.post("/api/analyze", json={"prompt": "Test prompt"})
    assert response.status_code == 200
    assert "result" in response.json()
```

Run tests:
```bash
pytest shd-hf/tests/
```

## 🚀 Deployment

The application can be deployed to various platforms that support Python/FastAPI:

### Production Build (Local VPS/Server)

**FastAPI with Uvicorn** (Production-ready):

```bash
cd shd-hf
pip install -r requirements.txt
python -m uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker Deployment

A `Dockerfile` is included for containerized deployment:

```bash
# Build the Docker image
docker build -t shd-heart-disease-app shd-hf/

# Run the container
docker run -e NVIDIA_API_KEY="your-key" -p 8000:8000 shd-heart-disease-app
```

---

## 🌐 Deployment Options & Guides

### 1. **Railway.app** (Recommended - Easiest) ⭐

Railway is simple, fast, and perfect for FastAPI apps.

**Steps:**
1. Sign up at [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub"
3. Select your GitHub repository
4. Set environment variable: `NVIDIA_API_KEY=your-key`
5. Deploy! (It's live in ~2 minutes)

**Cost:** Pay-as-you-go (~$5-20/month)  
**Setup time:** 5 minutes

---

### 2. **Hugging Face Spaces** (Free) 🎉

Perfect for ML/AI applications. Already configured for this app!

**Steps:**
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Choose "FastAPI" as the SDK
4. Upload your `shd-hf` folder
5. Add secret: `NVIDIA_API_KEY=your-key` in settings
6. Push to deploy!

**Cost:** FREE!  
**Setup time:** 10 minutes

---

### 3. **AWS (Elastic Beanstalk)** (Scalable) 📈

For high-traffic production apps.

**Steps:**
```bash
# Install AWS CLI
pip install awsebcli

# Initialize
eb init -p python-3.11 shd-heart-disease-app

# Create environment
eb create shd-prod

# Set environment variables
eb setenv NVIDIA_API_KEY=your-key

# Deploy
eb deploy
```

**Cost:** ~$10-50/month  
**Setup time:** 20 minutes

---

### 4. **Google Cloud Run** (Serverless) ☁️

Pay only for execution time - excellent for variable traffic.

**Steps:**
```bash
# Install Google Cloud SDK
# gcloud init

# Build and push Docker image
gcloud builds submit --tag gcr.io/PROJECT_ID/shd-heart-disease-app

# Deploy to Cloud Run
gcloud run deploy shd-heart-disease-app \
  --image gcr.io/PROJECT_ID/shd-heart-disease-app \
  --platform managed \
  --region us-central1 \
  --set-env-vars NVIDIA_API_KEY=your-key
```

**Cost:** ~$0-15/month (pay per request)  
**Setup time:** 25 minutes

---

### 5. **Azure App Service** (Enterprise) 🏢

For organizations using Azure ecosystem.

**Steps:**
```bash
# Install Azure CLI
# az login

# Create resource group
az group create --name shd-rg --location eastus

# Create App Service plan
az appservice plan create --name shd-plan --resource-group shd-rg --sku B2

# Create web app
az webapp create --resource-group shd-rg --plan shd-plan --name shd-app-name

# Set environment variables
az webapp config appsettings set --resource-group shd-rg --name shd-app-name \
  --settings NVIDIA_API_KEY=your-key

# Deploy from GitHub
az webapp up --location eastus --name shd-app-name
```

**Cost:** ~$15-100/month  
**Setup time:** 30 minutes

---

### 6. **DigitalOcean App Platform** (Simple & Affordable) 💙

Straightforward git-based deployment.

**Steps:**
1. Sign up at [digitalocean.com](https://digitalocean.com)
2. Click "Create" → "App Platform"
3. Connect your GitHub repository
4. Set build command: `pip install -r shd-hf/requirements.txt`
5. Set run command: `cd shd-hf && uvicorn app:app --host 0.0.0.0 --port 8080`
6. Add environment variable: `NVIDIA_API_KEY=your-key`
7. Deploy!

**Cost:** $12-25/month  
**Setup time:** 15 minutes

---

### 7. **PythonAnywhere** (Easiest for Beginners) 🐍

No command line knowledge needed - web-based setup.

**Steps:**
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your code via web interface
3. Create a new web app (choose FastAPI)
4. Configure WSGI file
5. Add environment variables in settings
6. Hit green "Reload" button

**Cost:** Free (limited) or ~$7-25/month  
**Setup time:** 20 minutes

---

### 8. **Replit** (Development & Demos) 🚀

Great for demos and collaborative development.

**Steps:**
1. Go to [replit.com](https://replit.com)
2. Click "Import from GitHub"
3. Paste your repository URL
4. Create `.env` file with `NVIDIA_API_KEY=your-key`
5. Click "Run"

**Cost:** Free (with limitations) or $7/month Pro  
**Setup time:** 5 minutes

---

### 9. **Oracle Cloud (Always Free)** 💰

Free tier with generous limits.

**Cost:** FREE for first year  
**Setup time:** 30 minutes

---

### 10. **Linode/Akamai** (VPS) 🖥️

Traditional VPS with full control.

**Cost:** $6-30/month  
**Setup time:** 45 minutes

---

## 📊 Quick Comparison

| Platform | Cost | Setup | Best For |
|----------|------|-------|----------|
| Railway | $5-20/mo | ⭐⭐ | Beginners |
| Hugging Face | FREE | ⭐⭐ | ML/AI demos |
| AWS EB | $10-50/mo | ⭐⭐⭐ | Enterprise |
| Google Cloud Run | $0-15/mo | ⭐⭐⭐ | Variable traffic |
| DigitalOcean | $12-25/mo | ⭐⭐ | Startups |
| PythonAnywhere | $7-25/mo | ⭐ | Beginners |
| Replit | FREE/$7 | ⭐ | Dev/Demos |

---

## 🔧 Environment Variables for Production

```
NVIDIA_API_KEY=nvapi-your-actual-key-here
```

---

## 🔒 Security Best Practices

1. **Never commit API keys** - Use environment variables only
2. **Use HTTPS** - All platforms provide free SSL
3. **Enable CORS carefully** in `app.py`:
   ```python
   from fastapi.middleware.cors import CORSMiddleware
   
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["https://yourdomain.com"],
       allow_credentials=True,
       allow_methods=["POST", "GET"],
       allow_headers=["Content-Type"],
   )
   ```
4. **Rate limiting** - Consider adding rate limits
5. **Keep dependencies updated** - Run `pip list --outdated`

## 📚 API Reference

### Current API (`shd-hf`)

The `shd-hf` FastAPI application provides endpoints for AI-powered health analysis.

#### `POST /api/analyze`

Analyzes health data and provides AI-generated insights using OpenRouter.

**Request Body (JSON):**

```json
{
    "prompt": "Analyze my health: I'm 45 years old, have a cholesterol level of 200, blood pressure is 120/80, and I exercise 3 times a week."
}
```

**Response Body (JSON):**

```json
{
    "result": "Based on your health metrics, your heart disease risk appears to be low to moderate. Your cholesterol and blood pressure are within acceptable ranges. Continue regular exercise and maintain a healthy diet. Consult with a healthcare professional for personalized advice."
}
```

**Error Response:**

```json
{
    "error": "API key not configured."
}
```

### Health Data Parameters (Recommended for Prompt)

When sending health data to the `/api/analyze` endpoint, include information about:

- **Age**: Current age in years
- **Cholesterol**: Total cholesterol level (mg/dL)
- **Blood Pressure**: Systolic/Diastolic readings (mmHg)
- **Heart Rate**: Resting heart rate (bpm)
- **Exercise Frequency**: How often you exercise per week
- **Smoking Status**: Yes/No
- **Family History**: Any family history of heart disease
- **Other Health Conditions**: Diabetes, hypertension, etc.

### Example: Complete Health Analysis Request

```bash
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "I am a 52-year-old male with the following health metrics: cholesterol 240 mg/dL, blood pressure 135/85 mmHg, resting heart rate 78 bpm, I exercise 2 times per week, non-smoker, no family history of heart disease. What is my heart disease risk?"
  }'
```

### Status Codes

| Code | Meaning |
|------|---------|
| 200 | Successful analysis |
| 400 | Missing prompt parameter |
| 500 | API key not configured or OpenRouter API error |

---

## 📚 Legacy API Reference (for `shd-screening-ai`)

*This section documents the original machine learning-based API if the `shd-screening-ai` service is used.*

### Endpoint

#### `POST /predict`

Makes a prediction based on the provided health parameters.

**Request Body (JSON):**

```json
{
    "age": 63,
    "sex": 1,
    "cp": 3,
    "trestbps": 145,
    "chol": 233,
    "fbs": 1,
    "restecg": 0,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 2.3,
    "slope": 0,
    "ca": 0,
    "thal": 1
}
```

**Response Body (JSON):**

```json
{
    "prediction": 1,
    "risk_level": "High Risk"
}
```

## 🆘 Troubleshooting

### Common Issues

#### 1. **"API key not configured" Error**

**Problem**: You see `{"error": "API key not configured."}` when making API requests.

**Solution**:
```bash
# Check if the environment variable is set
# Linux/macOS
echo $OPENROUTER_API_KEY

# Windows PowerShell
echo $env:OPENROUTER_API_KEY

# If not set, configure it
export OPENROUTER_API_KEY="your-actual-key"
# Then restart the FastAPI server
```

#### 2. **Connection Refused / Port Already in Use**

**Problem**: `Address already in use` or `Connection refused`

**Solution**:
```bash
# Use a different port
python -m uvicorn app:app --port 8001 --reload

# Or kill the process using port 8000 (on Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

#### 3. **ModuleNotFoundError: No module named 'fastapi'**

**Problem**: Missing dependencies

**Solution**:
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Linux/macOS
# or
.\venv\Scripts\activate   # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### 4. **OpenRouter API Returns 401 Unauthorized**

**Problem**: Authentication fails with OpenRouter

**Solution**:
- Verify your API key is correct (check on openrouter.ai dashboard)
- Ensure the key starts with `sk-or-v1-`
- The key hasn't expired or been revoked
- Check your OpenRouter account hasn't run out of credits

#### 5. **Slow Response Times**

**Problem**: Requests take a long time to complete

**Factors**:
- OpenRouter model (`meta-llama/llama-3.3-70b-instruct:free`) is rate-limited on free tier
- Network latency
- OpenRouter server load

**Solutions**:
- Upgrade to a paid OpenRouter plan for higher rate limits
- Check your internet connection
- Use a different model with faster response time

#### 6. **CORS Errors in Browser**

**Problem**: Frontend gets blocked with CORS error

**Solution**: Enable CORS in `app.py`:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Debugging Tips

1. **Check the console output** for error messages when starting the server
2. **Use curl to test the API directly**:
   ```bash
   curl -X POST http://localhost:8000/api/analyze \
     -H "Content-Type: application/json" \
     -d '{"prompt": "test"}'
   ```
3. **Check OpenRouter dashboard** for API status and quota information
4. **Verify Python version**: `python --version` (should be 3.8+)
5. **Review logs**: Check terminal output for detailed error messages

## 🤝 Contributing

We welcome contributions from everyone! Whether you want to:

- 🐛 **Report a bug** → [Open an issue](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-/issues)
- ✨ **Suggest a feature** → [Create a feature request](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-/issues/new)
- 💻 **Submit code** → [Create a pull request](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-/pulls)
- 📖 **Improve documentation** → [Edit README](README.md)

### Quick Start for Contributors

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/shd-heart-disease-prediction-.git

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Make your changes and commit
git commit -m "feat: add your feature description"

# 5. Push to your fork
git push origin feature/your-feature-name

# 6. Open a Pull Request on GitHub
```

### Development Setup

```bash
cd shd-hf
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md)

## 📄 License

This project is currently without a specified license. <!-- TODO: Add a LICENSE file (e.g., MIT, Apache 2.0) -->

## 🙏 Acknowledgments & Creator

**Creator**: [Anannya Vyas](https://github.com/Anannya-Vyas)  
**Year**: 2026  
**Repository**: [shd-heart-disease-prediction-](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-)

-   **Anannya Vyas**: Designed and developed the complete SHD (Structural Heart Disease) Screening AI application in 2026.
-   **Open APIs**: Thanks to NVIDIA AI and OpenRouter for providing accessible AI model APIs.
-   **Open-source Community**: For providing powerful libraries and tools like Python, FastAPI, OpenAI SDK, and more.

## 📞 Support & Contact

**Project Creator**: Anannya Vyas  
**Created**: 2026

-   🌐 GitHub: [Anannya-Vyas](https://github.com/Anannya-Vyas)
-   📁 Repository: [shd-heart-disease-prediction-](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-)
-   🐛 Issues: [GitHub Issues](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-/issues)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [Anannya Vyas](https://github.com/Anannya-Vyas) in 2026

[GitHub](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-) • [Issues](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-/issues)

</div>

