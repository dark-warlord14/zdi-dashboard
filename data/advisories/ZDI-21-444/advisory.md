# ZDI-21-444: Delta Industrial Automation CNCSoft-B DOPSoft DPA File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-444
- **ZDI-CAN:** ZDI-CAN-12418
- **Date:** 2021-04-22
- **CVE:** CVE-2021-22664
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** CNCSoft-B DOPSoft
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-444/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation CNCSoft-B DOPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPA files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-110-05

## Disclosure Timeline

- 2021-01-13 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
