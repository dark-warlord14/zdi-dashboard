# ZDI-10-172: Mozilla Firefox tree Object Removal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-172
- **ZDI-CAN:** ZDI-CAN-817
- **Date:** 2010-09-13
- **CVE:** CVE-2010-3168
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-172/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the support for XUL <tree> objects. If a specific property of a tree object is set and the parent node attempts to remove the child, the process can be made to access invalid memory. This can be abused by an attacker to execute remote code under the context of the user running the browser.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-55.html

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-09-13 - Coordinated public release of advisory
