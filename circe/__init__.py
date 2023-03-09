import jpype
import jpype.imports

from jpype.types import *
from importlib.resources import files


jar_folder = files('circe.java')
data_folder = files('circe.data')

# start the JVM

if __name__ == '__main__':

    jpype.startJVM(classpath=[str(jar_folder.joinpath('*'))])

    # import the Java classes
    from org.ohdsi.circe.cohortdefinition import CohortExpression
    from org.ohdsi.circe.cohortdefinition.printfriendly import MarkdownRender

    # load the JSON definition
    with data_folder.joinpath('simpleCohort.json').open() as f:
        definition = f.read()

    # convert the JSON to a Java object
    output = CohortExpression.fromJson(definition)

    # print the Markdown
    print(MarkdownRender().renderCohort(output))