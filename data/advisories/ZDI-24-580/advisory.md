# ZDI-24-580: Microsoft Artifact Registry Container Images Empty Password Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-580
- **ZDI-CAN:** ZDI-CAN-22149
- **Date:** 2024-06-06
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Artifact Registry
- **Credit:** Alfredo Oliveira and Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-580/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Microsoft Artifact Registry Container images. Authentication is not required to exploit this vulnerability. The specific flaw exists within the default credentials set within the image. The issue results from the use of empty root password. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

## Disclosure Timeline

- 2023-09-20 - Vulnerability reported to vendor
- 2024-06-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
