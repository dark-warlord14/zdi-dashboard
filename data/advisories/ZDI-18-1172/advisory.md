# ZDI-18-1172: Foxit Reader gotoNamedDest Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1172
- **ZDI-CAN:** ZDI-CAN-6851
- **Date:** 2018-10-11
- **CVE:** CVE-2018-17678
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Abago Forgans
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1172/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the gotoNamedDest method of a app object. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-07-22 - Vulnerability reported to vendor
- 2018-10-11 - Coordinated public release of advisory
