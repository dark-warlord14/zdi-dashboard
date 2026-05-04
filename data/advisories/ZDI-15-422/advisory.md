# ZDI-15-422: Microsoft Internet Explorer mergeAttributes Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-422
- **ZDI-CAN:** ZDI-CAN-2971
- **Date:** 2015-09-08
- **CVE:** CVE-2015-2486
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 0016EECD9D7159A949DAD3BC17E0A939
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-422/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer performs merging of HTML attributes. By manipulating a document's elements, an attacker can cause an object in memory to be processed as if it were a different type of object. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms15-095

## Disclosure Timeline

- 2015-06-01 - Vulnerability reported to vendor
- 2015-09-08 - Coordinated public release of advisory
