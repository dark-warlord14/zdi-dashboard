# ZDI-23-1214: (0Day) LG Simple Editor getServerSetting Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1214
- **ZDI-CAN:** ZDI-CAN-20012
- **Date:** 2023-08-24
- **CVE:** CVE-2023-40510
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** LG
- **Affected Products:** Simple Editor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1214/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of LG Simple Editor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getServerSetting method. The issue results from the exposure of plaintext credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

02/13/23 – The ZDI requested a vendor PSIRT contact. 02/14/23 – The vendor provided PSIRT Contact information. 02/14/23 – The ZDI reported the vulnerability to the vendor. 08/04/23 – The ZDI asked for an update. 08/08/23 – The vendor states that they do not have plans to fix the vulnerability now or in the future. 08/21/23 – The ZDI informed the vendor that we are publishing the case as a zero-day advisory on 08/24/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-02-14 - Vulnerability reported to vendor
- 2023-08-24 - Coordinated public release of advisory
