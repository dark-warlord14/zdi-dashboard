# ZDI-22-1436: Altair HyperView Player H3D File Parsing Uninitialized Memory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1436
- **ZDI-CAN:** ZDI-CAN-14889
- **Date:** 2022-10-14
- **CVE:** CVE-2022-2949
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Altair
- **Affected Products:** HyperView Player
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1436/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Altair HyperView Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of H3D files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Altair has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-284-01

## Disclosure Timeline

- 2022-04-06 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
