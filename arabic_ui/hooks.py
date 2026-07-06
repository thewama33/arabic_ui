app_name = "arabic_ui"
app_title = "Arabic Ui"
app_publisher = "Omar soliman"
app_description = "Arabic R"
app_email = "thewama33@gmail.com"
app_license = "mit"

# Send non-GET requests for this app's endpoints as native `application/json`
# bodies instead of form-encoded, per-key JSON-stringified values.
use_json_request_body = True

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "arabic_ui",
# 		"logo": "/assets/arabic_ui/logo.png",
# 		"title": "Arabic Ui",
# 		"route": "/arabic_ui",
# 		"has_permission": "arabic_ui.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/arabic_ui/css/arabic_ui.css"
# app_include_js = "/assets/arabic_ui/js/arabic_ui.js"

# include js, css files in header of web template
# web_include_css = "/assets/arabic_ui/css/arabic_ui.css"
# web_include_js = "/assets/arabic_ui/js/arabic_ui.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "arabic_ui/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "arabic_ui/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "arabic_ui.utils.jinja_methods",
# 	"filters": "arabic_ui.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "arabic_ui.install.before_install"
# after_install = "arabic_ui.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "arabic_ui.uninstall.before_uninstall"
# after_uninstall = "arabic_ui.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "arabic_ui.utils.before_app_install"
# after_app_install = "arabic_ui.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "arabic_ui.utils.before_app_uninstall"
# after_app_uninstall = "arabic_ui.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "arabic_ui.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "arabic_ui.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"arabic_ui.tasks.all"
# 	],
# 	"daily": [
# 		"arabic_ui.tasks.daily"
# 	],
# 	"hourly": [
# 		"arabic_ui.tasks.hourly"
# 	],
# 	"weekly": [
# 		"arabic_ui.tasks.weekly"
# 	],
# 	"monthly": [
# 		"arabic_ui.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "arabic_ui.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "arabic_ui.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "arabic_ui.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "arabic_ui.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["arabic_ui.utils.before_request"]
# after_request = ["arabic_ui.utils.after_request"]

# Job Events
# ----------
# before_job = ["arabic_ui.utils.before_job"]
# after_job = ["arabic_ui.utils.after_job"]

# after_file_upload = ["arabic_ui.utils.after_file_upload"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"arabic_ui.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# Require all whitelisted methods to have type annotations
require_type_annotated_api_methods = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

