# ZDI-17-728: Microsoft Windows PDF Library JPEG2000 Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-728
- **ZDI-CAN:** ZDI-CAN-4844
- **Date:** 2017-09-12
- **CVE:** CVE-2017-8737
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows PDF Library
- **Credit:** Giwan Go of STEALIEN & HIT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-728/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows PDF Library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JPEG2000 images. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8737

## Disclosure Timeline

- 2017-06-01 - Vulnerability reported to vendor
- 2017-09-12 - Coordinated public release of advisory
