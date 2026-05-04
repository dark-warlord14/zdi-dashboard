# ZDI-12-156: Cisco AnyConnect VPN Client Arbitrary Program Instantiation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-156
- **ZDI-CAN:** ZDI-CAN-1411
- **Date:** 2012-08-22
- **CVE:** CVE-2012-2493
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** AnyConnect VPN Client
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-156/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco AnyConnect VPN Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to insufficient signature checks with the Cisco AnyConnect VPN Client. When the client is invoked through the ActiveX control it downloads and checks a file called vpndownloader.exe. This file has to be properly signed by Cisco. Once this file is downloaded it is run and downloads additional configuration files. Within the downloaded config file it is possible to force a download of executable files. Those files are not properly checked for valid certificates and are run on the host as soon as they are downloaded.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco -sa-20120620-ac

## Disclosure Timeline

- 2011-11-22 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
