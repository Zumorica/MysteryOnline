using IrcDotNet;

namespace MysteryOnline.Networking
{
    public class IrcBackend
    {
        public NetworkStatus Status { get; } = NetworkStatus.None;

        public StandardIrcClient LocalClient { get; private set; }
        
        public void Connect()
        {
            if (Status != NetworkStatus.None)
                return;
            
            LocalClient = new StandardIrcClient();
        }

        public void Disconnect()
        {
            throw new System.NotImplementedException();
        }
    }
}