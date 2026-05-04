# ZDI-19-438: Foxit Reader XFA Template Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-438
- **ZDI-CAN:** ZDI-CAN-7972
- **Date:** 2019-04-29
- **CVE:** CVE-2019-6764
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** hungtt28 of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-438/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of XFA Template objects. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-03-01 - Vulnerability reported to vendor
- 2019-04-29 - Coordinated public release of advisory
