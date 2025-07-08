from django.urls import path
from .views import SystemsSettingsView
urlpatterns = [
    path('systems_settings/', SystemsSettingsView.as_view(), name='system-settings-list'),
    path('systems_settings/create/', SystemsSettingsView.as_view(), name='system-settings-create'),
    path('systems_settings/<int:setting_id>/update/', SystemsSettingsView.as_view(), name='system-settings-update'),
    path('systems_settings/<int:setting_id>/delete/', SystemsSettingsView.as_view(), name='system-settings-delete'),
]