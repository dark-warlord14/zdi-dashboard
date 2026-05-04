# ZDI-14-291: Attachmate Reflection Pro FTP rftpcom15.dll GetSiteProperties3 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-291
- **ZDI-CAN:** ZDI-CAN-2354
- **Date:** 2014-08-12
- **CVE:** CVE-2014-0603
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Attachmate
- **Affected Products:** Reflection
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-291/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Attachmate Reflection Pro FTP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ActiveX control's GetSiteProperties3 method. The control suffers from an untrusted pointer dereference vulnerability because it blindly dereferences an attacker-supplied memory address. An attacker can exploit this condition to achieve code execution under the context of the browser process.

## Additional Details

Attachmate has issued an update to correct this vulnerability. More details can be found at: http://support.attachmate.com/techdocs/2501.html

## Disclosure Timeline

- 2014-06-23 - Vulnerability reported to vendor
- 2014-08-12 - Coordinated public release of advisory
