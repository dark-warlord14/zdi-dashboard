# ZDI-18-1185: Foxit Reader ConvertToPDF BMP File Parsing Out-of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1185
- **ZDI-CAN:** ZDI-CAN-6844
- **Date:** 2018-10-11
- **CVE:** CVE-2018-17686
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1185/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of BMP images. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-07-22 - Vulnerability reported to vendor
- 2018-10-11 - Coordinated public release of advisory
