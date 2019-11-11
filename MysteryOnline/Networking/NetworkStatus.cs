namespace MysteryOnline.Networking
{
    /// <summary>
    ///     The current status of the network backend.
    /// </summary>
    public enum NetworkStatus
    {
        /// <summary>
        ///     The network is still uninitialized.
        /// </summary>
        None,
        
        /// <summary>
        ///     The network is still connecting.
        /// </summary>
        Connecting,
        
        /// <summary>
        ///     The network is connected and ready.
        /// </summary>
        Connected,
        
        /// <summary>
        ///     The network has been disconnected.
        /// </summary>
        Disconnected
    }
}