# ZDI-20-213: Foxit Reader Annotations AcroForm Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-213
- **ZDI-CAN:** ZDI-CAN-9862
- **Date:** 2020-02-11
- **CVE:** CVE-2020-8857
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** hungtt28
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-213/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of form Annotation objects within AcroForms. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-12-11 - Vulnerability reported to vendor
- 2020-02-11 - Coordinated public release of advisory
