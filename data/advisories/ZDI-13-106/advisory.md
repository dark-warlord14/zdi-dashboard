# ZDI-13-106: (Pwn2Own) Adobe Reader Sandbox Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-106
- **ZDI-CAN:** ZDI-CAN-1840
- **Date:** 2013-05-30
- **CVE:** CVE-2013-2549 , CVE-2013-2550
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** George Hotz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-106/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of regular expressions. The issue lies in the ability to leak addresses by popping more items off of the stack than intended. An attacker can leverage this to execute code under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb13-15.html

## Disclosure Timeline

- 2013-05-14 - Vulnerability reported to vendor
- 2013-05-30 - Coordinated public release of advisory
