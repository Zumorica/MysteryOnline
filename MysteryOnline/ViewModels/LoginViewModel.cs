using System;
using System.Reactive;
using MysteryOnline.Views;
using ReactiveUI;
using Serilog.Debugging;

namespace MysteryOnline.ViewModels
{
    public class LoginViewModel : ViewModelBase
    {
        public LoginViewModel()
        {

        }

        public void Login()
        {
            ((MainWindow)App.Current.MainWindow).Content = new ChatroomViewModel();
        }
    }
}