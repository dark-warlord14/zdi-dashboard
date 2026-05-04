# ZDI-23-1391: PDF-XChange Editor mailForm Use-After-Free Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1391
- **ZDI-CAN:** ZDI-CAN-20663
- **Date:** 2023-09-08
- **CVE:** CVE-2023-42040
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1391/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the mailForm method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

PDF-XChange has issued an update to correct this vulnerability. More details can be found at: https://www.tracker-software.com/support/security-bulletins.html

## Disclosure Timeline

- 2023-04-07 - Vulnerability reported to vendor
- 2023-09-08 - Coordinated public release of advisory
