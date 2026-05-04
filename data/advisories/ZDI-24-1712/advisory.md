# ZDI-24-1712: Tibbo Aggregate Network Manager UploaderTempFileController Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1712
- **ZDI-CAN:** ZDI-CAN-24941
- **Date:** 2024-12-19
- **CVE:** CVE-2024-12700
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tibbo
- **Affected Products:** Aggregate Network Manager
- **Credit:** Vu Khanh Trinh (@Sonicrr) of VNPT Cyber Immunity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1712/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tibbo Aggregate Network Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the UploaderTempFileController class. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

Tibbo has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-354-05

## Disclosure Timeline

- 2024-09-19 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2024-12-19 - Advisory Updated
