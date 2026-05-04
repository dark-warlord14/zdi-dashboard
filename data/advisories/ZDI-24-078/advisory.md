# ZDI-24-078: Trend Micro Mobile Security for Enterprises DevicesManagementEditNotePopupTip Cross-Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-078
- **ZDI-CAN:** ZDI-CAN-20804
- **Date:** 2024-01-19
- **CVE:** CVE-2023-41176
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** Mobile Security for Enterprises
- **Credit:** Poh Jia Hao of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-078/
## Vulnerability Details

This vulnerability allows remote attackers to execute web requests with the victim's privileges on affected installations of Trend Micro Mobile Security for Enterprises. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the DevicesManagementEditNotePopupTip endpoint. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to interact with the application in the context of the target user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000294695?language=en_US

## Disclosure Timeline

- 2023-05-01 - Vulnerability reported to vendor
- 2024-01-19 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
