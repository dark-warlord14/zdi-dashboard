# ZDI-22-575: Omron CX-One CX-Position NCI File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-575
- **ZDI-CAN:** ZDI-CAN-14674
- **Date:** 2022-04-05
- **CVE:** CVE-2022-26419
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-One
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-575/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Omron CX-One. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of NCI files in the CX-Position module. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-088-02

## Disclosure Timeline

- 2021-10-06 - Vulnerability reported to vendor
- 2022-04-05 - Coordinated public release of advisory
