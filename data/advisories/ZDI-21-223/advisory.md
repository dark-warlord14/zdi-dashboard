# ZDI-21-223: Siemens JT2Go DXF File Parsing Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-223
- **ZDI-CAN:** ZDI-CAN-11993
- **Date:** 2021-02-24
- **CVE:** CVE-2021-25175
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-223/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DXF files. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-040-06

## Disclosure Timeline

- 2020-10-30 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
