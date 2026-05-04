# ZDI-24-052: Trend Micro Apex Central modVulnerabilityProtect Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-052
- **ZDI-CAN:** ZDI-CAN-21888
- **Date:** 2024-01-11
- **CVE:** CVE-2023-52331
- **CVSS:** 9.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:L/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex Central
- **Credit:** Poh Jia Hao of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-052/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Trend Micro Apex Central. Authentication is required to exploit this vulnerability. The specific flaw exists within the modVulnerabilityProtect module. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000296153?language=en_US

## Disclosure Timeline

- 2023-10-03 - Vulnerability reported to vendor
- 2024-01-11 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
