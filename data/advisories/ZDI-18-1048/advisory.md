# ZDI-18-1048: Microsoft Internet Explorer Table Row NULL Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1048
- **ZDI-CAN:** ZDI-CAN-6262
- **Date:** 2018-09-14
- **CVE:** CVE-2018-8447
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** ca0nguyen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of table rows. By manipulating a document's elements, an attacker can trigger a read from an array based at address zero. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8447

## Disclosure Timeline

- 2018-05-31 - Vulnerability reported to vendor
- 2018-09-14 - Coordinated public release of advisory
- 2018-09-14 - Advisory Updated
