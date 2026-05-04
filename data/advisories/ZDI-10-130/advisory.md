# ZDI-10-130: Mozilla Firefox NodeIterator Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-130
- **ZDI-CAN:** ZDI-CAN-712
- **Date:** 2010-07-20
- **CVE:** CVE-2010-1209
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-130/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the victim must visit a malicious page or open a malicious file. The specific flaw exists within the application's implementation of the NodeIterator interface for traversal of the Document Object Model. Due to the implementation requiring a javascript callback, an attacker can utilize the callback in order to manipulate the contents of the page. By doing so in an unexpected manner, an attacker can cause the process to corrupt memory. Successful exploitation will lead to code execution under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-36.html

## Disclosure Timeline

- 2010-03-12 - Vulnerability reported to vendor
- 2010-07-20 - Coordinated public release of advisory
