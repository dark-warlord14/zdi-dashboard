# ZDI-19-433: Foxit Reader ConvertToPDF BMP File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-433
- **ZDI-CAN:** ZDI-CAN-7614
- **Date:** 2019-04-29
- **CVE:** CVE-2019-6759
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Hao Li from ADLab of VenusTech
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-433/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within ConvertToPDF_x86.dll. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-01-17 - Vulnerability reported to vendor
- 2019-04-29 - Coordinated public release of advisory
