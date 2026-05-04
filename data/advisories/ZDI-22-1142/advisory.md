# ZDI-22-1142: Measuresoft ScadaPro Server ORM File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1142
- **ZDI-CAN:** ZDI-CAN-16262
- **Date:** 2022-08-23
- **CVE:** CVE-2022-2895
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Measuresoft
- **Affected Products:** ScadaPro Server
- **Credit:** @rgod777
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1142/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Measuresoft ScadaPro Server. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ORM files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Measuresoft has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-235-06

## Disclosure Timeline

- 2022-02-04 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
