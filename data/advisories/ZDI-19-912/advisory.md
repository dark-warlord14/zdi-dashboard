# ZDI-19-912: Foxit PhantomPDF ListBox Field Keystroke Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-912
- **ZDI-CAN:** ZDI-CAN-9081
- **Date:** 2019-10-22
- **CVE:** CVE-2019-17142
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** RockStar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-912/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of script within a Keystroke action of a listbox field. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-09-13 - Vulnerability reported to vendor
- 2019-10-22 - Coordinated public release of advisory
