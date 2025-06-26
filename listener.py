import subprocess

titulo = "🚀 Teste de Notificação"
mensagem = "O script foi executado com sucesso!"

subprocess.run([
    "powershell",
    "-Command",
    f'''
    [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;
    $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);
    $template.GetElementsByTagName("text").Item(0).AppendChild($template.CreateTextNode("{titulo}")) > $null;
    $template.GetElementsByTagName("text").Item(1).AppendChild($template.CreateTextNode("{mensagem}")) > $null;
    $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("Notificação Script");
    $notification = [Windows.UI.Notifications.ToastNotification]::new($template);
    $notifier.Show($notification);
    '''
], shell=True)