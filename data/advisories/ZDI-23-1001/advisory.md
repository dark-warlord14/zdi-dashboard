# ZDI-23-1001: Trend Micro Apex Central modTXSO Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1001
- **ZDI-CAN:** ZDI-CAN-20329
- **Date:** 2023-07-26
- **CVE:** CVE-2023-38627
- **CVSS:** 9.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:L/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex Central
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1001/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Trend Micro Apex Central. Authentication is required to exploit this vulnerability. The specific flaw exists within the modTXSO module. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000294176

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-07-26 - Coordinated public release of advisory
