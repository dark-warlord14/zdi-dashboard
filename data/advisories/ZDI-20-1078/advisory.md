# ZDI-20-1078: Foxit Studio Photo PSD File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1078
- **ZDI-CAN:** ZDI-CAN-11003
- **Date:** 2020-08-21
- **CVE:** CVE-2020-17403
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Studio Photo
- **Credit:** Pengsu Cheng of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1078/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit Studio Photo. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PSD files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.html

## Disclosure Timeline

- 2020-04-28 - Vulnerability reported to vendor
- 2020-08-21 - Coordinated public release of advisory
