# ZDI-18-428: Microsoft Edge Undo Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-428
- **ZDI-CAN:** ZDI-CAN-5622
- **Date:** 2018-05-14
- **CVE:** CVE-2018-1021
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** akayn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-428/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of undo functionality available to script. By manipulating a document's elements, an attacker can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-1021

## Disclosure Timeline

- 2018-01-30 - Vulnerability reported to vendor
- 2018-05-14 - Coordinated public release of advisory
- 2018-05-14 - Advisory Updated
