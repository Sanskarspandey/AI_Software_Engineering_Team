# 🤖 AI Software Engineering Team

> A multi-agent AI system that transforms a natural language software idea into software engineering artifacts and a full-stack project scaffold using LangGraph, Ollama, and specialized AI agents.

---

## 📌 Overview

**AI Software Engineering Team** is an Agentic AI project that simulates a real software development company.

Instead of relying on a single chatbot, the system coordinates multiple AI agents, each with a specialized responsibility, to collaboratively transform a user's software idea into a structured project.

Given a prompt such as:

> **"Build me an Airbnb Clone."**

the system automatically:

* Understands the project requirements
* Creates a Product Specification
* Generates a Software Requirements Specification (SRS)
* Designs the UI architecture
* Designs the database
* Generates a backend project scaffold
* Generates a frontend project scaffold

The project demonstrates how multiple AI agents can collaborate using **LangGraph** to automate software engineering workflows.

---

# 🚀 Features

* Multi-Agent AI Workflow
* LangGraph-based orchestration
* Supervisor & Router architecture
* Structured outputs using Pydantic
* Automatic document generation
* Backend project generation
* Frontend project generation
* Local LLM support using Ollama
* Modular and extensible architecture

---

# 🏗️ Architecture

```
                     User Request
                           │
                           ▼
                  LangGraph Supervisor
                           │
                           ▼
                        Router
                           │
 ┌─────────────────────────────────────────────────────────┐
 │                                                         │
 ▼                                                         ▼
Product Manager                                   Clarification
       │
       ▼
Business Analyst
       │
       ▼
UI Designer
       │
       ▼
Database Engineer
       │
       ▼
Backend Engineer
       │
       ▼
Frontend Engineer
```

Each agent receives structured information from the previous agent, performs its own specialized task, and forwards the updated project state to the next stage.

---

# 🤖 AI Agents

## 1. Product Manager

### Responsibilities

* Understand user requirements
* Define product vision
* Identify target users
* Generate core features
* Define MVP scope

### Output

* Product Specification

---

## 2. Business Analyst

### Responsibilities

* Convert Product Specification into an SRS
* Generate functional requirements
* Generate non-functional requirements
* Generate user stories
* Generate use cases

### Output

* Software Requirements Specification (SRS)

---

## 3. UI Designer

### Responsibilities

* Design application screens
* Generate navigation flow
* Suggest reusable UI components
* Recommend colors and typography
* Plan responsive design

### Output

* UI Design Specification

---

## 4. Database Engineer

### Responsibilities

* Select database technology
* Design collections/tables
* Define relationships
* Recommend indexes
* Define validation rules
* Identify Mongoose models

### Output

* Database Design Specification

---

## 5. Backend Engineer

### Responsibilities

* Generate an Express.js backend scaffold
* Generate project structure
* Generate backend source files
* Create configuration files
* Prepare API architecture

### Output

```
backend/

package.json

src/

config/

controllers/

middleware/

models/

routes/

utils/
```

---

## 6. Frontend Engineer

### Responsibilities

* Generate a React frontend scaffold
* Generate application pages
* Generate reusable components
* Configure routing
* Configure API integration

### Output

```
frontend/

package.json

src/

pages/

components/

services/

assets/

styles/
```

---

# 📂 Project Structure

```
AI_Software_Engineering_Team/

agents/
    product_manager/
    business_analyst/
    ui_designer/
    database_engineer/
    backend_engineer/
    frontend_engineer/

backend/

frontend/

docs/

generated_projects/

graphs/

models/

schemas/

tools/

utils/

main.py

state.py
```

---

# 🧠 Technologies Used

### AI

* LangGraph
* Ollama
* Qwen 2.5
* Pydantic

### Backend

* Python
* Express.js (generated)
* MongoDB (generated)
* Mongoose (generated)

### Frontend

* React
* Vite
* Tailwind CSS

### Utilities

* Git
* GitHub

---

# ⚙️ Workflow

```
User Prompt

↓

Supervisor

↓

Product Manager

↓

Business Analyst

↓

UI Designer

↓

Database Engineer

↓

Backend Engineer

↓

Frontend Engineer

↓

Generated Project
```

---

# 📄 Generated Documents

The system automatically generates:

* Product Specification
* Software Requirements Specification
* UI Design Specification
* Database Design Specification

These documents are stored in the `docs/` directory.

---

# 📦 Generated Project

The generated project is created under:

```
generated_projects/

airbnb_clone/

backend/

frontend/
```

---

# ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/Sanskarspandey/AI_Software_Engineering_Team.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama serve
```

Ensure the required model is available:

```bash
ollama pull qwen2.5:3b
```

Run the project:

```bash
python main.py
```

---

# 💡 Example Prompt

```
Build me an Airbnb clone.
```

---

# 🎯 Learning Outcomes

This project demonstrates:

* Multi-Agent AI Design
* LangGraph Workflows
* State Management
* Structured AI Outputs
* AI Agent Collaboration
* Software Engineering Automation
* Backend Code Generation
* Frontend Code Generation
* Local LLM Integration

---

# 🔮 Future Improvements

Potential future enhancements include:

* QA Engineer Agent
* DevOps Engineer Agent
* Docker support
* CI/CD pipeline generation
* Automated testing
* Deployment automation
* Human-in-the-loop approvals
* Support for additional programming languages
* Cloud LLM integration

---

# 👨‍💻 Author

**Sanskar Pandey**

* GitHub: https://github.com/Sanskarspandey

---

# ⭐ If you found this project interesting

Please consider giving the repository a ⭐ on GitHub.
