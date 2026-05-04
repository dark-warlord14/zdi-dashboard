# ZDI-17-696: Microsoft Edge DOMAttrModified Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-696
- **ZDI-CAN:** ZDI-CAN-4884
- **Date:** 2017-08-24
- **CVE:** CVE-2017-8496
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Jose A. Vazquez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-696/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the DOMAttrModified event. By manipulating a document's elements an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8496

## Disclosure Timeline

- 2017-06-12 - Vulnerability reported to vendor
- 2017-08-24 - Coordinated public release of advisory
