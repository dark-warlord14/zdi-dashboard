# ZDI-18-1386: Adobe Reader DC AFLayoutInfo Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1386
- **ZDI-CAN:** ZDI-CAN-6655
- **Date:** 2018-12-12
- **CVE:** CVE-2018-16003
- **CVSS:** 8.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Sebastian Apelt (@bitshifter123)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1386/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AFLayoutInfo objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-07-07 - Vulnerability reported to vendor
- 2018-12-12 - Coordinated public release of advisory
