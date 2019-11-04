using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;

namespace MysteryOnline.Views
{
    public class ChatroomView : UserControl
    {
        public ChatroomView()
        {
            InitializeComponent();
        }

        private void InitializeComponent()
        {
            AvaloniaXamlLoader.Load(this);
        }
    }
}