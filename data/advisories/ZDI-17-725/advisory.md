# ZDI-17-725: Microsoft Edge Undo Command Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-725
- **ZDI-CAN:** ZDI-CAN-4888
- **Date:** 2017-09-12
- **CVE:** CVE-2017-8661
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** 0011
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-725/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the Undo command in HTML documents. By performing actions in JavaScript an attacker can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8661

## Disclosure Timeline

- 2017-06-12 - Vulnerability reported to vendor
- 2017-09-12 - Coordinated public release of advisory
