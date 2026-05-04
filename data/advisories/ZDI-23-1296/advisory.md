# ZDI-23-1296: D-Link DAP-1325 HNAP SetAPLanSettings DeviceName Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1296
- **ZDI-CAN:** ZDI-CAN-18808
- **Date:** 2023-09-07
- **CVE:** CVE-2023-41188
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1325
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1296/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-1325 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of a request parameter provided to the HNAP1 SOAP endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10351

## Disclosure Timeline

- 2022-09-26 - Vulnerability reported to vendor
- 2023-09-07 - Coordinated public release of advisory
