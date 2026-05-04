# ZDI-19-908: Foxit Studio Photo JPEG Batch Processing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-908
- **ZDI-CAN:** ZDI-CAN-8809
- **Date:** 2019-10-22
- **CVE:** CVE-2019-17138
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** Studio Photo
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-908/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Foxit Studio Photo. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the conversion from JPEG to EPS. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-06-21 - Vulnerability reported to vendor
- 2019-10-22 - Coordinated public release of advisory
