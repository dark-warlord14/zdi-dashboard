# ZDI-21-1151: Schneider Electric IGSS Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1151
- **ZDI-CAN:** ZDI-CAN-13892
- **Date:** 2021-10-14
- **CVE:** CVE-2021-22803
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** Vyacheslav Moskvin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1151/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric IGSS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of TCP traffic by the dc.exe process. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the user running IGSS.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-285-03

## Disclosure Timeline

- 2021-07-30 - Vulnerability reported to vendor
- 2021-10-14 - Coordinated public release of advisory
