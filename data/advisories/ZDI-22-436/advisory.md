# ZDI-22-436: Fatek Automation FvDesigner FPJ File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-436
- **ZDI-CAN:** ZDI-CAN-14853
- **Date:** 2022-03-07
- **CVE:** CVE-2022-21209
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fatek Automation
- **Affected Products:** FvDesigner
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-436/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fatek Automation FvDesigner. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FPJ files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fatek Automation has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-055-01

## Disclosure Timeline

- 2021-10-06 - Vulnerability reported to vendor
- 2022-03-07 - Coordinated public release of advisory
