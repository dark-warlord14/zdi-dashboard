# ZDI-20-939: Delta Industrial Automation CNCSoft ScreenEditor DPB File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-939
- **ZDI-CAN:** ZDI-CAN-10890
- **Date:** 2020-08-05
- **CVE:** CVE-2020-16199
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** CNCSoft ScreenEditor
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-939/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation CNCSoft ScreenEditor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPB files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-217-01

## Disclosure Timeline

- 2020-04-09 - Vulnerability reported to vendor
- 2020-08-05 - Coordinated public release of advisory
