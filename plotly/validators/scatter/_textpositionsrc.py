import _plotly_utils.basevalidators


class TextpositionsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='textpositionsrc', parent_name='scatter', **kwargs
    ):
        super(TextpositionsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )