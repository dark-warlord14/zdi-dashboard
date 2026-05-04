# ZDI-21-419: Siemens RobotExpert CELL File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-419
- **ZDI-CAN:** ZDI-CAN-12608
- **Date:** 2021-04-15
- **CVE:** CVE-2021-25670
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** RobotExpert
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-419/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens RobotExpert. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CELL files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://cert-portal.siemens.com/productcert/pdf/ssa-163226.pdf https://us-cert.cisa.gov/ics/advisories/icsa-21-103-12

## Disclosure Timeline

- 2021-01-05 - Vulnerability reported to vendor
- 2021-04-15 - Coordinated public release of advisory
