# ZDI-18-421: Trend Micro Smart Protection Server BWListMgmt SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-421
- **ZDI-CAN:** ZDI-CAN-5807
- **Date:** 2018-05-04
- **CVE:** CVE-2018-10350
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Smart Protection Server
- **Credit:** Fabius Artrel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-421/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Smart Protection Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of parameters provided to wcs\_bwlists\_handler.php. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to remotely execute code under the context of webserv.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119715

## Disclosure Timeline

- 2018-03-21 - Vulnerability reported to vendor
- 2018-05-04 - Coordinated public release of advisory
- 2018-05-04 - Advisory Updated
