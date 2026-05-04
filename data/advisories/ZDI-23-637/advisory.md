# ZDI-23-637: Schneider Electric APC Easy UPS Online UpLoadAction Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-637
- **ZDI-CAN:** ZDI-CAN-17584
- **Date:** 2023-05-17
- **CVE:** CVE-2022-42971
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** APC Easy UPS Online
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-637/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric APC Easy UPS Online. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UpLoadAction class. When parsing the filename parameter, the process does not properly validate user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-22-347-02

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
