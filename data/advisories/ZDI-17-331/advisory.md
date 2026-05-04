# ZDI-17-331: Hewlett Packard Enterprise Network Automation RedirectServlet SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-331
- **ZDI-CAN:** ZDI-CAN-4219
- **Date:** 2017-05-11
- **CVE:** CVE-2017-5810
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Network Automation
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-331/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Network Automation. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RedirectServlet component. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute SQL under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: http://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbgn03740en_us

## Disclosure Timeline

- 2016-12-15 - Vulnerability reported to vendor
- 2017-05-11 - Coordinated public release of advisory
