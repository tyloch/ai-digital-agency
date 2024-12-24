from agency_swarm import Agent, Agency
from tools import AnalyzeProjectRequirements, CreateTechnicalSpecification

def create_agency(api_headers):
    """
    Creates and returns all agents (CEO, CTO, Product Manager, Developer, Client Manager)
    and the Agency with the same instructions, tools, and parameters
    exactly as in the original code.
    """
    ceo = Agent(
        name="Project Director",
        description="You are a CEO of multiple companies in the past and have a lot of experience in evaluating projects and making strategic decisions.",
        instructions="""
        You are an experienced CEO who evaluates projects. Follow these steps strictly:

        1. FIRST, use the AnalyzeProjectRequirements tool with:
           - project_name: The name from the project details
           - project_description: The full project description
           - project_type: The type of project (Web Application, Mobile App, etc)
           - budget_range: The specified budget range

        2. WAIT for the analysis to complete before proceeding.

        3. Review the analysis results and provide strategic recommendations.
        """,
        tools=[AnalyzeProjectRequirements],
        api_headers=api_headers,
        temperature=0.7,
        max_prompt_tokens=25000
    )

    cto = Agent(
        name="Technical Architect",
        description="Senior technical architect with deep expertise in system design.",
        instructions="""
        You are a technical architect. Follow these steps strictly:

        1. WAIT for the project analysis to be completed by the CEO.

        2. Use the CreateTechnicalSpecification tool with:
           - architecture_type: Choose from monolithic/microservices/serverless/hybrid
           - core_technologies: List main technologies as comma-separated values
           - scalability_requirements: Choose high/medium/low based on project needs

        3. Review the technical specification and provide additional recommendations.
        """,
        tools=[CreateTechnicalSpecification],
        api_headers=api_headers,
        temperature=0.5,
        max_prompt_tokens=25000
    )

    product_manager = Agent(
        name="Product Manager",
        description="Experienced product manager focused on delivery excellence.",
        instructions="""
        - Manage project scope and timeline giving the roadmap of the project
        - Define product requirements and you should give potential products and features that can be built for the startup
        """,
        api_headers=api_headers,
        temperature=0.4,
        max_prompt_tokens=25000
    )

    developer = Agent(
        name="Lead Developer",
        description="Senior developer with full-stack expertise.",
        instructions="""
        - Plan technical implementation
        - Provide effort estimates
        - Review technical feasibility
        """,
        api_headers=api_headers,
        temperature=0.3,
        max_prompt_tokens=25000
    )

    client_manager = Agent(
        name="Client Success Manager",
        description="Experienced client manager focused on project delivery.",
        instructions="""
        - Ensure client satisfaction
        - Manage expectations
        - Handle feedback
        """,
        api_headers=api_headers,
        temperature=0.6,
        max_prompt_tokens=25000
    )

    agency = Agency(
        [
            ceo, 
            cto, 
            product_manager, 
            developer, 
            client_manager,
            [ceo, cto],
            [ceo, product_manager],
            [ceo, developer],
            [ceo, client_manager],
            [cto, developer],
            [product_manager, developer],
            [product_manager, client_manager]
        ],
        async_mode='threading',
        shared_files='shared_files'
    )

    return ceo, cto, product_manager, developer, client_manager, agency
