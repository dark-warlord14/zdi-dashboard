# ZDI-16-370: Microsoft Windows PDF Library JPEG2000 COD Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-370
- **ZDI-CAN:** ZDI-CAN-3810
- **Date:** 2016-06-22
- **CVE:** CVE-2016-3215
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows PDF Library
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-370/
## Vulnerability Details

This vulnerability allows a remote attacker to disclose sensitive information on vulnerable installations of Microsoft Windows PDF Library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG2000 files. A crafted number of decomposition levels in a COD marker can trigger a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-080

## Disclosure Timeline

- 2016-05-31 - Vulnerability reported to vendor
- 2016-06-22 - Coordinated public release of advisory
