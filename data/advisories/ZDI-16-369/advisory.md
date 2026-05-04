# ZDI-16-369: Microsoft Windows PDF Library AES Encryption Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-369
- **ZDI-CAN:** ZDI-CAN-3811
- **Date:** 2016-06-22
- **CVE:** CVE-2016-3203
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows PDF Library
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-369/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows PDF Library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AES crypt filters. A crafted Length of an AES crypt filter object can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-080

## Disclosure Timeline

- 2016-05-31 - Vulnerability reported to vendor
- 2016-06-22 - Coordinated public release of advisory
