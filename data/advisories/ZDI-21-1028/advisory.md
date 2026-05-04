# ZDI-21-1028: Fatek Automation FvDesigner FPJ File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1028
- **ZDI-CAN:** ZDI-CAN-13392
- **Date:** 2021-08-27
- **CVE:** CVE-2021-32939
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fatek Automation
- **Affected Products:** FvDesigner
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1028/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fatek Automation FvDesigner. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FPJ files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fatek Automation has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-217-02

## Disclosure Timeline

- 2021-04-14 - Vulnerability reported to vendor
- 2021-08-27 - Coordinated public release of advisory
