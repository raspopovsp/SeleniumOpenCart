

class LoginPageLocators:

    login_url = 'http://localhost/admin/index.php'
    admin_path = '?route=common/login'
    admin_panel_path = '?route=common/dashboard'
    forgotten_pass_path = '?route=common/forgotten'

    header_logo = {'css': '#header-logo'}

    panel_heading_title = {'css': 'h1.panel-title'}
    panel_body = {'css': '.panel-body'}

    form = {'css': 'form'}
    username_label = {'css': 'label[for="input-username"]'}
    username_input = {'css': '#input-username'}

    password_label = {'css': 'label[for="input-password"]'}
    password_input = {'css': '#input-password'}
    password_restore_btn = {'css': 'span.help-block > a'}

    submit = {'css': form['css'] + ' button[type="submit"]'}

    footer = {'css': 'footer'}
    footer_link = {'css': footer['css'] + ' a'}

    restore_pass_form_title = {'css': 'h1.panel-title'}
    username_email_label = {'css': 'label[for="input-email"]'}
    email_input = {'css': '#input-email'}
    reset_pwd_btn = {'css': 'button'}
    cancel_btn = {'css': 'div.text-right > a[data-original-title="Cancel"]'}

    alert_success = {'css': '.alert-success'}
    alert_success_text = "An email with a confirmation link has been sent your admin email address."

    alert_danger = {'css': '.alert-danger'}
    alert_danger_text = "Warning: The E-Mail Address was not found in our records, please try again!"
