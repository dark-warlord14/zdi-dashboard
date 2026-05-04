# ZDI-24-441: Delta Electronics CNCSoft-B DOPSoft Uncontrolled Search Path Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-441
- **ZDI-CAN:** ZDI-CAN-21884
- **Date:** 2024-05-13
- **CVE:** CVE-2024-1595
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** CNCSoft-B
- **Credit:** Sean de Regge
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-441/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics CNCSoft-B. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the loading of DLL images during the startup of the DOPSoft component. The process does not restrict DLL search to trusted paths, which can result in the loading of a malicious DLL. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-053-01

## Disclosure Timeline

- 2023-08-22 - Vulnerability reported to vendor
- 2024-05-13 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
