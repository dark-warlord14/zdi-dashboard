# ZDI-21-550: Foxit Reader app.media Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-550
- **ZDI-CAN:** ZDI-CAN-13333
- **Date:** 2021-05-07
- **CVE:** CVE-2021-31461
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** cor3sm4sh3r working with Volon Cyber Security Pvt Ltd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-550/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the the handling of app.media objects. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2021-03-31 - Vulnerability reported to vendor
- 2021-05-07 - Coordinated public release of advisory
- 2021-05-07 - Advisory Updated
