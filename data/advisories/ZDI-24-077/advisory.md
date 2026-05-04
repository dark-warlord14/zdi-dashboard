# ZDI-24-077: Trend Micro Apex Central Unrestricted File Upload Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-077
- **ZDI-CAN:** ZDI-CAN-20803
- **Date:** 2024-01-19
- **CVE:** CVE-2023-52324
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex Central
- **Credit:** Poh Jia Hao of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-077/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Trend Micro Apex Central. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of uploaded ZIP files. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of IUSR.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000296153?language=en_US

## Disclosure Timeline

- 2023-07-18 - Vulnerability reported to vendor
- 2024-01-19 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
