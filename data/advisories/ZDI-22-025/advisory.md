# ZDI-22-025: Delta Industrial Automation DIAScreen XLS File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-025
- **ZDI-CAN:** ZDI-CAN-13033
- **Date:** 2022-01-11
- **CVE:** CVE-2021-32965
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DIAScreen
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-025/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation DIAScreen. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-21-208-05

## Disclosure Timeline

- 2021-03-17 - Vulnerability reported to vendor
- 2022-01-11 - Coordinated public release of advisory
