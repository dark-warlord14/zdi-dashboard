# ZDI-21-182: Omron CX-One NCI File Parsing Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-182
- **ZDI-CAN:** ZDI-CAN-11807
- **Date:** 2021-02-10
- **CVE:** CVE-2020-27259
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-One
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-182/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Omron CX-One. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of NCI files by the CX-Position application. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-007-02

## Disclosure Timeline

- 2020-09-04 - Vulnerability reported to vendor
- 2021-02-10 - Coordinated public release of advisory
