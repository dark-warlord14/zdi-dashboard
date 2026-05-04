# ZDI-24-784: PaperCut MF handleServiceException Cross-Site Scripting Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-784
- **ZDI-CAN:** ZDI-CAN-23254
- **Date:** 2024-06-18
- **CVE:** CVE-2024-1883
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** PaperCut
- **Affected Products:** MF
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-784/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of PaperCut MF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handleServiceException method. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/Security-Bulletin-March-2024

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
