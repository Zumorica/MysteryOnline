using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;

namespace MysteryOnline.Views
{
    public class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            ClientSize = new Size(1366d, 768d);
        }

        private void InitializeComponent()
        {
            AvaloniaXamlLoader.Load(this);
        }
    }
}