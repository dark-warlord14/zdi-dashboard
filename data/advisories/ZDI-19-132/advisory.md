# ZDI-19-132: Foxit Reader ConvertToPDF TIF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-132
- **ZDI-CAN:** ZDI-CAN-7593
- **Date:** 2019-01-25
- **CVE:** CVE-2019-5005
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** HAO LI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-132/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within ConvertToPDF_x86.dll. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-01-04 - Vulnerability reported to vendor
- 2019-01-25 - Coordinated public release of advisory
- 2020-05-08 - Advisory Updated
