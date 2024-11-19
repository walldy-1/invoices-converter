from const.invoice import InvoiceVarNames

class SessionNames(InvoiceVarNames):
    LOGGED_IN = "logged_in"
    USERNAME = "username"
    IS_GUEST = "is_guest"
    OPENAI_API_KEY = "openai_api_key"
    GOOGLE_API_KEY = "google_api_key"
    ENCRYPT_KEY = "encrypt_key"
    CURR_PAGE = "page"
    LOGIN_TYPE = "login_type"
    EDIT_INV_ACTION = "edit_inv_action"
    EDIT_INV_ACTION_ADD = "add"
    EDIT_INV_ACTION_UPDATE = "update"
    NEW_INVOICES = "new_invoices"
    EXISTING_INVOICES = "existing_invoices"
    INPUT_WIDGETS = "input_widgets"
    INPUT_WIDGETS_WIDGETS = "widgets"
    INPUT_WIDGETS_ERRORS = "errors"
    DIR_INVOICES = "dir_invoices"
    DIR_INVOICES_IMAGES = "dir_invoices_images"
    INV_FILTER_TEXT_WIDGET_KEY = "txt_filter_inv_text"
    INV_FILTER_DATE_FROM_WIDGET_KEY = "txt_filter_inv_issue_date_from"
    INV_FILTER_DATE_TO_WIDGET_KEY = "txt_filter_inv_issue_date_to"
    INV_FILTER_TOTAL_GROSS_AMOUNT_FROM_WIDGET_KEY = "txt_filter_inv_total_gross_amount_from"
    INV_FILTER_TOTAL_GROSS_AMOUNT_TO_WIDGET_KEY = "txt_filter_inv_total_gross_amount_to"