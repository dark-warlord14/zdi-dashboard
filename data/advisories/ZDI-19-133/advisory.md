# ZDI-19-133: Foxit Reader XFA remerge Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-133
- **ZDI-CAN:** ZDI-CAN-7347
- **Date:** 2019-01-25
- **CVE:** CVE-2019-6727
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Sebastian Apelt (@bitshifter123)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-133/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the XFA remerge method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-10-07 - Vulnerability reported to vendor
- 2019-01-25 - Coordinated public release of advisory
