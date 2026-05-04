# ZDI-21-052: Siemens JT2Go CG4 and CGM File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-052
- **ZDI-CAN:** ZDI-CAN-11898
- **Date:** 2021-01-14
- **CVE:** CVE-2020-26982
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-052/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CG4 and CGM files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-012-03/

## Disclosure Timeline

- 2020-09-30 - Vulnerability reported to vendor
- 2021-01-14 - Coordinated public release of advisory
