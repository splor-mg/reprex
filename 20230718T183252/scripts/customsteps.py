from frictionless import Step
import petl as etl

class remove_blank_rows(Step):
    """
    Remove blank lines that exceeds a threshold of blank values.

    :param int threshold: Maximum number of blanks values in a row to not be droped. Blank values include Nones, empty string and string with only spaces.

    """

    def __init__(self, threshold):
        self.threshold = threshold

    def transform_resource(self, resource):
        current = resource.to_copy()

        # Data
        def data():
            with current:
                for row in current.cell_stream:
                    num_blanks = sum(1 for item in row if str(item).strip() == "" or item == None)
                    if num_blanks <= self.threshold:
                        yield row
                    elif num_blanks < 25:
                        print(f'{num_blanks=}\n {row}')
        # Meta

        resource.data = data
        data().close()





    # def transform_resource(self, resource):
    #     current = resource.to_copy()
    #
    #     # Data
    #     def data():
    #         with current:
    #             for row in current.cell_stream:
    #                 num_blanks = sum(1 for item in row if str(item).strip() == "" or item == None)
    #                 if num_blanks <= self.threshold:
    #                     yield row
    #
    #     # Meta
    #     resource.data = etl.wrap(data())
