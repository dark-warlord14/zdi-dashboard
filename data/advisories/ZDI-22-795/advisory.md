# ZDI-22-795: Delta Industrial Automation ASDA-Soft SCP File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-795
- **ZDI-CAN:** ZDI-CAN-14471
- **Date:** 2022-05-26
- **CVE:** CVE-2022-1402
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** ASDA-Soft
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-795/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation ASDA-Soft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SCP files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-111-01

## Disclosure Timeline

- 2021-11-18 - Vulnerability reported to vendor
- 2022-05-26 - Coordinated public release of advisory
