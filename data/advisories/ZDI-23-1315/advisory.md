# ZDI-23-1315: D-Link DAP-1325 SetHostIPv6StaticSettings StaticAddress Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1315
- **ZDI-CAN:** ZDI-CAN-18833
- **Date:** 2023-09-07
- **CVE:** CVE-2023-41207
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1325
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1315/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-1325 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of XML data provided to the HNAP1 SOAP endpoint. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10351

## Disclosure Timeline

- 2022-09-28 - Vulnerability reported to vendor
- 2023-09-07 - Coordinated public release of advisory
