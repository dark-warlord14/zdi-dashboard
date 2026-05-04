# ZDI-18-612: (Pwn2Own) Microsoft Edge WebGL ImageData Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-612
- **ZDI-CAN:** ZDI-CAN-5814
- **Date:** 2018-07-12
- **CVE:** CVE-2018-1025
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-612/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ImageData objects in WebGL. By performing actions in JavaScript an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-1025

## Disclosure Timeline

- 2018-03-18 - Vulnerability reported to vendor
- 2018-07-12 - Coordinated public release of advisory
- 2018-07-12 - Advisory Updated
