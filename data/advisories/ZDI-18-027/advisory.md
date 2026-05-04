# ZDI-18-027: Advantech WebAccess LogList ChkAdminViewUsrPwd1 SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-027
- **ZDI-CAN:** ZDI-CAN-4995
- **Date:** 2018-01-05
- **CVE:** CVE-2017-16716
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-027/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within ChkAdminViewUsrPwd1, called from LogList.asp. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code under the context of the web service.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-004-02

## Disclosure Timeline

- 2017-08-04 - Vulnerability reported to vendor
- 2018-01-05 - Coordinated public release of advisory
