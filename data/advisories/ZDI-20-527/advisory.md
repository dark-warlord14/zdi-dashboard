# ZDI-20-527: Foxit Reader XFA Template Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-527
- **ZDI-CAN:** ZDI-CAN-10132
- **Date:** 2020-04-16
- **CVE:** CVE-2020-10899
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** hungtt28 of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-527/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of XFA templates. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2020-02-04 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
