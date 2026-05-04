# ZDI-23-892: D-Link DIR-X3260 prog.cgi SOAPAction Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-892
- **ZDI-CAN:** ZDI-CAN-20983
- **Date:** 2023-06-30
- **CVE:** CVE-2023-35723
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-X3260
- **Credit:** Nicholas Zubrisky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-892/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-X3260 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the SOAPAction request header provided to the prog.cgi endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10345

## Disclosure Timeline

- 2023-05-09 - Vulnerability reported to vendor
- 2023-06-30 - Coordinated public release of advisory
