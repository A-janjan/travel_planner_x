"""Dependency-free repository checks that can run before optional integrations are installed."""

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_python_sources_parse():
    sources = [*ROOT.glob("*.py"), *ROOT.glob("agents/*.py"), *ROOT.glob("services/*.py"), *ROOT.glob("workflows/*.py")]
    assert sources
    for source in sources:
        ast.parse(source.read_text(encoding="utf-8"), filename=str(source))


def test_json_resources_are_valid():
    resources = [*ROOT.glob("data/*.json"), *ROOT.glob("frontend/data/*.json")]
    assert resources
    for resource in resources:
        json.loads(resource.read_text(encoding="utf-8"))


def test_no_embedded_rapidapi_credential():
    source = (ROOT / "agents" / "information_agent.py").read_text(encoding="utf-8")
    assert "car_api_key=None" in source
