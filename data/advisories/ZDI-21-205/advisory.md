# ZDI-21-205: D-Link DAP-2020 errorpage External Control of File Name Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-205
- **ZDI-CAN:** ZDI-CAN-11856
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27250
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-2020
- **Credit:** SUID
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-205/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of D-Link DAP-2020 Wi-Fi access points. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of CGI scripts. When parsing the errorpage request parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10201

## Disclosure Timeline

- 2020-09-08 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
