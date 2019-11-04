using System;
using System.Reactive;
using ReactiveUI;

namespace MysteryOnline.ViewModels
{
    public class LoginViewModel : ViewModelBase
    {
        public ReactiveCommand<Unit, Unit> Login;
        
        public LoginViewModel()
        {
            Login = ReactiveCommand.Create(() =>
            {
                Console.WriteLine("login!");
            });
        }
    }
}