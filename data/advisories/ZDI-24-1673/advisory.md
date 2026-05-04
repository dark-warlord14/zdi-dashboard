# ZDI-24-1673: AutomationDirect C-More EA9 EAP9 File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1673
- **ZDI-CAN:** ZDI-CAN-24772
- **Date:** 2024-12-11
- **CVE:** CVE-2024-11609
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** AutomationDirect
- **Affected Products:** C-More EA9
- **Credit:** Andrea Micalizzi aka rgod (@rgod777)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1673/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of AutomationDirect C-More EA9. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EAP9 files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

AutomationDirect has issued an update to correct this vulnerability. More details can be found at: https://certvde.com/en/bulletins/bulletins/2182-automationdirect-c-more-ea9-programming-software/

## Disclosure Timeline

- 2024-07-30 - Vulnerability reported to vendor
- 2024-12-11 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated
