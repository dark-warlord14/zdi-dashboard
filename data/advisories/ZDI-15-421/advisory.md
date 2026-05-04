# ZDI-15-421: Microsoft Internet Explorer Element ID Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-421
- **ZDI-CAN:** ZDI-CAN-2962
- **Date:** 2015-09-08
- **CVE:** CVE-2015-2485
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 0016EECD9D7159A949DAD3BC17E0A939
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-421/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes the IDs of HTML elements. By manipulating a document's elements an attacker can cause a CPtrAry<CDOMNode*> object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms15-095

## Disclosure Timeline

- 2015-05-28 - Vulnerability reported to vendor
- 2015-09-08 - Coordinated public release of advisory
