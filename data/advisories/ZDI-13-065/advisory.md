# ZDI-13-065: Microsoft Internet Explorer RDP ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-065
- **ZDI-CAN:** ZDI-CAN-1675
- **Date:** 2013-05-10
- **CVE:** CVE-2013-1296
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** c1d2d9acc746ae45eeb477b97fa74688
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Remote Desktop ActiveX control. By manipulating TransportSettings or AdvancedSettings, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this to gain code execution in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms13-029

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
