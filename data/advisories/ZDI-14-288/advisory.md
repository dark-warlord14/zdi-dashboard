# ZDI-14-288: Attachmate Reflection Secure FTP Client rftpcom.dll Multiple Memory Corruption Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-14-288
- **ZDI-CAN:** ZDI-CAN-2075
- **Date:** 2014-08-12
- **CVE:** CVE-2014-0603
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Attachmate
- **Affected Products:** Reflection
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-288/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Attachmate Reflection Secure FTP Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Attachmate Reflection Secure FTP Client rftpcom.dll ActiveX control GetGlobalSettings method which dereferences attacker-supplied input as memory addresses. An attacker can exploit this condition to achieve code execution under the context of the browser process.

## Additional Details

Attachmate has issued an update to correct this vulnerability. More details can be found at: http://support.attachmate.com/techdocs/2501.html

## Disclosure Timeline

- 2014-04-22 - Vulnerability reported to vendor
- 2014-08-12 - Coordinated public release of advisory
