from typing import List, Literal, Dict, Optional
from agency_swarm import BaseTool
from pydantic import Field, BaseModel

class AnalyzeProjectRequirements(BaseTool):
    project_name: str = Field(..., description="Name of the project")
    project_description: str = Field(..., description="Project description and goals")
    project_type: Literal["Web Application", "Mobile App", "API Development", 
                         "Data Analytics", "AI/ML Solution", "Other"] = Field(..., 
                         description="Type of project")
    budget_range: Literal["$10k-$25k", "$25k-$50k", "$50k-$100k", "$100k+"] = Field(..., 
                         description="Budget range for the project")

    class ToolConfig:
        name = "analyze_project"
        description = "Analyzes project requirements and feasibility"
        one_call_at_a_time = True

    def run(self) -> str:
        """Analyzes project and stores results in shared state"""
        if self._shared_state.get("project_analysis", None) is not None:
            raise ValueError("Project analysis already exists. Please proceed with technical specification.")
        
        analysis = {
            "name": self.project_name,
            "type": self.project_type,
            "complexity": "high",
            "timeline": "6 months",
            "budget_feasibility": "within range",
            "requirements": ["Scalable architecture", "Security", "API integration"]
        }
        
        self._shared_state.set("project_analysis", analysis)
        return "Project analysis completed. Please proceed with technical specification."

class CreateTechnicalSpecification(BaseTool):
    architecture_type: Literal["monolithic", "microservices", "serverless", "hybrid"] = Field(
        ..., 
        description="Proposed architecture type"
    )
    core_technologies: str = Field(
        ..., 
        description="Comma-separated list of main technologies and frameworks"
    )
    scalability_requirements: Literal["high", "medium", "low"] = Field(
        ..., 
        description="Scalability needs"
    )

    class ToolConfig:
        name = "create_technical_spec"
        description = "Creates technical specifications based on project analysis"
        one_call_at_a_time = True

    def run(self) -> str:
        """Creates technical specification based on analysis"""
        project_analysis = self._shared_state.get("project_analysis", None)
        if project_analysis is None:
            raise ValueError("Please analyze project requirements first using AnalyzeProjectRequirements tool.")
        
        spec = {
            "project_name": project_analysis["name"],
            "architecture": self.architecture_type,
            "technologies": self.core_technologies.split(","),
            "scalability": self.scalability_requirements
        }
        
        self._shared_state.set("technical_specification", spec)
        return f"Technical specification created for {project_analysis['name']}."
