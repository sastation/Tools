//var test="test.com";
//alert("Hello*."+test);

function FindProxyForURL(url, host)
{
    //var us_proxy = "PROXY 192.168.100.107:8087; PROXY 192.168.100.107:8081 ";
    var us_proxy = "PROXY 192.168.100.107:8081";
    var sh_proxy = "DIRECT";

    var domains = new Array (
        "google.com.hk", 
        "google.com.sg",
        "akamaihd.net",
        "tinypic.com",
        "top81.org",
        "top81.ws",
        "top81.net",
        "googleusercontent.com",
        "===private above===",
        <domains-from-gfwlist> 
        "===END==="
    );

    for (var index in domains)
    {
        var domain = domains[index];
        if (dnsDomainIs(host, domain) || dnsDomainIs(host, "*."+domain))
        {
            //alert("transfer " + domain + " to us_proxy");
            return us_proxy;
        }
    }

    return "DIRECT";
    
/*
    var matchs = new Array (
        "twitter.com/*",
        "facebook.com/*",
        "youtube.com/*",
        "top81.org/*",
        "top81.ws/*",
        "top81.net/*",
        "===END==="
    );

    for (var index in matchs)
    {
        var match = matchs[index];
        if (shExpMatch(host, "*twitter.com*"))
        {
            //alert("transfer " + match + " to us_proxy");
            return us_proxy;
        }
    }
*/

/*
    if (isPlainHostName(host)
        || isInNet(host, "192.168.0.0", "255.255.0.0")
        || dnsDomainIs(host, "family.cnict.info")
       )
    {
        return "DIRECT"
    }
    else
    {
        return sh_proxy;
    }
*/
}
