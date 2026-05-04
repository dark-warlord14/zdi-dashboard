# ZDI-25-296: Trend Micro Apex Central modTMCM Unrestricted File Upload Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-296
- **ZDI-CAN:** ZDI-CAN-25331
- **Date:** 2025-05-21
- **CVE:** CVE-2025-47866
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex Central
- **Credit:** Poh Jia Hao of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-296/
## Vulnerability Details

This vulnerability allows remote attackers to upload arbitrary files on affected installations of Trend Micro Apex Central. Authentication is required to exploit this vulnerability. The specific flaw exists within the modTMCM webapp widget. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of IUSR.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019355

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2025-05-21 - Coordinated public release of advisory
- 2025-05-21 - Advisory Updated
