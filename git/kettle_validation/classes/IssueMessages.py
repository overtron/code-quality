
__author__ = 'aoverton'

class IssueMessages:
    # warnings
    not_required = "Input files should be set to 'Y' unless they are optional for the transformation"
    lazy_conversion = "Be careful enabling lazy conversion. It's only appropriate for simple reading and writing of " \
                      "data"
    ignore_empty_file = "Are you sure you want to ignore empty files?"
    ignore_missing_file = "Are you sure you want to ignore missing files?"
    select_star = "Are you sure you want to use 'select *'? It's better to specify the fields you want in case the " \
                  "table schema changes"
    bulk_loader = "Consider using another output method if possible. Bulk loader can cause resource contention in Mysql"
    ignore_insert_errors = "Be careful enabling 'ignore insert errors' this supresses all insert errors mysql might " \
                           "throw"
    unique_rows = "The unique rows option is not reliable. It is preferable to use a separate unique rows step"
    null_steps = "Bulit in steps that convert values to null don't work well. Consider using Javascript step instead."

    # errors
    missing_encoding = "File encoding should be set on content tab"
    limit_set = "Limit field should not be used on content tab"
    missing_utf_8 = "Output files should be UTF-8 encoded"
    default_fifo = "Default fifo file '/tmp/fifo' should not be used. Please choose a unique name"
    multi_tabs = "You should only use one tab of the 'Select Values' step at a time as the behavior is undefined " \
                 "when using multiple tabs."
    disabled_hops = "Production jobs should not contain disabled hops"
    hidden_error_handlers = "Error handlers should always send their output to another step (e.g. Dummy step) " \
                            "otherwise they can unknowingly hide errors in the transformation"

    # notifications
    external_script = "Unable to follow path to inserted script. Data Logistics may be used."
    data_logistics = "Data logistics is used in this transformation."
    ftb_importv0 = "FTB Import step v0 exists"
    ftb_importv1 = "FTB Import step v1 exists"