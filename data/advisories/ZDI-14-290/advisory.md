# ZDI-14-290: Attachmate Reflection Secure FTP Client rftpcom.dll SaveSettings Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-290
- **ZDI-CAN:** ZDI-CAN-2106
- **Date:** 2014-08-12
- **CVE:** CVE-2014-0605
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Attachmate
- **Affected Products:** Reflection
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-290/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Attachmate Reflection Secure FTP Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Attachmate Reflection Secure FTP Client ActiveX control SaveSettings method which suffers from a directory traversal flaw. An attacker can exploit this condition to achieve code execution under the context of the browsing user.

## Additional Details

Attachmate has issued an update to correct this vulnerability. More details can be found at: http://support.attachmate.com/techdocs/2546.html

## Disclosure Timeline

- 2014-04-22 - Vulnerability reported to vendor
- 2014-08-12 - Coordinated public release of advisory
