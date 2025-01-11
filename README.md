### AI-Driven Digital Agency Framework

An AI application that simulates a full-service software agency using multiple AI agents to analyze and plan software projects. Each agent represents a different role in the project lifecycle, from strategic planning to technical implementation.

- **`tools.py`**: Defines custom tools (`AnalyzeProjectRequirements` and `CreateTechnicalSpecification`).
- **`agents.py`**: Creates specialized AI agents (CEO, CTO, Product Manager, Developer, Client Success) and configures their interactions.
- **`main.py`**: Streamlit application handling UI, form input, and agent responses.

## Features

1. **Multi-Agent Architecture**  
   - Five specialized AI agents, each with distinct expertise:
     - **CEO (Strategic Leader)**
     - **CTO (Technical Architect)**
     - **Product Manager**
     - **Lead Developer**
     - **Client Success Manager**

2. **Custom Tools**  
   - **AnalyzeProjectRequirements** for analyzing project feasibility  
   - **CreateTechnicalSpecification** for technical architecture, stack, and scalability  

3. **Async Communication**  
   - Parallel processing of each agent’s analysis  
   - Non-blocking operations for more efficient collaboration  

4. **Streamlit UI**  
   - Interactive form to capture project details  
   - Expander sections for input and AI strategy responses  
   - Easy toggles (checkboxes, if desired) for agent selection (optional)  

5. **Extendable**  
   - Additional features like Gantt charts for timeline visualization or budget estimators can be integrated easily  

## Prerequisites

- **Python 3.9+** (recommended)
- **pip** or **conda** for package management
- An **OpenAI API Key** (or equivalent GPT-like provider)

## Installation

1. **Clone** the repository:
    ```bash
    git clone https://github.com/tyloch/ai-digital-agency.git
    cd ai-digital-agency
    ```

2. **Install dependencies** (sample command):
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Obtain an **OpenAI API Key** from [OpenAI](https://platform.openai.com/api-keys).
2. Run `main.py` with Streamlit:
    ```bash
    streamlit run main.py
    ```
3. In the **sidebar**, enter your **API key**.

## Usage

1. **Launch the app**:
    ```bash
    streamlit run main.py
    ```
2. **Fill in** the project form:
   - Project name, description, type, timeline, budget, etc.
3. **Click “Analyze Project”**:
   - Agents collaborate asynchronously to produce:
     - **CEO’s Project Analysis**
     - **CTO’s Technical Specification**
     - **Product Manager’s Plan**
     - **Developer’s Implementation Suggestions**
     - **Client Success Strategy**
4. **Review** each response in the generated tabs.

## Customization

- **tools.py**: Add or modify analysis tools and their logic.
- **agents.py**: Configure agent instructions, personalities, or add new agents.
- **main.py**: Adjust UI elements, incorporate Gantt charts, or a budget estimator if desired.

## Troubleshooting

- **API Key Issues**: Ensure a valid key is entered. The app won’t proceed if left empty.
- **Agent Errors**: Check logs for JSON parsing or completion issues.
- **Dependency Issues**: Confirm your Python environment has correct versions.

## Contributing

1. **Fork** this repo.
2. **Create a feature branch**.
3. **Submit a pull request** with a clear description of changes and improvements.

## License

[MIT License](LICENSE) - Feel free to adapt and expand this project for your needs.
*
