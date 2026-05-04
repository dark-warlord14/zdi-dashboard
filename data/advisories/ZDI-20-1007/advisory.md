# ZDI-20-1007: Schneider Electric APC Easy UPS Online SoundUploadServlet processRequest Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1007
- **ZDI-CAN:** ZDI-CAN-10605
- **Date:** 2020-08-17
- **CVE:** CVE-2020-7522
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** APC Easy UPS Online
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1007/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric APC Easy UPS Online. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SoundUploadServlet class. When parsing the filename parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-224-02

## Disclosure Timeline

- 2020-04-14 - Vulnerability reported to vendor
- 2020-08-17 - Coordinated public release of advisory
