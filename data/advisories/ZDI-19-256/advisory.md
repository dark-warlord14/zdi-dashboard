# ZDI-19-256: Jaspersoft JasperReports Server ResourceForwardingServlet URI Improper Access Control Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-256
- **ZDI-CAN:** ZDI-CAN-7655
- **Date:** 2019-03-06
- **CVE:** CVE-2018-18815
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Jaspersoft
- **Affected Products:** Jasper Reports
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-256/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Jaspersoft JasperReports Server. Authentication is not required to exploit this vulnerability. The specific flaw exists in the doGet method of the ResourceForwardingServlet. The issue results from the lack of proper filtering of URLs. An attacker can leverage this in conjunction with other vulnerabilities to bypass authentication on the system.

## Additional Details

Jaspersoft has issued an update to correct this vulnerability. More details can be found at: https://www.tibco.com/support/advisories/2019/03/tibco-security-advisory-march-6-2019-tibco-jasperreports-server-2018-18815

## Disclosure Timeline

- 2018-12-11 - Vulnerability reported to vendor
- 2019-03-06 - Coordinated public release of advisory
