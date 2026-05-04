# ZDI-19-1031: D-Link DCS-960L HNAP SOAPAction Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1031
- **ZDI-CAN:** ZDI-CAN-8458
- **Date:** 2019-12-23
- **CVE:** CVE-2019-17146
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DCS-960L
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1031/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of D-Link DCS-960L. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HNAP service, which listens on TCP port 80 by default. When parsing the SOAPAction request header, the process does not properly validate the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the admin user.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10142

## Disclosure Timeline

- 2019-09-27 - Vulnerability reported to vendor
- 2019-12-23 - Coordinated public release of advisory
