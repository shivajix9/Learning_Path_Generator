# 📚 Learning Path Generator

A Generative AI application that creates a structured learning roadmap for any skill or domain. The application helps learners understand what to learn, in what order, and how to progress from beginner to advanced levels.

---

## 🚀 Project Overview

Learners often know the skill they want to learn but struggle to break it into manageable stages. Without a structured roadmap, they jump between topics and resources inefficiently.

This project uses a Large Language Model (LLM) to generate a logical learning path based on a user-provided skill.

Example:

**Input:**

```
Data Science
```

**Output:**

```json
{
  "learning_stages": [
    "Beginner",
    "Intermediate",
    "Advanced"
  ],
  "key_topics": [
    "Python Programming",
    "Statistics",
    "Data Visualization",
    "Machine Learning",
    "Model Evaluation"
  ],
  "learning_goal_summary": "The roadmap introduces programming and statistics first, then progresses toward machine learning concepts and practical model building."
}
```

---

## 🎯 Objective

Generate a structured learning roadmap that includes:

* Learning Stages
* Key Topics
* Learning Goal Summary

The roadmap remains general, logical, and based only on the provided input skill.

---

## 🏗️ Project Architecture

```
User Input
     │
     ▼
Input Validation
     │
     ▼
Prompt Template
     │
     ▼
LLM (Gemini/Groq)
     │
     ▼
Pydantic Output Parser
     │
     ▼
Structured Output
     │
     ▼
Streamlit UI
```

---

## 📂 Project Structure

```
Learning_Path_Generator/
│
├── app.py
├── chain.py
├── model.py
├── parser.py
├── prompt.py
├── requirements.txt
├── .env
└── README.md
```

### File Description

| File             | Purpose                    |
| ---------------- | -------------------------- |
| app.py           | Streamlit User Interface   |
| prompt.py        | Prompt Template Definition |
| model.py         | LLM Initialization         |
| parser.py        | Pydantic Output Schema     |
| chain.py         | LangChain Runnable Chain   |
| .env             | API Key Storage            |
| requirements.txt | Project Dependencies       |

---

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* Pydantic
* Google Gemini API / Groq API
* dotenv

---

## 📋 Output Schema

```python
class LearningPathOutput(BaseModel):
    learning_stages: list[str]
    key_topics: list[str]
    learning_goal_summary: str
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd Learning_Path_Generator
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

or

```env
GROQ_API_KEY=your_api_key
```

### 5. Run Application

```bash
streamlit run app.py
```

---

## 🧪 Testing

### Test Case 1

Input:

```
Data Science
```

Expected:

* Beginner → Intermediate → Advanced roadmap
* Topics such as Python, Statistics, Machine Learning

Status: ✅ Pass

---

### Test Case 2

Input:

```
Pandas
```

Expected:

* Focused roadmap on Pandas concepts

Status: ✅ Pass

---

### Test Case 3

Input:

```
Transformer Architecture
```

Expected:

* Logical progression for advanced concepts

Status: ✅ Pass

---

## 🚨 Edge Cases Handled

### Empty Input

```
""
```

Result:

```
Please enter a skill.
```

### Numeric Input

```
12345
```

Result:

```
Skill must contain text.
```

### Special Characters

```
@@@@@
```

Result:

```
Invalid skill name.
```

### Excessively Long Input

Result:

```
Skill name too long.
```

---

## 🔮 Future Improvements

* Personalized learning plans
* Resource recommendations
* Learning duration estimation
* Export roadmap as PDF
* User authentication
* Progress tracking dashboard
* Database integration

---
* Home Page
* Generated Learning Roadmap
* Input Validation Messages
* Edge Case Handling

---

## 👨‍💻 Author

Shivaji

---

## 📄 License

This project is developed for educational and learning purposes.
