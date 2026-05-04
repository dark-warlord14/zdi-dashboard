# ZDI-11-002: Microsoft Internet Explorer MSADO CacheSize Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-002
- **ZDI-CAN:** ZDI-CAN-856
- **Date:** 2011-01-11
- **CVE:** CVE-2011-0027
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 8
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-002/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. This vulnerability was submitted to the ZDI via at the annual Pwn2Own competition at CanSecWest. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the MSADO component. When handling the a user specified CacheSize property the process uses this value to calculate the 'real' cache size. This value is used without proper validation. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS11-002.mspx

## Disclosure Timeline

- 2010-03-26 - Vulnerability reported to vendor
- 2011-01-11 - Coordinated public release of advisory
