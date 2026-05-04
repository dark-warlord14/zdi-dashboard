# ZDI-22-324: Schneider Electric IGSS Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-324
- **ZDI-CAN:** ZDI-CAN-15193
- **Date:** 2022-02-11
- **CVE:** CVE-2022-24317
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** Vyacheslav Moskvin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-324/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Schneider Electric IGSS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IGSSDataServer process, which listens on TCP port 12401 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose information from the IGSS application.

## Additional Details

https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2022-039-01 https://www.cisa.gov/uscert/ics/advisories/icsa-22-046-01

## Disclosure Timeline

- 2021-12-15 - Vulnerability reported to vendor
- 2022-02-11 - Coordinated public release of advisory
- 2023-09-20 - Advisory Updated
