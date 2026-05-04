# ZDI-15-136: Microsoft Internet Explorer Layout::FlowBoxBuilder Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-136
- **ZDI-CAN:** ZDI-CAN-2669
- **Date:** 2015-04-15
- **CVE:** CVE-2015-1659
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Jason Kratzer
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-136/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Layout::FlowBoxBuilder objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-032.aspx

## Disclosure Timeline

- 2015-01-06 - Vulnerability reported to vendor
- 2015-04-15 - Coordinated public release of advisory
