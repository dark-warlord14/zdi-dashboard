# ZDI-22-1501: D-Link DIR-1935 SOAPAction Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1501
- **ZDI-CAN:** ZDI-CAN-16150
- **Date:** 2022-11-03
- **CVE:** CVE-2022-43630
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-1935
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1501/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-1935 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of http requests to the web management portal. When parsing the SOAPAction header, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10310

## Disclosure Timeline

- 2022-07-22 - Vulnerability reported to vendor
- 2022-11-03 - Coordinated public release of advisory
