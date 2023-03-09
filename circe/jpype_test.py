import jpype
import jpype.imports
from jpype.types import *
import json

jpype.startJVM(classpath=[r'C:\Users\FMa1805.36838\Repositories\python-circe\circe\java\*'])

cohort = {
      "ConceptSets": [
        {
          "id": 0,
      "name": "Some ConceptSet",
      "expression": {
            "items": []
      }
    }
  ],
  "PrimaryCriteria": {
        "CriteriaList": [
          {
            "ConditionOccurrence": {
              "CodesetId": 0
        }
      }
    ],
    "ObservationWindow": {
          "PriorDays": 0,
      "PostDays": 0
    },
    "PrimaryCriteriaLimit": {
          "Type": "First"
    }
  },
  "QualifiedLimit": {
        "Type": "First"
  },
  "ExpressionLimit": {
        "Type": "First"
  },
  "InclusionRules": [],
  "CensoringCriteria": [],
  "CollapseSettings": {
        "CollapseType": "ERA",
    "EraPad": 0
  },
  "CensorWindow": {}
}

definition = json.dumps(cohort)
from org.ohdsi.circe.cohortdefinition import CohortExpression
output = CohortExpression.fromJson(definition)
print(output)

from org.ohdsi.circe.cohortdefinition.printfriendly import MarkdownRender
print(MarkdownRender().renderCohort(output))
