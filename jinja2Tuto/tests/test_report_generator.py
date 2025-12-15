import pytest

from jinja2Tuto.src.report_generator import ReportGenerator
from pathlib import Path


@pytest.fixture
def report_generator():
    template_dir = (Path.cwd() / "jinja2Tuto" / "templates").as_posix()
    return ReportGenerator(template_dir)


@pytest.fixture
def report_params():
    report_data = {
        "organization": {
            "name": "CASD",
            "department": "Projet Management"
        },
        "report": {
            "period": "2026",
            "author": "Thalia",
            "date": "2025-12-15",
            "summary": "This report provides an estimated budget for planned activities."
        },
        "budget": {
            "rows": [
                {"category": "Infrastructure", "description": "Servers and storage", "amount": 120000},
                {"category": "Software", "description": "Licenses and subscriptions", "amount": 45000},
                {"category": "Staffing", "description": "Contractors and training", "amount": 8000},
                {"category": "Hobby", "description": "for the pleasure of employee", "amount": 9999999999},
            ],
            "total": 245000
        }
    }
    return report_data


def test_display_generated_source(report_generator, report_params):
    temp_name = "budget_report.html"

    report_generator.display_generated_source(temp_name, report_params)


def test_persist_generated_source(report_generator, report_params):
    temp_name = "budget_report.html"
    report_generator.persist_generated_source(temp_name, report_params,
                                              "C:/Users/pliu/Documents/git/Jinja2Tuto/data/tmp/out/test_report.html")
