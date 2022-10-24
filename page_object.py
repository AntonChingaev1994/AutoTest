class Page():

    '''Auth'''
    login = 'login'
    passowrd = 'password'
    button_come_in = '//button[@class="btn btn-info"]'

    """Open Project"""
    project = '//a[@class="dropdown-toggle"]//span[text()="Проекты "]'
    project_bis = '//ul[@class="dropdown-menu show"]//a[text()="БИС"]'
    project_training = '//ul[@class="dropdown-menu show"]//a[text()="Учебный"]'
    project_test = '//ul[@class="dropdown-menu "]//a[text()="ТЕСТ"]'

    """project management"""
    project_management = '//a[@title="Управление проектом"]'
    create_button = '//a[@class="iframeEditor btn btn-primary pm_doc_add"]'
    btn_close = '//a[@class="close"]'

    сontract_management = '//div[@id="compound_page_tab_pm"]//a[@data-subtab="contracts"]'
    metca_create_contract = '//div[@class="modal-header modal-draggable-cursor"]'

    documents_management = '//div[@id="compound_page_tab_pm"]//a[@data-subtab="docs"]'
    metca_create_documents = '//div[@class="modal-header modal-draggable-cursor"]'

    project_management_doc = '//div[@id="compound_page_tab_pm"]//a[@data-subtab="pm_docs"]'
    project_management_doc_new = '//div[@id="compound_page_tab_pm"]//a[@data-subtab="pm_docs2"]'
    metca_project_management_doc = '//div[@class="modal-header modal-draggable-cursor"]'

    upm_setup = '//div[@id="compound_page_tab_pm"]//a[@data-subtab="pm_settings"]'
    category_setting_button = '//div[@class="pmdocs_content wo-container"]//a[@class="btn btn-primary"]'
    button_add = '//a[@class="iframeEditor btn btn-primary "]'
    partition_window = '//div[@class="modal-content"]'

    field_name = '//textarea[@class="form-control lib-control"]'
    btn_create_in_frame = '//a[@class="btn btn-primary btn-iframe-save-override"]'
    field_name_reestr = '//td[@class="rt_c rt_field_title"]'

    first_entry = '//div[@class="structural_list"]//tr[@class="item rt1"]//td[@class="rt_c rt_field_actions"]'

    structural_list = '//div[@class="structural_list"]'
    rt_field_actions = '//td[@class="rt_c rt_field_actions"]'

    delete_field = '//ul[@class="wo-dropdown dropdown-menu pull-right show"]//li[@class="wo-act-delete"]'

    new_doc = '//a[@data-subtab="pm_docs2"]'
    but_add = '//a[@class="iframeEditor btn btn-primary "]'

    btn_fill_in_template = '//a[text()="Заполнить по шаблону"]'
    btn_success = '//a[@class="btn btn-success"]'

    list_table = "//div[@class='tree_list_table']"