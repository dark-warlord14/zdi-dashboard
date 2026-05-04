# ZDI-23-652: Trend Micro Apex Central modTMMS SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-652
- **ZDI-CAN:** ZDI-CAN-17688
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32529
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex Central
- **Credit:** Poh Jia Hao of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-652/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Apex Central. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of delete_cert_vec requests to the modTMMS endpoint. When parsing the id parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the IUSR user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000293107

## Disclosure Timeline

- 2022-07-26 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
