# ZDI-24-895: Progress Software WhatsUp Gold APM Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-895
- **ZDI-CAN:** ZDI-CAN-22319
- **Date:** 2024-07-03
- **CVE:** CVE-2024-5008
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Le Ngoc Anh (@L3ng0c4nh) and Nguy Minh Tuan (@minhtuanact) of Sun* Cyber Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-895/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Progress Software WhatsUp Gold. Authentication is required to exploit this vulnerability. The specific flaw exists within the APM module. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-June-2024

## Disclosure Timeline

- 2024-04-03 - Vulnerability reported to vendor
- 2024-07-03 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
