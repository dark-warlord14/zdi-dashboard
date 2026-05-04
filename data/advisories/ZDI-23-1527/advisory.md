# ZDI-23-1527: Microsoft PC Manager SAS Token Incorrect Permission Assignment Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1527
- **ZDI-CAN:** ZDI-CAN-22263
- **Date:** 2023-10-05
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** PC Manager
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1527/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on Microsoft PC Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the permissions granted to an SAS token. An attacker can leverage this vulnerability to launch a supply-chain attack and execute arbitrary code on customers' endpoints.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

## Disclosure Timeline

- 2023-09-28 - Vulnerability reported to vendor
- 2023-10-05 - Coordinated public release of advisory
