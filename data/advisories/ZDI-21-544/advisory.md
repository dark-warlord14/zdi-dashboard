# ZDI-21-544: Foxit Reader XFA Form Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-544
- **ZDI-CAN:** ZDI-CAN-13100
- **Date:** 2021-05-07
- **CVE:** CVE-2021-31455
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Yongil Lee(@intellee) and Wonyoung Jung(@nonetype) of Diffense
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-544/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XFA forms. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2021-03-03 - Vulnerability reported to vendor
- 2021-05-07 - Coordinated public release of advisory
- 2021-05-07 - Advisory Updated
